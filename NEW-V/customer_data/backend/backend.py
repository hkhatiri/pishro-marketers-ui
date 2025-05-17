# customer_data/backend/backend.py
import datetime
import math
import random # برای user_id موقت
from typing import List, Optional, Union, Dict, Tuple, Any
from collections import Counter

import reflex as rx
from bson import ObjectId
import jdatetime
import pytz

# --- Import های داخلی پکیج backend ---
# این import ها باید به درستی کار کنند اگر ساختار پوشه صحیح باشد
# و فایل __init__.py (حتی خالی) در پوشه backend وجود داشته باشد.
try:
    from .mongo import Mongo, ChatState # ChatState از mongo.py شما می‌آید
    from .auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL, REFERRAL_LEVEL_CONFIG
except ImportError as e:
    print(f"ImportError in backend.py, trying absolute: {e}")
    # فال‌بک به import مطلق اگر برنامه از یک context دیگر اجرا شود (مثلاً تست‌ها)
    # اما در حالت عادی اجرای reflex run از ریشه پروژه، import نسبی باید کار کند.
    from customer_data.backend.mongo import Mongo, ChatState # type: ignore
    from customer_data.backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL, REFERRAL_LEVEL_CONFIG # type: ignore


# --- تعاریف اولیه ---
CHAT_STATE_TRANSLATIONS: Dict[str, str] = {
    "HasAccess": "دسترسی دارد", "HasManualAccess": "دسترسی دستی",
    "INITED": "کاربر جدید", "BLOCKED": "مسدود",
    "WaitForNationalId": "در انتظار کدملی", "WaitForOTP": "در انتظار کد",
    "WaitForCaptcha": "در انتظار کپچا", "LoggedIn": "لاگین شده",
    # اضافه کردن سایر وضعیت‌ها اگر لازم است
    "UNKNOWN_STATE": "وضعیت نامشخص" # برای مقادیر غیرمنتظره
}

class MongoUserDisplay(rx.Base):
    _id_str: Optional[str] = None
    username: Optional[str] = None
    national_id: Optional[str] = None
    raw_chat_state: Optional[str] = None # مقدار خام از دیتابیس
    chat_state_fa: Optional[str] = None # ترجمه فارسی
    created_at_str: Optional[str] = None
    updated_at_str: Optional[str] = None # این را اگر لازم دارید اضافه کنید
    created_at_ts: Optional[float] = None
    channel_count: int = 0
    level: Optional[str] = None

class MonthValues(rx.Base): # برای آمارهای مقایسه‌ای ماهانه (فعلاً ساده)
    num_customers: int = 0

_mongo_client_global_instance: Optional[Mongo] = None
YOUR_MONGO_DB_NAME = "marketersbot" # نام دیتابیس شما در MongoDB
TEHRAN_TZ = pytz.timezone('Asia/Tehran')

def get_mongo_client_instance() -> Mongo:
    global _mongo_client_global_instance
    if _mongo_client_global_instance is None:
        _mongo_client_global_instance = Mongo(mongo_db_name=YOUR_MONGO_DB_NAME)
    return _mongo_client_global_instance

# ==============================================================================
# کلاس اصلی State
# ==============================================================================
class State(rx.State):
    # متغیرهای مربوط به جدول و صفحه‌بندی
    users: list[MongoUserDisplay] = []
    current_user_for_edit: Optional[MongoUserDisplay] = None
    sort_value: str = "created_at_ts" # ستون پیش‌فرض برای مرتب‌سازی (timestamp)
    sort_reverse: bool = True # مرتب‌سازی نزولی (جدیدترین‌ها اول)
    search_value: str = ""
    current_page_number: int = 1
    users_per_page: int = 10 # تعداد کاربران در هر صفحه

    # متغیرهای مربوط به آمار کلی
    total_registered_users: int = 0
    user_counts_by_level: Dict[str, int] = {} # شمارش کاربران برای هر سطح
    users_in_channels_count: int = 0 # کل کاربرانی که حداقل در یک کانال عضو هستند

    # متغیرهای جدید برای آمار وضعیت دسترسی
    user_counts_by_chat_state: dict[str, int] = {} # شمارش کاربران بر اساس وضعیت کلی
    channel_members_counts_by_chat_state: dict[str, int] = {} # شمارش اعضای کانال بر اساس وضعیت

    # --------------------------------------------------------------------------
    # Var های محاسباتی برای نمایش در UI
    # --------------------------------------------------------------------------
    @rx.var
    def paginated_users(self) -> list[MongoUserDisplay]:
        start_index = (self.current_page_number - 1) * self.users_per_page
        end_index = start_index + self.users_per_page
        return self._processed_users_for_display[start_index:end_index]

    @rx.var
    def total_pages(self) -> int:
        processed_users_len = len(self._processed_users_for_display)
        if not processed_users_len: return 1
        return math.ceil(processed_users_len / self.users_per_page) if processed_users_len > 0 else 1

    @rx.var
    def user_counts_by_level_var(self) -> Dict[str, int]: # برای استفاده در level_acquisition_view
        return self.user_counts_by_level

    @rx.var
    def users_in_channels_count_var(self) -> int: # برای کارت آمار
        return self.users_in_channels_count

    @rx.var
    def total_users_for_current_referral(self) -> int: # برای کارت آمار و محاسبات درصد
        return self.total_registered_users

    @rx.var
    def user_levels_pie_data(self) -> list[dict]:
        data = []
        # self.user_counts_by_level باید فقط شامل سطوح مجاز و شمارش آنها باشد.
        # این در _recalculate_stats_async تضمین شده است.
        if not self.user_counts_by_level:
            return [{"name": "سطحی برای نمایش یافت نشد", "value": 1, "fill": "var(--gray-8)"}]

        colors = ["var(--blue-8)", "var(--green-8)", "var(--purple-8)", "var(--red-8)", "var(--orange-8)", "var(--cyan-8)", "var(--yellow-8)"]
        color_index = 0
        for level_key, count in self.user_counts_by_level.items():
            if count > 0: # فقط سطوحی که کاربر دارند
                level_name = LEVEL_TRANSLATIONS.get(level_key, level_key.replace("level_", "سطح "))
                data.append({"name": level_name, "value": count, "fill": colors[color_index % len(colors)]})
                color_index += 1
        if not data:
             return [{"name": "کاربری در سطوح تعریف شده یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
        return data

    @rx.var
    def user_chat_state_pie_data(self) -> list[dict]:
        data = []
        if not self.user_counts_by_chat_state:
            return [{"name": "اطلاعات وضعیت موجود نیست", "value": 1, "fill": "var(--gray-8)"}]
        colors = ["var(--cyan-8)", "var(--teal-8)", "var(--mint-8)", "var(--sky-8)", "var(--indigo-8)", "var(--plum-8)", "var(--pink-8)"]
        color_index = 0
        for state_key, count in self.user_counts_by_chat_state.items():
            if count > 0:
                state_name = CHAT_STATE_TRANSLATIONS.get(state_key, state_key)
                data.append({"name": state_name, "value": count, "fill": colors[color_index % len(colors)]})
                color_index += 1
        if not data:
             return [{"name": "کاربری با وضعیت مشخص یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
        return data

    @rx.var
    def channel_members_chat_state_pie_data(self) -> list[dict]:
        data = []
        if not self.channel_members_counts_by_chat_state: # اگر دیکشنری خالی باشد
            return [{"name": "عضو کانالی یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
        colors = ["var(--lime-8)", "var(--grass-8)", "var(--jade-8)", "var(--blue-8)", "var(--crimson-8)", "var(--violet-8)", "var(--yellow-8)"]
        color_index = 0
        for state_key, count in self.channel_members_counts_by_chat_state.items():
            if count > 0:
                state_name = CHAT_STATE_TRANSLATIONS.get(state_key, state_key)
                data.append({"name": state_name, "value": count, "fill": colors[color_index % len(colors)]})
                color_index += 1
        if not data: # اگر پس از فیلتر count > 0 چیزی نماند
             return [{"name": "عضو کانالی با وضعیت مشخص یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
        return data

    # --------------------------------------------------------------------------
    # متدهای عملیاتی و Event Handler ها
    # --------------------------------------------------------------------------
    async def clear_all_users_data(self):
        """تمام داده‌های کاربران و آمارها را پاک می‌کند."""
        self.users = []
        self.current_page_number = 1
        self.current_user_for_edit = None
        await self._recalculate_stats_async() # بازنشانی آمارها

    def clear_current_user_for_edit(self):
        """کاربر انتخاب شده برای ویرایش را پاک می‌کند."""
        self.current_user_for_edit = None

    @rx.var
    def _processed_users_for_display(self) -> list[MongoUserDisplay]:
        """کاربران را بر اساس جستجو و مرتب‌سازی پردازش می‌کند."""
        users_to_process = list(self.users)
        if self.search_value:
            search_lower = self.search_value.lower()
            users_to_process = [
                user for user in users_to_process
                if search_lower in str(user.username or '').lower() or \
                   search_lower in str(user.national_id or '').lower() or \
                   search_lower in str(user.raw_chat_state or '').lower() or \
                   search_lower in str(user.chat_state_fa or '').lower() or \
                   search_lower in str(user.level or '').lower() or \
                   search_lower in str(user.created_at_str or '').lower() or \
                   (str(user.channel_count) if user.channel_count is not None else '').startswith(search_lower)
            ]
        if self.sort_value:
            def sort_key_func(user_item: MongoUserDisplay):
                val = getattr(user_item, self.sort_value, None)
                if self.sort_value == "created_at_ts":
                    return float(val) if val is not None else (float('-inf') if not self.sort_reverse else float('inf'))
                if self.sort_value == "channel_count":
                    return int(val) if val is not None else (float('-inf') if not self.sort_reverse else float('inf'))
                if self.sort_value == "level": # مرتب‌سازی بر اساس بخش عددی سطح
                    if val is None: return (float('-inf') if not self.sort_reverse else float('inf'))
                    if isinstance(val, str) and val.startswith("level_"):
                        try: return int(val.split("_")[-1])
                        except (ValueError, IndexError): return (float('-inf') if not self.sort_reverse else float('inf'))
                    return (float('-inf') if not self.sort_reverse else float('inf')) # برای مقادیر نامعتبر سطح
                return str(val or '').lower() # برای سایر فیلدهای رشته‌ای
            try:
                # استفاده از sort() روی لیست کپی شده برای جلوگیری از تغییر مستقیم self.users
                users_to_process.sort(key=sort_key_func, reverse=self.sort_reverse)
            except Exception as e:
                print(f"Sorting error in _processed_users_for_display (key={self.sort_value}): {e}")
        return users_to_process

    async def load_entries(self, active_referral: Optional[str] = None):
        """بارگذاری کاربران از دیتابیس بر اساس معرف فعال."""
        if active_referral is None:
            try:
                auth_state_instance = await self.get_state(AuthState)
                if auth_state_instance:
                    active_referral = auth_state_instance.current_logged_in_referral
            except Exception as e:
                print(f"Error getting AuthState/active_referral in load_entries: {e}")
                # ادامه با active_referral = None اگر AuthState قابل دسترسی نباشد
        if not active_referral:
            print("No active referral provided or found in load_entries. Clearing user data.")
            self.users = [] # پاک کردن کاربران اگر معرف معتبر نیست
            await self._recalculate_stats_async()
            return

        print(f"Attempting to load entries for referral: {active_referral}")
        mongo = get_mongo_client_instance()
        query_filter = {"referral": active_referral}
        mongo_users_cursor = mongo.get_all_users_cursor(query_filter=query_filter)

        loaded_users: list[MongoUserDisplay] = []
        for user_data_db in mongo_users_cursor:
            created_at_ts_val = user_data_db.get('created_at')
            created_at_jalali_str = "-"
            if isinstance(created_at_ts_val, (int, float)):
                try:
                    dt_utc_naive = datetime.datetime.utcfromtimestamp(created_at_ts_val)
                    dt_utc_aware = pytz.utc.localize(dt_utc_naive)
                    dt_tehran = dt_utc_aware.astimezone(TEHRAN_TZ)
                    j_datetime_tehran = jdatetime.datetime.fromgregorian(datetime=dt_tehran)
                    created_at_jalali_str = j_datetime_tehran.strftime('%Y/%m/%d %H:%M:%S')
                except (OSError, OverflowError, ValueError) as e:
                    created_at_jalali_str = f"تاریخ نامعتبر ({e})"

            updated_at_ts_val = user_data_db.get('updated_at')
            updated_at_jalali_str = "-" # اگر لازم دارید، اضافه کنید
            # if isinstance(updated_at_ts_val, (int, float)): ...

            raw_cs = user_data_db.get('chat_state')
            display_user = MongoUserDisplay(
                _id_str=str(user_data_db.get('_id')) if user_data_db.get('_id') else None,
                username=user_data_db.get('username'),
                national_id=user_data_db.get('national_id'),
                raw_chat_state=raw_cs,
                chat_state_fa=CHAT_STATE_TRANSLATIONS.get(raw_cs, CHAT_STATE_TRANSLATIONS["UNKNOWN_STATE"]), # مقدار پیش‌فرض
                created_at_str=created_at_jalali_str,
                created_at_ts=float(created_at_ts_val) if isinstance(created_at_ts_val, (int, float)) else None,
                channel_count=len(user_data_db.get('channels', [])) if isinstance(user_data_db.get('channels'), list) else 0,
                level=user_data_db.get('level') if isinstance(user_data_db.get('level'), str) else None,
            )
            if display_user._id_str:
                loaded_users.append(display_user)

        self.users = loaded_users
        self.current_page_number = 1 # بازنشانی به صفحه اول پس از بارگذاری
        await self._recalculate_stats_async() # محاسبه مجدد آمارها
        print(f"Finished loading. Loaded {len(self.users)} users for referral '{active_referral}'.")

    async def _recalculate_stats_async(self):
        """محاسبه مجدد تمام آمارها بر اساس لیست کاربران فعلی."""
        self.total_registered_users = len(self.users)

        users_in_channels_list: list[MongoUserDisplay] = []
        count_in_channels = 0
        for user in self.users:
            if user.channel_count > 0:
                count_in_channels += 1
                users_in_channels_list.append(user)
        self.users_in_channels_count = count_in_channels

        # محاسبه تعداد کاربران بر اساس سطح
        temp_level_counts: Dict[str, int] = {}
        allowed_levels_for_stats: List[str] = []
        auth_state_instance = None
        try:
            auth_state_instance = await self.get_state(AuthState)
            if auth_state_instance:
                allowed_levels_for_stats = auth_state_instance.allowed_levels_for_current_referral
            else:
                print("WARNING (_recalculate_stats_async): AuthState instance is None when calculating level counts.")
        except Exception as e:
            print(f"ERROR (_recalculate_stats_async): Failed to get AuthState for level counts: {e}")

        if allowed_levels_for_stats:
            for level_key in allowed_levels_for_stats:
                if level_key != NO_LEVEL_VALUE_INTERNAL:
                     temp_level_counts[level_key] = 0 # مقدار اولیه
            # شمارش کاربران فقط برای سطوح مجاز
            user_levels_present = [
                user.level for user in self.users
                if user.level and user.level in allowed_levels_for_stats and user.level != NO_LEVEL_VALUE_INTERNAL
            ]
            level_counts_from_users = Counter(user_levels_present)
            for level_key, count in level_counts_from_users.items():
                if level_key in temp_level_counts:
                    temp_level_counts[level_key] = count
        else:
            # اگر هیچ سطح مجازی تعریف نشده، می‌توانید همه سطوح موجود در کاربران را شمارش کنید
            # یا دیکشنری را خالی بگذارید.
            print("WARNING (_recalculate_stats_async): No allowed_levels. user_counts_by_level may be empty.")
        self.user_counts_by_level = temp_level_counts
        print(f"DEBUG (_recalculate_stats_async): Final user_counts_by_level = {self.user_counts_by_level}")

        # محاسبه تعداد کاربران بر اساس وضعیت دسترسی (chat_state)
        all_chat_states_raw = [user.raw_chat_state for user in self.users if user.raw_chat_state]
        self.user_counts_by_chat_state = dict(Counter(all_chat_states_raw))
        print(f"DEBUG (_recalculate_stats_async): user_counts_by_chat_state = {self.user_counts_by_chat_state}")

        # محاسبه تعداد اعضای کانال بر اساس وضعیت دسترسی (chat_state)
        channel_members_chat_states_raw = [user.raw_chat_state for user in users_in_channels_list if user.raw_chat_state]
        self.channel_members_counts_by_chat_state = dict(Counter(channel_members_chat_states_raw))
        print(f"DEBUG (_recalculate_stats_async): channel_members_counts_by_chat_state = {self.channel_members_counts_by_chat_state}")


    def sort_values(self, sort_by: str):
        """تنظیم ستون و جهت مرتب‌سازی."""
        if self.sort_value == sort_by:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_value = sort_by
            self.sort_reverse = False # پیش‌فرض صعودی برای ستون جدید
        self.current_page_number = 1 # بازنشانی به صفحه اول

    def toggle_sort(self):
        """تغییر جهت مرتب‌سازی."""
        self.sort_reverse = not self.sort_reverse
        self.current_page_number = 1

    def filter_values(self, search_term: str):
        """تنظیم مقدار جستجو."""
        self.search_value = search_term.strip() # حذف فضاهای خالی اضافی
        self.current_page_number = 1

    def set_current_user_for_edit(self, object_id_str: Optional[str]):
        """کاربر انتخاب شده برای ویرایش را تنظیم می‌کند."""
        if not object_id_str:
            self.current_user_for_edit = None
            return
        user_to_edit = next((u for u in self.users if u._id_str == object_id_str), None)
        if user_to_edit:
            # ایجاد یک کپی از آبجکت برای جلوگیری از تغییر مستقیم لیست اصلی
            self.current_user_for_edit = MongoUserDisplay(**user_to_edit.dict())
        else:
            self.current_user_for_edit = None
            print(f"--- WARNING: User {object_id_str} not found in self.users for edit. ---")

    async def add_customer_to_db(self, form_data: dict):
        """افزودن کاربر جدید به دیتابیس."""
        auth_state = await self.get_state(AuthState)
        if not auth_state:
            return rx.toast.error("خطا در دسترسی به وضعیت احراز هویت.", position="bottom-right")
        active_referral = auth_state.current_logged_in_referral
        if not active_referral:
            return rx.toast.error("کد معرف نامعتبر. ابتدا از سیستم خارج و دوباره وارد شوید.", position="bottom-right")

        allowed_levels = auth_state.allowed_levels_for_current_referral
        level_from_form = form_data.get("level")
        level_to_store: Optional[str] = None
        if level_from_form == NO_LEVEL_VALUE_INTERNAL or not level_from_form:
            level_to_store = None
        elif level_from_form in allowed_levels:
            level_to_store = level_from_form
        else: # سطح انتخاب شده مجاز نیست
            label = LEVEL_TRANSLATIONS.get(str(level_from_form), str(level_from_form))
            return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")

        username = str(form_data.get("username", "")).strip()
        if not username:
            return rx.toast.error("نام کاربری نمی‌تواند خالی باشد.", position="bottom-right")

        mongo = get_mongo_client_instance()
        if mongo.db.users.find_one({"username": username, "referral": active_referral}):
            return rx.toast.error(f"کاربری با نام کاربری '{username}' قبلا برای این معرف ثبت شده.", position="bottom-right")

        new_doc = {
            "username": username,
            "national_id": str(form_data.get("national_id", "")).strip() or None,
            "chat_state": form_data.get("chat_state"), # باید از CHAT_STATE_TRANSLATIONS باشد
            "level": level_to_store,
            "created_at": int(datetime.datetime.now(pytz.utc).timestamp()),
            "updated_at": int(datetime.datetime.now(pytz.utc).timestamp()),
            "channels": [], "referral": active_referral,
            "user_id": mongo.db.users.count_documents({}) + 6000000000 + random.randint(1,10000) # برای منحصر به فرد بودن بیشتر
        }
        try:
            result = mongo.insert_user(new_doc)
            if result.inserted_id:
                await self.load_entries(active_referral=active_referral) # بارگذاری مجدد داده‌ها
                return rx.toast.success(f"کاربر {new_doc.get('username')} افزوده شد.", position="bottom-right")
        except Exception as e:
            print(f"Error inserting user to DB: {e}")
            return rx.toast.error(f"خطا در افزودن کاربر: {e}", position="bottom-right")
        return rx.toast.error("خطای نامشخص در افزودن کاربر.", position="bottom-right")


    async def update_customer_to_db(self, form_data: dict):
        """به‌روزرسانی اطلاعات کاربر موجود در دیتابیس."""
        auth_state = await self.get_state(AuthState)
        if not auth_state:
            return rx.toast.error("خطا در دسترسی به وضعیت احراز هویت.", position="bottom-right")
        if not self.current_user_for_edit or not self.current_user_for_edit._id_str:
            return rx.toast.error("کاربری برای ویرایش انتخاب نشده است.", position="bottom-right")

        obj_id_str = self.current_user_for_edit._id_str
        original_data = self.current_user_for_edit
        active_referral = auth_state.current_logged_in_referral
        allowed_levels = auth_state.allowed_levels_for_current_referral

        set_payload: Dict[str, Any] = {}
        unset_payload: Dict[str, Any] = {} # برای حذف فیلدها (مثل level)
        changed = False

        new_username = str(form_data.get("username", "")).strip()
        if new_username and new_username != original_data.username:
            mongo = get_mongo_client_instance()
            existing_user_with_new_username = mongo.db.users.find_one({
                "username": new_username, "referral": active_referral,
                "_id": {"$ne": ObjectId(obj_id_str)}
            })
            if existing_user_with_new_username:
                return rx.toast.error(f"نام کاربری '{new_username}' قبلاً توسط کاربر دیگری استفاده شده است.", position="bottom-right")
            set_payload["username"] = new_username; changed = True
        elif not new_username and original_data.username:
             return rx.toast.error("نام کاربری نمی‌تواند خالی باشد.", position="bottom-right")

        new_national_id = str(form_data.get("national_id", "")).strip()
        if new_national_id != (original_data.national_id or ""):
            set_payload["national_id"] = new_national_id or None; changed = True

        if (val := form_data.get("chat_state")) is not None and val != original_data.raw_chat_state:
            set_payload["chat_state"] = val; changed = True

        new_level = form_data.get("level")
        # مقایسه دقیق‌تر برای None و رشته خالی
        original_level = original_data.level if original_data.level else None # تبدیل رشته خالی به None برای مقایسه
        processed_new_level = new_level if new_level and new_level != NO_LEVEL_VALUE_INTERNAL else None

        if processed_new_level != original_level:
            if processed_new_level is None: # کاربر می‌خواهد سطح را حذف کند
                if original_data.level is not None: # فقط اگر قبلاً سطحی داشته
                    unset_payload["level"] = ""; changed = True
            elif processed_new_level in allowed_levels:
                set_payload["level"] = processed_new_level; changed = True
            else:
                label = LEVEL_TRANSLATIONS.get(str(new_level), str(new_level))
                return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")

        if not changed:
            self.clear_current_user_for_edit() # پاک کردن فرم ویرایش
            return rx.toast.info("تغییری برای اعمال وجود ندارد.", position="bottom-right")

        set_payload["updated_at"] = int(datetime.datetime.now(pytz.utc).timestamp())
        mongo = get_mongo_client_instance()
        user_doc_from_db = mongo.get_user_by_object_id(obj_id_str)
        if not user_doc_from_db or user_doc_from_db.get("referral") != active_referral:
            self.clear_current_user_for_edit()
            return rx.toast.error("شما اجازه ویرایش این کاربر را ندارید یا کاربر یافت نشد.", position="bottom-right")

        ops: Dict[str, Any] = {}
        if set_payload: ops['$set'] = set_payload
        if unset_payload: ops['$unset'] = unset_payload

        if ops:
            try:
                update_result = mongo.db.users.update_one({'_id': ObjectId(obj_id_str)}, ops)
                if update_result.matched_count == 0:
                    self.clear_current_user_for_edit()
                    return rx.toast.error("کاربر برای به‌روزرسانی یافت نشد (ممکن است همزمان حذف شده باشد).", position="bottom-right")
            except Exception as e:
                self.clear_current_user_for_edit()
                return rx.toast.error(f"خطا در پایگاه داده هنگام به‌روزرسانی: {e}", position="bottom-right")

        await self.load_entries(active_referral=active_referral)
        self.clear_current_user_for_edit()
        display_username_after_update = set_payload.get("username", original_data.username or "کاربر")
        return rx.toast.success(f"کاربر {display_username_after_update} به‌روز شد.", position="bottom-right")


    async def delete_customer(self, object_id_str: Optional[str]):
        """حذف کاربر از دیتابیس."""
        if not object_id_str:
            return rx.toast.error("شناسه کاربر نامعتبر است.", position="bottom-right")
        auth_state = await self.get_state(AuthState)
        if not auth_state:
            return rx.toast.error("خطا در دسترسی به وضعیت احراز هویت.", position="bottom-right")
        active_referral = auth_state.current_logged_in_referral

        mongo = get_mongo_client_instance()
        user_doc = mongo.get_user_by_object_id(object_id_str)
        if not user_doc:
            return rx.toast.error("کاربر یافت نشد.", position="bottom-right")
        if user_doc.get("referral") != active_referral: # بررسی مالکیت معرف
            return rx.toast.error("شما اجازه حذف این کاربر را ندارید.", position="bottom-right")
        try:
            result = mongo.delete_user_by_object_id(object_id_str)
            if result and result.deleted_count > 0:
                await self.load_entries(active_referral=active_referral)
                if self.current_user_for_edit and self.current_user_for_edit._id_str == object_id_str:
                    self.clear_current_user_for_edit() # پاک کردن از فرم ویرایش اگر همان کاربر بود
                return rx.toast.success(f"کاربر {user_doc.get('username', object_id_str)} حذف شد.", position="bottom-right")
            else: # اگر deleted_count صفر بود
                return rx.toast.warn("کاربر یافت نشد یا قبلاً حذف شده بود.", position="bottom-right")
        except Exception as e:
            print(f"Error deleting user from DB: {e}")
            return rx.toast.error(f"خطا در حذف کاربر: {e}", position="bottom-right")

    # --- متدهای صفحه‌بندی ---
    def next_page_handler(self):
        if self.current_page_number < self.total_pages:
            self.current_page_number += 1

    def prev_page_handler(self):
        if self.current_page_number > 1:
            self.current_page_number -= 1

    def first_page_handler(self):
        self.current_page_number = 1

    def last_page_handler(self):
        if self.total_pages > 0:
            self.current_page_number = self.total_pages
        else: # اگر هیچ صفحه‌ای وجود ندارد (مثلاً نتایج جستجو خالی است)
            self.current_page_number = 1

# تابع کمکی (خارج از کلاس State اگر لازم باشد، یا به عنوان متد استاتیک)
def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    """محاسبه درصد تغییرات."""
    if prev_value == 0:
        return float("inf") if value > 0 else 0.0 # یا ۱۰۰٪ اگر value > 0
    return round(((value - prev_value) / prev_value) * 100, 2)