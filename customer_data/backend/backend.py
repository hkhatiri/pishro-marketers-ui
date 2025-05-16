# customer_data/backend/backend.py
# ... (سایر import ها و تعاریف اولیه مانند قبل) ...
import datetime
import math
from typing import List, Optional, Union, TypedDict, Dict, Tuple, Any
from collections import Counter

import reflex as rx
from bson import ObjectId
import jdatetime
import pytz

try:
    from .mongo import Mongo, ChatState
    from .auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL, REFERRAL_LEVEL_CONFIG
except ImportError:
    from mongo import Mongo, ChatState # type: ignore
    try:
        from auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL, REFERRAL_LEVEL_CONFIG # type: ignore
    except ImportError:
        class AuthState(rx.State): # type: ignore
            current_logged_in_referral: Optional[str] = "test_referral"
            is_logged_in: bool = True
            @rx.var
            def token_is_valid(self) -> bool: return self.is_logged_in
            @rx.var
            def allowed_levels_for_current_referral(self) -> List[str]: return REFERRAL_LEVEL_CONFIG.get(self.current_logged_in_referral, []) if self.current_logged_in_referral else [] # type: ignore
            @rx.var
            def level_options_for_dropdown(self) -> List[Tuple[str,str]]: return []

        LEVEL_TRANSLATIONS: Dict[str, str] = {} # type: ignore
        NO_LEVEL_VALUE_INTERNAL: str = "_NO_LEVEL_" # type: ignore
        REFERRAL_LEVEL_CONFIG: Dict[str, List[str]] = {} # type: ignore


CHAT_STATE_TRANSLATIONS = {
    "HasAccess": "دسترسی دارد", "HasManualAccess": "دسترسی دستی دارد",
    "INITED": "کاربر جدید", "BLOCKED": "مسدود",
    "WaitForNationalId": "در انتظار کدملی", "WaitForOTP": "در انتظار کد",
    "WaitForCaptcha": "در انتظار کپچا", "LoggedIn": "لاگین شده",
}

class MongoUserDisplay(TypedDict):
    _id_str: Optional[str]; username: Optional[str]; national_id: Optional[str]
    raw_chat_state: Optional[str]; chat_state_fa: Optional[str]
    created_at_str: Optional[str]; updated_at_str: Optional[str]
    created_at_ts: Optional[float] 
    channel_count: int; level: Optional[str]

class MonthValues(rx.Base):
    num_customers: int = 0

_mongo_client_global_instance: Optional[Mongo] = None
YOUR_MONGO_DB_NAME = "marketersbot"
TEHRAN_TZ = pytz.timezone('Asia/Tehran')

def get_mongo_client_instance() -> Mongo:
    global _mongo_client_global_instance
    if _mongo_client_global_instance is None:
        _mongo_client_global_instance = Mongo(mongo_db_name=YOUR_MONGO_DB_NAME)
    return _mongo_client_global_instance

class State(rx.State):
    users: list[MongoUserDisplay] = []
    current_user_for_edit: Optional[MongoUserDisplay] = None
    sort_value: str = "created_at_ts" 
    sort_reverse: bool = True 
    search_value: str = ""; current_page_number: int = 1
    users_per_page: int = 10
    total_registered_users: int = 0
    user_counts_by_level: Dict[str, int] = {}
    users_in_channels_count: int = 0
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()

    async def clear_all_users_data(self):
        self.users = []; self.current_page_number = 1
        self.current_user_for_edit = None; await self._recalculate_stats_async()

    def clear_current_user_for_edit(self): self.current_user_for_edit = None

    @rx.var
    def _processed_users_for_display(self) -> list[MongoUserDisplay]:
        users_to_process = list(self.users)
        if self.search_value:
            search_lower = self.search_value.lower()
            users_to_process = [
                user for user in users_to_process
                if search_lower in str(user.get('username', '')).lower() or \
                   search_lower in str(user.get('national_id', '')).lower() or \
                   search_lower in str(user.get('raw_chat_state', '')).lower() or \
                   search_lower in str(user.get('chat_state_fa', '')).lower() or \
                   search_lower in str(user.get('level', '')).lower() or \
                   search_lower in str(user.get('created_at_str', '')).lower() or
                   search_lower in str(user.get('channel_count', '')).lower()
            ]

        if self.sort_value:
            def sort_key_func(user_item: MongoUserDisplay) -> Union[float, int, str]: # تایپ بازگشتی
                val = user_item.get(self.sort_value) # type: ignore
                
                # مقادیر پیش‌فرض برای None ها برای اطمینان از مرتب‌سازی صحیح
                # برای مرتب‌سازی صعودی، None ها باید کوچکترین مقدار باشند
                # برای مرتب‌سازی نزولی، None ها باید بزرگترین مقدار باشند (یا کوچکترین اگر reverse=True)
                # برای سادگی، None ها را به مقداری تبدیل می‌کنیم که همیشه در یک سمت قرار گیرند.
                
                if self.sort_value == "created_at_ts":
                    if val is None: return float('-inf') if not self.sort_reverse else float('inf')
                    try: return float(val)
                    except (ValueError, TypeError): return float('-inf') if not self.sort_reverse else float('inf')
                
                elif self.sort_value == "channel_count":
                    if val is None: return float('-inf') if not self.sort_reverse else float('inf')
                    try: return int(val) # کانال همیشه int است
                    except (ValueError, TypeError): return float('-inf') if not self.sort_reverse else float('inf')

                elif self.sort_value == "level":
                    # برای level، بخش عددی را استخراج می‌کنیم و به عنوان عدد مرتب می‌کنیم
                    # None ها یا مقادیر نامعتبر باید به یک مقدار عددی پیش‌فرض تبدیل شوند
                    if val is None: return float('-inf') if not self.sort_reverse else float('inf')
                    if isinstance(val, str) and val.startswith("level_"):
                        try:
                            return int(val.split("_")[-1])
                        except (ValueError, IndexError, TypeError):
                            return float('-inf') if not self.sort_reverse else float('inf') 
                    return float('-inf') if not self.sort_reverse else float('inf') # اگر فرمت نامعتبر بود

                # برای سایر فیلدها که انتظار می‌رود رشته باشند
                else: # username, national_id, raw_chat_state, created_at_str
                    if val is None: return "" if not self.sort_reverse else "~" # "~" بزرگتر از اکثر کاراکترهاست
                    return str(val).lower()
            
            try:
                users_to_process = sorted(users_to_process, key=sort_key_func, reverse=self.sort_reverse)
            except TypeError as e:
                print(f"!!! Sorting TypeError (key={self.sort_value}, reverse={self.sort_reverse}): {e}")
                # در صورت بروز خطای پیش‌بینی نشده، لیست مرتب‌نشده را برگردان
                # این باید از بروز خطا در UI جلوگیری کند، اما باید علت اصلی خطا بررسی شود.
                pass 
        return users_to_process
        
    # ... (بقیه متدهای State مانند paginated_users, total_pages, load_entries, و غیره مانند قبل)
    @rx.var
    def paginated_users(self) -> list[MongoUserDisplay]:
        start_index = (self.current_page_number - 1) * self.users_per_page
        end_index = start_index + self.users_per_page
        return self._processed_users_for_display[start_index:end_index]

    @rx.var
    def total_pages(self) -> int:
        if not self._processed_users_for_display: return 1
        return math.ceil(len(self._processed_users_for_display) / self.users_per_page) if self._processed_users_for_display else 1

    @rx.var
    def user_counts_by_level_var(self) -> Dict[str, int]: return self.user_counts_by_level
        
    @rx.var
    def users_in_channels_count_var(self) -> int: return self.users_in_channels_count

    @rx.var
    def customers_change(self) -> float:
        return _get_percentage_change(self.total_registered_users, self.previous_month_values.num_customers)

    async def load_entries(self, active_referral: Optional[str] = None):
        if active_referral is None:
            try:
                auth_state_instance = await self.get_state(AuthState) # type: ignore
                active_referral = auth_state_instance.current_logged_in_referral
            except Exception as e:
                print(f"Error getting active_referral from AuthState in load_entries: {e}")
                active_referral = None
        if not active_referral:
            self.users = []; await self._recalculate_stats_async(); return

        mongo = get_mongo_client_instance()
        query_filter = {"referral": active_referral}
        mongo_users_cursor = mongo.get_all_users_cursor(query_filter) # مرتب‌سازی در _processed_users_for_display
        
        loaded_users = []
        for user_data in mongo_users_cursor: # type: ignore
            created_at_ts_val = user_data.get('created_at')
            updated_at_ts_val = user_data.get('updated_at')
            created_at_jalali_str = "نامشخص"
            if isinstance(created_at_ts_val, (int, float)):
                try:
                    dt_utc_naive = datetime.datetime.utcfromtimestamp(created_at_ts_val)
                    dt_utc_aware = pytz.utc.localize(dt_utc_naive)
                    dt_tehran = dt_utc_aware.astimezone(TEHRAN_TZ)
                    j_datetime_tehran = jdatetime.datetime.fromgregorian(datetime=dt_tehran)
                    created_at_jalali_str = j_datetime_tehran.strftime('%Y/%m/%d ساعت %H:%M:%S')
                except Exception: created_at_jalali_str = str(datetime.datetime.fromtimestamp(created_at_ts_val)) 
            updated_at_jalali_str = "نامشخص"
            if isinstance(updated_at_ts_val, (int, float)):
                try:
                    dt_utc_naive_up = datetime.datetime.utcfromtimestamp(updated_at_ts_val)
                    dt_utc_aware_up = pytz.utc.localize(dt_utc_naive_up)
                    dt_tehran_up = dt_utc_aware_up.astimezone(TEHRAN_TZ)
                    j_datetime_tehran_up = jdatetime.datetime.fromgregorian(datetime=dt_tehran_up)
                    updated_at_jalali_str = j_datetime_tehran_up.strftime('%Y/%m/%d ساعت %H:%M:%S')
                except Exception: updated_at_jalali_str = str(datetime.datetime.fromtimestamp(updated_at_ts_val)) 

            display_user: MongoUserDisplay = {
                '_id_str': str(user_data.get('_id')) if user_data.get('_id') else None, 
                'username': user_data.get('username'),
                'national_id': user_data.get('national_id'), 
                'raw_chat_state': user_data.get('chat_state'),
                'created_at_str': created_at_jalali_str,
                'updated_at_str': updated_at_jalali_str,
                'created_at_ts': float(created_at_ts_val) if isinstance(created_at_ts_val, (int, float)) else None,
                'channel_count': len(user_data.get('channels', [])) if isinstance(user_data.get('channels'), list) else 0,
                'chat_state_fa': CHAT_STATE_TRANSLATIONS.get(user_data.get('chat_state', ""), user_data.get('chat_state', "") or "نامشخص"),
                'level': user_data.get('level') if isinstance(user_data.get('level'), str) else None,
            }
            if display_user['_id_str'] is None: continue
            loaded_users.append(display_user)
        self.users = loaded_users; self.current_page_number = 1
        await self._recalculate_stats_async()

    async def _recalculate_stats_async(self):
        self.total_registered_users = len(self.users)
        self.current_month_values = MonthValues(num_customers=self.total_registered_users)
        count_in_channels = 0
        for user in self.users:
            if user.get('channel_count', 0) > 0: count_in_channels += 1
        self.users_in_channels_count = count_in_channels
        auth_state_instance = await self.get_state(AuthState) # type: ignore
        allowed_levels_for_stats: List[str] = []
        if auth_state_instance and hasattr(auth_state_instance, 'allowed_levels_for_current_referral'):
            allowed_levels_for_stats = auth_state_instance.allowed_levels_for_current_referral
        temp_counts: Dict[str, int] = {}
        if allowed_levels_for_stats:
            level_values_in_users = [user.get('level') for user in self.users if user.get('level') is not None]
            level_counts_from_users = Counter(lvl for lvl in level_values_in_users if lvl in allowed_levels_for_stats)
            for level_key in allowed_levels_for_stats:
                temp_counts[level_key] = level_counts_from_users.get(level_key, 0)
        self.user_counts_by_level = temp_counts

    def sort_values(self, sort_by: str):
        if self.sort_value == sort_by: self.sort_reverse = not self.sort_reverse
        else: self.sort_value = sort_by; self.sort_reverse = False
        self.current_page_number = 1

    def toggle_sort(self): self.sort_reverse = not self.sort_reverse; self.current_page_number = 1
    def filter_values(self, search_term: str): self.search_value = search_term; self.current_page_number = 1

    def set_current_user_for_edit(self, object_id_str: Optional[str]):
        if not object_id_str: self.current_user_for_edit = None; return
        user = next((u for u in self.users if u.get('_id_str') == object_id_str), None)
        self.current_user_for_edit = user.copy() if user else None # type: ignore
        if not user: print(f"--- WARNING: User {object_id_str} not found for edit. ---")

    async def add_customer_to_db(self, form_data: dict):
        auth_state = await self.get_state(AuthState) # type: ignore
        active_referral = auth_state.current_logged_in_referral
        if not active_referral: return rx.toast.error("کد معرف نامعتبر.", position="bottom-right")
        allowed_levels = auth_state.allowed_levels_for_current_referral
        level_from_form = form_data.get("level")
        level_to_store: Optional[str] = None
        if level_from_form == NO_LEVEL_VALUE_INTERNAL: level_to_store = None
        elif level_from_form and level_from_form in allowed_levels: level_to_store = level_from_form
        elif not level_from_form and allowed_levels: level_to_store = allowed_levels[0]
        elif level_from_form:
            label = LEVEL_TRANSLATIONS.get(level_from_form, level_from_form)
            return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")
        mongo = get_mongo_client_instance()
        new_doc = {
            "username": form_data.get("username"), "national_id": form_data.get("national_id"),
            "chat_state": form_data.get("chat_state"), "level": level_to_store,
            "created_at": int(datetime.datetime.now().timestamp()), "updated_at": int(datetime.datetime.now().timestamp()),
            "channels": [], "referral": active_referral, 
            "user_id": mongo.db.users.count_documents({}) + 6000000000
        }
        if mongo.db.users.find_one({"username": new_doc["username"], "referral": active_referral}):
            return rx.toast.error(f"کاربری با نام کاربری '{new_doc['username']}' قبلا برای این معرف ثبت شده.", position="bottom-right")
        result = mongo.insert_user(new_doc)
        if result.inserted_id: 
            await self.load_entries(active_referral=active_referral)
            return rx.toast.success(f"کاربر {new_doc.get('username', 'جدید')} افزوده شد.", position="bottom-right")
        return rx.toast.error("خطا در افزودن کاربر.", position="bottom-right")

    async def update_customer_to_db(self, form_data: dict):
        auth_state = await self.get_state(AuthState) # type: ignore
        if not self.current_user_for_edit or not self.current_user_for_edit.get("_id_str"):
            return rx.toast.error("کاربری برای ویرایش انتخاب نشده است.", position="bottom-right")
        obj_id_str = self.current_user_for_edit["_id_str"]
        original_data = self.current_user_for_edit
        allowed_levels = auth_state.allowed_levels_for_current_referral
        set_payload: Dict[str, Any] = {}; unset_payload: Dict[str, Any] = {}; changed = False
        if (val := form_data.get("username")) is not None and val != original_data.get("username"): set_payload["username"] = val; changed = True
        if "national_id" in form_data:
            val = form_data.get("national_id")
            if val != original_data.get("national_id"): set_payload["national_id"] = val if val else ""; changed = True
        if (val := form_data.get("chat_state")) is not None and val != original_data.get("raw_chat_state"): set_payload["chat_state"] = val; changed = True
        if (val := form_data.get("level")) is not None and val != original_data.get("level"):
            if val == NO_LEVEL_VALUE_INTERNAL:
                if original_data.get("level") is not None: unset_payload["level"] = ""; changed = True
            elif val in allowed_levels: set_payload["level"] = val; changed = True
            else: 
                label = LEVEL_TRANSLATIONS.get(val, val)
                return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")
        if not changed: self.clear_current_user_for_edit(); return rx.toast.info("تغییری برای اعمال وجود ندارد.", position="bottom-right")
        set_payload["updated_at"] = int(datetime.datetime.now().timestamp())
        mongo = get_mongo_client_instance()
        active_referral = auth_state.current_logged_in_referral
        user_doc_from_db = mongo.get_user_by_object_id(obj_id_str) # type: ignore
        if not user_doc_from_db or user_doc_from_db.get("referral") != active_referral:
            return rx.toast.error("شما اجازه ویرایش این کاربر را ندارید.", position="bottom-right")
        ops: Dict[str, Any] = {}
        if set_payload: ops['$set'] = set_payload
        if unset_payload: ops['$unset'] = unset_payload
        if ops: 
            try: mongo.db.users.update_one({'_id': ObjectId(obj_id_str)}, ops) # type: ignore
            except Exception as e: return rx.toast.error(f"خطا در پایگاه داده: {e}", position="bottom-right")
        await self.load_entries(active_referral=active_referral)
        self.clear_current_user_for_edit()
        display_username = set_payload.get("username", original_data.get("username", ""))
        return rx.toast.success(f"کاربر {display_username} به‌روز شد.", position="bottom-right")

    async def delete_customer(self, object_id_str: Optional[str]):
        if not object_id_str: return rx.toast.error("شناسه کاربر نامعتبر است.", position="bottom-right")
        auth_state = await self.get_state(AuthState) # type: ignore
        active_referral = auth_state.current_logged_in_referral
        mongo = get_mongo_client_instance()
        user_doc = mongo.get_user_by_object_id(object_id_str) # type: ignore
        if not user_doc: return rx.toast.error("کاربر یافت نشد.", position="bottom-right")
        if user_doc.get("referral") != active_referral: return rx.toast.error("شما اجازه حذف این کاربر را ندارید.", position="bottom-right")
        result = mongo.delete_user_by_object_id(object_id_str) # type: ignore
        if result.deleted_count > 0:
            await self.load_entries(active_referral=active_referral)
            if self.current_user_for_edit and self.current_user_for_edit.get("_id_str") == object_id_str:
                self.clear_current_user_for_edit()
            return rx.toast.success(f"کاربر {user_doc.get('username', object_id_str)} حذف شد.", position="bottom-right")
        return rx.toast.error("خطا در حذف کاربر.", position="bottom-right")

    @rx.var
    def total_users_for_current_referral(self) -> int: return self.total_registered_users
    def next_page_handler(self): self.current_page_number = min(self.current_page_number + 1, self.total_pages)
    def prev_page_handler(self): self.current_page_number = max(1, self.current_page_number - 1)
    def first_page_handler(self): self.current_page_number = 1
    def last_page_handler(self): self.current_page_number = self.total_pages


def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    if prev_value == 0: return float("inf") if value > 0 else 0.0
    return round(((value - prev_value) / prev_value) * 100, 2)