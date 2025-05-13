import reflex as rx
from typing import List, Dict, Any, Optional
from ..models.bot_user import BotUser
# مسیردهی به فایل‌های کپی شده‌ی شما
from ..remote_db.mongo import Mongo
from ..remote_db import settings as remote_settings
from .auth_state import AuthState
import datetime

USERS_COLLECTION_NAME = "users"

class AdminState(rx.State):
    bot_users: List[BotUser] = []
    is_loading: bool = False
    search_term: str = ""
    current_page: int = 1
    items_per_page: int = 20

    show_edit_dialog: bool = False
    editing_user: Optional[BotUser] = None
    # برای فرم ویرایش، مطمئن شوید همه فیلدهای BotUser که می‌خواهید ویرایش شوند اینجا هستند
    edit_form_data: Dict[str, Any] = {}

    _mongo_client: Optional[Mongo] = None
    auth_state: AuthState = AuthState() # برای دسترسی به اطلاعات ادمین

    def _get_mongo_instance(self) -> Mongo:
        if self._mongo_client is None:
            mongo_db_name = remote_settings.SETTINGS['marketers']['MONGO_DB']
            self._mongo_client = Mongo(mongo_db=mongo_db_name)
        return self._mongo_client

    def _map_mongo_to_botuser(self, mongo_data: Dict[str, Any]) -> Optional[BotUser]:
        try:
            # اطمینان از وجود user_id
            if mongo_data.get("user_id") is None:
                print(f"Skipping record due to missing user_id: {mongo_data}")
                return None

            # تبدیل تایم‌استمپ‌ها به int اگر از نوع دیگری هستند و وجود دارند
            created_at = mongo_data.get("created_at")
            updated_at = mongo_data.get("updated_at")
            level_checked_at = mongo_data.get("level_checked_at")

            return BotUser(
                user_id=int(mongo_data["user_id"]), # user_id باید int باشد
                national_id=str(mongo_data.get("national_id")) if mongo_data.get("national_id") is not None else None,
                username=mongo_data.get("username"),
                chat_state=mongo_data.get("chat_state"),
                chat_id=int(mongo_data.get("chat_id")) if mongo_data.get("chat_id") is not None else None,
                updated_at=int(updated_at) if isinstance(updated_at, (int, float)) else None,
                created_at=int(created_at) if isinstance(created_at, (int, float)) else None,
                referral=mongo_data.get("referral"),
                agent_code=mongo_data.get("agent_code"),
                trial_noticed=mongo_data.get("trial_noticed") if isinstance(mongo_data.get("trial_noticed"), bool) else None,
                trial_ended=mongo_data.get("trial_ended") if isinstance(mongo_data.get("trial_ended"), bool) else None,
                level=mongo_data.get("level"),
                level_checked_at=int(level_checked_at) if isinstance(level_checked_at, (int, float)) else None,
                channels=mongo_data.get("channels") if isinstance(mongo_data.get("channels"), list) else None,
                registration_wizard_step=int(mongo_data.get("registration_wizard_step")) if mongo_data.get("registration_wizard_step") is not None else None,
                capital_limit=mongo_data.get("capital_limit"),
            )
        except Exception as e:
            print(f"Error mapping MongoDB data for user_id {mongo_data.get('user_id')}: {e}")
            print(f"Problematic data: {mongo_data}")
            return None

    @rx.var
    def filtered_bot_users(self) -> List[BotUser]:
        # ... (بدون تغییر نسبت به پاسخ قبلی)
        users = self.bot_users
        if self.search_term:
            term = self.search_term.lower()
            users = [
                u for u in users if
                (u.username and term in u.username.lower()) or
                (u.national_id and term in u.national_id) or
                (str(u.user_id) and term in str(u.user_id)) or # جستجو بر اساس user_id
                (u.referral and term in u.referral.lower()) or
                (u.agent_code and term in u.agent_code.lower()) or
                (u.level and term in u.level.lower())
            ]
        return users

    @rx.var
    def paginated_users(self) -> List[BotUser]:
        # ... (بدون تغییر)
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.filtered_bot_users[start_index:end_index]


    @rx.var
    def total_pages(self) -> int:
        # ... (بدون تغییر)
        import math
        if not self.filtered_bot_users or self.items_per_page <= 0:
            return 1 # حداقل یک صفحه وجود دارد حتی اگر خالی باشد
        return math.ceil(len(self.filtered_bot_users) / self.items_per_page)

    def go_to_page(self, page_num: str): # تغییر به str برای ورودی از UI
        try:
            page = int(page_num)
            if 1 <= page <= self.total_pages:
                self.current_page = page
        except ValueError:
            pass # اگر ورودی عدد معتبر نباشد، کاری نکن

    def next_page(self):
        # ... (بدون تغییر)
        if self.current_page < self.total_pages:
            self.current_page +=1

    def prev_page(self):
        # ... (بدون تغییر)
        if self.current_page > 1:
            self.current_page -= 1

    async def load_bot_users(self):
        if not self.auth_state.is_authenticated:
            return rx.redirect("/login")

        self.is_loading = True
        yield

        mongo = self._get_mongo_instance()
        query_filter = {}

        if not self.auth_state.is_logged_in_super_admin:
            if self.auth_state.logged_in_admin_referral_type:
                query_filter["referral"] = self.auth_state.logged_in_admin_referral_type
            else:
                self.bot_users = []
                self.is_loading = False
                return

        try:
            mongo_users_cursor = mongo.db[USERS_COLLECTION_NAME].find(query_filter)
            all_mongo_users_data = list(mongo_users_cursor) # خواندن همه داده‌ها
        except Exception as e:
            self.is_loading = False
            yield rx.toast.error(f"خطا در خواندن از دیتابیس: {str(e)}")
            return

        temp_users = []
        for user_data in all_mongo_users_data:
            mapped_user = self._map_mongo_to_botuser(user_data)
            if mapped_user:
                temp_users.append(mapped_user)

        self.bot_users = temp_users
        self.current_page = 1
        self.is_loading = False
        yield

    def start_edit_user(self, user: BotUser):
        self.editing_user = user
        self.edit_form_data = {
            "national_id": user.national_id or "",
            "username": user.username or "",
            "chat_state": user.chat_state or "", # اطمینان از اینکه None به "" تبدیل می‌شود
            "level": user.level or "",
            "referral": user.referral or "",
            "agent_code": user.agent_code or "",
            "trial_noticed": user.trial_noticed if user.trial_noticed is not None else False, # پیش‌فرض برای checkbox
            "trial_ended": user.trial_ended if user.trial_ended is not None else False, # پیش‌فرض برای checkbox
            "capital_limit": user.capital_limit or "",
        }
        self.show_edit_dialog = True

    def handle_edit_form_change(self, field_name: str, value: Any):
        # برای checkbox ها، مقدار value مستقیما boolean است
        if isinstance(value, bool) and field_name in ["trial_noticed", "trial_ended"]:
             self.edit_form_data[field_name] = value
        else:
            self.edit_form_data[field_name] = str(value) # تبدیل به رشته برای input ها

    def save_user_changes(self):
        if self.editing_user is None:
            return

        mongo = self._get_mongo_instance()
        user_id_to_update = self.editing_user.user_id

        updates_to_apply = {}
        for key, value in self.edit_form_data.items():
            # تبدیل مقادیر خالی رشته به None تا در دیتابیس ذخیره نشوند اگر فیلد optional است
            # یا تبدیل به نوع داده مناسب قبل از ذخیره
            if isinstance(value, str) and value == "":
                updates_to_apply[key] = None # یا حذف کلید اگر می‌خواهید فیلد unset شود
            elif key in ["trial_noticed", "trial_ended"]: # اینها boolean هستند
                updates_to_apply[key] = bool(value)
            elif key in ["user_id", "chat_id", "registration_wizard_step"] and value is not None and str(value).isdigit():
                 updates_to_apply[key] = int(value)
            else:
                updates_to_apply[key] = value

        if not updates_to_apply:
            self.show_edit_dialog = False
            return rx.toast.info("هیچ تغییری برای ذخیره وجود ندارد.")

        updates_to_apply["updated_at"] = int(datetime.datetime.now().timestamp())

        if not self.auth_state.is_logged_in_super_admin and "referral" in updates_to_apply:
            if updates_to_apply["referral"] != self.auth_state.logged_in_admin_referral_type:
                return rx.toast.error("شما اجازه تغییر referral به این مقدار را ندارید.")

        try:
            mongo.db[USERS_COLLECTION_NAME].update_one(
                {'user_id': user_id_to_update},
                {'$set': updates_to_apply}
            )

            # آپدیت کاربر در لیست محلی
            for i, u in enumerate(self.bot_users):
                if u.user_id == user_id_to_update:
                    # ایجاد یک دیکشنری از کاربر فعلی و آپدیت آن با مقادیر فرم
                    updated_user_data = u.dict()
                    for k, v in updates_to_apply.items():
                        if hasattr(BotUser, k): # فقط فیلدهایی که در مدل BotUser هستند
                            updated_user_data[k] = v
                    self.bot_users[i] = self._map_mongo_to_botuser(updated_user_data) # دوباره مپ کن تا نوع‌ها درست باشند
                    break

            self.show_edit_dialog = False
            self.editing_user = None
            return rx.toast.success("اطلاعات کاربر با موفقیت به‌روز شد.")
        except Exception as e:
            return rx.toast.error(f"خطا در ذخیره تغییرات: {str(e)}")

    def delete_bot_user(self, user_id: int):
        if not self.auth_state.is_logged_in_super_admin:
            user_to_delete = next((u for u in self.bot_users if u.user_id == user_id), None)
            if not user_to_delete or user_to_delete.referral != self.auth_state.logged_in_admin_referral_type:
                return rx.toast.error("شما اجازه حذف این کاربر را ندارید.")

        mongo = self._get_mongo_instance()
        mongo.db[USERS_COLLECTION_NAME].delete_one({'user_id': user_id})
        self.bot_users = [u for u in self.bot_users if u.user_id != user_id]
        self.current_page = 1  # بازگشت به صفحه اول
        return rx.toast.info(f"کاربر با شناسه {user_id} حذف شد.")


    def on_dashboard_load(self):
        if not self.auth_state.is_authenticated:
            return rx.redirect("/login")
        # فراخوانی load_bot_users به عنوان یک event جداگانه
        return AdminState.load_bot_users()