import datetime
import math
from typing import List, Optional, Union, TypedDict

import reflex as rx
try:
    from .mongo import Mongo, ChatState
    from .auth_state import AuthState 
except ImportError:
    # Fallback imports for local execution or different project structures
    from mongo import Mongo, ChatState
    try:
        from auth_state import AuthState
    except ImportError:
        # Mock AuthState to prevent complete application failure if auth_state.py is missing during development
        class AuthState(rx.State): # type: ignore
            current_logged_in_referral: Optional[str] = "test_referral" # Default for testing
            is_logged_in: bool = True 
            @rx.var
            def token_is_valid(self) -> bool: return self.is_logged_in


CHAT_STATE_TRANSLATIONS = {
    "HasAccess": "دسترسی دارد",
    "HasManualAccess": "دسترسی دستی دارد",
    "INITED": "کاربر جدید",
    "BLOCKED": "مسدود",
    "WaitForNationalId": "در انتظار کدملی",
    "WaitForOTP": "در انتظار کد",
    "WaitForCaptcha": "در انتظار کپچا",
    "LoggedIn": "لاگین شده",
}

class MongoUserDisplay(TypedDict):
    _id_str: Optional[str]
    username: Optional[str]
    national_id: Optional[str]
    raw_chat_state: Optional[str] 
    chat_state_fa: Optional[str] # برای نمایش فارسی در جدول
    created_at_str: Optional[str]
    updated_at_str: Optional[str]
    channel_count: int


class MonthValues(rx.Base):
    num_customers: int = 0


_mongo_client_global_instance: Optional[Mongo] = None
YOUR_MONGO_DB_NAME = "marketersbot" 

def get_mongo_client_instance() -> Mongo:
    global _mongo_client_global_instance
    if _mongo_client_global_instance is None:
        _mongo_client_global_instance = Mongo(mongo_db_name=YOUR_MONGO_DB_NAME)
    return _mongo_client_global_instance


class State(rx.State): 
    users: list[MongoUserDisplay] = []
    current_user_for_edit: Optional[MongoUserDisplay] = None

    sort_value: str = "username"
    sort_reverse: bool = False
    search_value: str = ""

    current_page_number: int = 1
    users_per_page: int = 10

    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()

    # --- Event Handlers ---
    async def clear_all_users_data(self):
        """ تمام داده‌های کاربران و آمار مربوطه را پاک می‌کند. """
        self.users = []
        self.current_page_number = 1
        self.current_user_for_edit = None
        self._recalculate_stats() # این یک متد همگام است و نیازی به await ندارد
        # print("--- DEBUG: All user data cleared from MainState ---")

    def clear_current_user_for_edit(self): # <<< تعریف متد به عنوان event handler معمولی
        """ کاربر انتخاب شده برای ویرایش را پاک می‌کند. """
        self.current_user_for_edit = None
        # print("--- DEBUG: current_user_for_edit in MainState cleared ---")


    # --- Computed Vars ---
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
                   search_lower in str(user.get('channel_count', '')).lower()
            ]

        if self.sort_value:
            def sort_key_func(user_item):
                val = user_item.get(self.sort_value)
                if self.sort_value == "channel_count":
                    return int(val) if val is not None else (-float('inf') if self.sort_reverse else float('inf'))
                elif isinstance(val, str): return val.lower()
                elif isinstance(val, (int, float)): return val if val is not None else (-float('inf') if self.sort_reverse else float('inf'))
                return str(val)
            users_to_process = sorted(users_to_process, key=sort_key_func, reverse=self.sort_reverse)
        return users_to_process

    @rx.var
    def paginated_users(self) -> list[MongoUserDisplay]:
        start_index = (self.current_page_number - 1) * self.users_per_page
        end_index = start_index + self.users_per_page
        return self._processed_users_for_display[start_index:end_index]

    @rx.var
    def total_pages(self) -> int:
        if not self._processed_users_for_display: return 1
        total_items = len(self._processed_users_for_display)
        return math.ceil(total_items / self.users_per_page) if total_items > 0 else 1

    @rx.var
    def customers_change(self) -> float:
        current_customers = self.current_month_values.num_customers
        previous_customers = self.previous_month_values.num_customers
        return _get_percentage_change(current_customers, previous_customers)
        
    async def load_entries(self, active_referral: Optional[str] = None):
        if active_referral is None:
            try:
                auth_state_instance = await self.get_state(AuthState)
                active_referral = auth_state_instance.current_logged_in_referral
            except Exception as e:
                print(f"Error getting active_referral from AuthState in load_entries (fallback): {e}")
                active_referral = None

        if not active_referral:
            self.users = []
            self._recalculate_stats()
            return

        mongo = get_mongo_client_instance()
        query_filter = {"referral": active_referral}
        mongo_users_cursor = mongo.get_all_users_cursor(query_filter)
        
        loaded_users = []
        for user_data in mongo_users_cursor:
            created_at_ts = user_data.get('created_at')
            created_at_str = datetime.datetime.fromtimestamp(created_at_ts).strftime('%Y-%m-%d %H:%M:%S') if isinstance(created_at_ts, (int,float)) else str(created_at_ts)
            updated_at_ts = user_data.get('updated_at')
            updated_at_str = datetime.datetime.fromtimestamp(updated_at_ts).strftime('%Y-%m-%d %H:%M:%S') if isinstance(updated_at_ts, (int,float)) else str(updated_at_ts)
            object_id = user_data.get('_id')
            channels_data = user_data.get('channels')
            current_channel_count = len(channels_data) if channels_data and isinstance(channels_data, list) else 0
            raw_chat_state_val = user_data.get('chat_state')
            _id_str_val = str(object_id) if object_id else None

            display_user: MongoUserDisplay = {
                '_id_str': _id_str_val,
                'username': user_data.get('username'),
                'national_id': user_data.get('national_id'),
                'raw_chat_state': raw_chat_state_val,
                'created_at_str': created_at_str,
                'updated_at_str': updated_at_str,
                'channel_count': current_channel_count,
                'chat_state_fa': CHAT_STATE_TRANSLATIONS.get(raw_chat_state_val, raw_chat_state_val if raw_chat_state_val else "نامشخص"),
            }
            if _id_str_val is None: continue
            loaded_users.append(display_user)
        
        self.users = loaded_users
        self.current_page_number = 1
        self._recalculate_stats()

    def _recalculate_stats(self):
        self.current_month_values = MonthValues(num_customers=len(self.users))
        self.previous_month_values = MonthValues(num_customers=len(self.users))

    def sort_values(self, sort_by: str):
        if self.sort_value == sort_by: self.sort_reverse = not self.sort_reverse
        else: self.sort_value = sort_by; self.sort_reverse = False
        self.current_page_number = 1

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.current_page_number = 1

    def filter_values(self, search_term: str):
        self.search_value = search_term
        self.current_page_number = 1

    def set_current_user_for_edit(self, object_id_str: Optional[str]):
        if not object_id_str:
            self.current_user_for_edit = None
            return
        found_user = next((user for user in self.users if user.get('_id_str') == object_id_str), None)
        if found_user:
            self.current_user_for_edit = found_user.copy()
        else:
            self.current_user_for_edit = None
            print(f"--- WARNING: User with _id {object_id_str} not found in self.users for editing. ---")
    
    async def add_customer_to_db(self, form_data: dict):
        auth_state_instance = await self.get_state(AuthState)
        active_referral = auth_state_instance.current_logged_in_referral
        if not active_referral:
            return rx.toast.error("خطا: کد معرف معتبر نیست.", position="bottom-right")

        mongo = get_mongo_client_instance()
        try:
            new_user_mongo_doc = {
                "username": form_data.get("username"),
                "national_id": form_data.get("national_id"),
                "chat_state": form_data.get("chat_state"),
                "created_at": int(datetime.datetime.now().timestamp()),
                "updated_at": int(datetime.datetime.now().timestamp()),
                "channels": [],
                "referral": active_referral,
                "user_id": mongo.db.users.count_documents({}) + 60000000 
            }
            query_for_uniqueness = {"username": new_user_mongo_doc["username"], "referral": active_referral}
            if mongo.db.users.find_one(query_for_uniqueness):
                 return rx.toast.error(f"کاربری با نام کاربری '{new_user_mongo_doc['username']}' برای این معرف قبلا ثبت شده.", position="bottom-right")
            
            result = mongo.insert_user(new_user_mongo_doc)
            if result.inserted_id:
                await self.load_entries(active_referral=active_referral)
                return rx.toast.success(f"کاربر {new_user_mongo_doc.get('username', 'جدید')} افزوده شد.", position="bottom-right")
            else: return rx.toast.error("خطا در افزودن کاربر.", position="bottom-right")
        except Exception as e: return rx.toast.error(f"خطا در افزودن کاربر: {str(e)}", position="bottom-right")

    async def update_customer_to_db(self, form_data: dict):
        mongo = get_mongo_client_instance()
        if not self.current_user_for_edit or not self.current_user_for_edit.get("_id_str"):
            return rx.toast.error("کاربری برای ویرایش انتخاب نشده است.", position="bottom-right")
        object_id_to_update = self.current_user_for_edit["_id_str"]
        update_payload = {}
        if form_data.get("username") is not None: update_payload["username"] = form_data["username"]
        if form_data.get("national_id") is not None: update_payload["national_id"] = form_data["national_id"]
        if form_data.get("chat_state") is not None: update_payload["chat_state"] = form_data["chat_state"]
        
        if not update_payload:
            self.clear_current_user_for_edit() 
            return rx.toast.info("تغییری برای اعمال وجود ندارد.", position="bottom-right")
        update_payload["updated_at"] = int(datetime.datetime.now().timestamp())
        try:
            auth_state_instance = await self.get_state(AuthState)
            active_referral = auth_state_instance.current_logged_in_referral
            user_to_update_doc = mongo.get_user_by_object_id(object_id_to_update) 
            if not user_to_update_doc or user_to_update_doc.get("referral") != active_referral:
                return rx.toast.error("شما اجازه ویرایش این کاربر را ندارید.", position="bottom-right")

            mongo.update_user_properties_by_object_id(object_id_to_update, update_payload) 
            await self.load_entries(active_referral=active_referral)
            self.clear_current_user_for_edit() 
            return rx.toast.success(f"کاربر {update_payload.get('username', '')} به‌روزرسانی شد.", position="bottom-right")
        except Exception as e: return rx.toast.error(f"خطا در به‌روزرسانی: {str(e)}", position="bottom-right")

    async def delete_customer(self, object_id_str: Optional[str]):
        if not object_id_str: return rx.toast.error("شناسه کاربر نامعتبر است.", position="bottom-right")
        mongo = get_mongo_client_instance()
        try:
            user_to_delete_doc = mongo.get_user_by_object_id(object_id_str)
            if not user_to_delete_doc: return rx.toast.error("کاربر یافت نشد.", position="bottom-right")

            auth_state_instance = await self.get_state(AuthState)
            active_referral = auth_state_instance.current_logged_in_referral
            if user_to_delete_doc.get("referral") != active_referral:
                return rx.toast.error("شما اجازه حذف این کاربر را ندارید.", position="bottom-right")

            result = mongo.delete_user_by_object_id(object_id_str)
            if result.deleted_count > 0:
                await self.load_entries(active_referral=active_referral)
                if self.current_user_for_edit and self.current_user_for_edit.get("_id_str") == object_id_str:
                    self.clear_current_user_for_edit() 
                return rx.toast.success(f"کاربر {user_to_delete_doc.get('username', object_id_str)} حذف شد.", position="bottom-right")
            else: return rx.toast.error("خطا در حذف.", position="bottom-right")
        except Exception as e: return rx.toast.error(f"خطا در حذف: {str(e)}", position="bottom-right")
    
    @rx.var
    def total_users_for_current_referral(self) -> int:
        return len(self._processed_users_for_display)

    def next_page_handler(self):
        if self.current_page_number < self.total_pages: self.current_page_number += 1
    def prev_page_handler(self):
        if self.current_page_number > 1: self.current_page_number -= 1
    def first_page_handler(self): self.current_page_number = 1
    def last_page_handler(self): self.current_page_number = self.total_pages

def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    if prev_value == 0: return float("inf") if value > 0 else 0.0
    return round(((value - prev_value) / prev_value) * 100, 2)

