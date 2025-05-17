# customer_data/backend/backend.py
# ... (Your existing imports: datetime, math, List, Optional, etc.)
import datetime
import math
from typing import Any, Optional, Union
import reflex as rx
from bson import ObjectId
import jdatetime
import pytz
from collections import Counter # Ensure Counter is imported

try:
    from .mongo import Mongo, ChatState
    from .auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL, REFERRAL_LEVEL_CONFIG
except ImportError:
    # ... (your existing fallbacks) ...
    pass


CHAT_STATE_TRANSLATIONS = {
    "HasAccess": "دسترسی دارد", "HasManualAccess": "دسترسی دستی دارد",
    "INITED": "کاربر جدید", "BLOCKED": "مسدود",
    "WaitForNationalId": "در انتظار کدملی", "WaitForOTP": "در انتظار کد",
    "WaitForCaptcha": "در انتظار کپچا", "LoggedIn": "لاگین شده",
}

class MongoUserDisplay(rx.Base): # Changed from Typeddict to rx.Base for direct use in rx.vars
    _id_str: Optional[str] = None
    username: Optional[str] = None
    national_id: Optional[str] = None
    raw_chat_state: Optional[str] = None
    chat_state_fa: Optional[str] = None
    created_at_str: Optional[str] = None
    updated_at_str: Optional[str] = None
    created_at_ts: Optional[float] = None
    channel_count: int = 0
    level: Optional[str] = None

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
    # ... (your existing state variables: users, current_user_for_edit, etc.) ...
    users: list[MongoUserDisplay] = []
    current_user_for_edit: Optional[MongoUserDisplay] = None
    sort_value: str = "created_at_ts"
    sort_reverse: bool = True
    search_value: str = ""
    current_page_number: int = 1
    users_per_page: int = 10
    total_registered_users: int = 0
    user_counts_by_level: dict[str, int] = {}
    users_in_channels_count: int = 0
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()


    # --- ADD THESE NEW VARS ---
    @rx.var
    def user_levels_pie_data(self) -> list[dict]:
        data = []
        # Ensure AuthState is accessible, for example, via get_state if needed in an event context.
        # For a var, it's better if AuthState is a substate or its relevant parts are copied/synced.
        # Assuming direct access or that this var is recalculated when AuthState changes.
        try:
            auth_state_instance = self.get_state(AuthState)
            allowed_levels = auth_state_instance.allowed_levels_for_current_referral
            current_level_translations = LEVEL_TRANSLATIONS # Global import
        except Exception: # Fallback if AuthState is not readily available
            allowed_levels = []
            current_level_translations = {}

        if not self.user_counts_by_level and not allowed_levels: # if no data and no defined levels
            return [{"name": "اطلاعات سطح موجود نیست", "value": 1, "fill": "var(--gray-8)"}]

        # Define colors for consistency or generate them
        colors = ["var(--blue-8)", "var(--green-8)", "var(--purple-8)", "var(--red-8)", "var(--orange-8)", "var(--cyan-8)", "var(--yellow-8)"]
        color_index = 0

        # Iterate through allowed levels to maintain order and ensure all allowed levels are considered
        for level_key in allowed_levels:
            count = self.user_counts_by_level.get(level_key, 0)
            if count > 0: # Only include levels that have users
                level_name = current_level_translations.get(level_key, level_key.replace("level_", "سطح "))
                data.append({
                    "name": level_name,
                    "value": count,
                    "fill": colors[color_index % len(colors)]
                })
                color_index += 1
        
        if not data: # If after checking all allowed levels, no users were found in them
             return [{"name": "کاربری در سطوح مجاز یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
        return data

    @rx.var
    def channel_membership_pie_data(self) -> list[dict]:
        users_in_channel = self.users_in_channels_count
        # Ensure total_users_for_current_referral is accurate
        total_users = self.total_users_for_current_referral # This should be updated in _recalculate_stats_async
        
        users_not_in_channel = total_users - users_in_channel

        if total_users == 0:
            return [{"name": "کاربری یافت نشد", "value": 1, "fill": "var(--gray-8)"}]

        data = []
        if users_in_channel >= 0: # Show even if zero, if total_users > 0
            data.append({"name": "عضو کانال", "value": users_in_channel, "fill": "var(--grass-8)"})
        if users_not_in_channel >= 0 and total_users > users_in_channel : # ensure it's not negative due to bad data
            data.append({"name": "عضو نشده", "value": users_not_in_channel, "fill": "var(--tomato-8)"})
        
        if not data and total_users > 0 :
            return [{"name": "اطلاعات عضویت موجود نیست", "value": total_users, "fill": "var(--gray-8)"}]
        elif not data and total_users == 0:
             return [{"name": "کاربری یافت نشد", "value": 1, "fill": "var(--gray-8)"}]
            
        return data
    # --- END OF NEW VARS ---

    async def clear_all_users_data(self):
        self.users = []
        self.current_page_number = 1
        self.current_user_for_edit = None
        await self._recalculate_stats_async() # Recalculate stats after clearing

    def clear_current_user_for_edit(self):
        self.current_user_for_edit = None

    @rx.var
    def _processed_users_for_display(self) -> list[MongoUserDisplay]:
        # ... (your existing _processed_users_for_display logic) ...
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
                   search_lower in str(user.channel_count or '').lower() # channel_count is int
            ]

        if self.sort_value:
            def sort_key_func(user_item: MongoUserDisplay):
                val = getattr(user_item, self.sort_value, None)
                if self.sort_value == "created_at_ts":
                    return float(val) if val is not None else (float('-inf') if not self.sort_reverse else float('inf'))
                if self.sort_value == "channel_count":
                    return int(val) if val is not None else (float('-inf') if not self.sort_reverse else float('inf'))
                if self.sort_value == "level":
                    if val is None: return (float('-inf') if not self.sort_reverse else float('inf'))
                    if isinstance(val, str) and val.startswith("level_"):
                        try: return int(val.split("_")[-1])
                        except: return (float('-inf') if not self.sort_reverse else float('inf'))
                    return (float('-inf') if not self.sort_reverse else float('inf'))
                return str(val or '').lower()
            try:
                users_to_process = sorted(users_to_process, key=sort_key_func, reverse=self.sort_reverse)
            except Exception as e:
                print(f"Sorting error in _processed_users_for_display: {e}")
        return users_to_process


    @rx.var
    def paginated_users(self) -> list[MongoUserDisplay]:
        # ... (your existing paginated_users logic) ...
        start_index = (self.current_page_number - 1) * self.users_per_page
        end_index = start_index + self.users_per_page
        return self._processed_users_for_display[start_index:end_index]


    @rx.var
    def total_pages(self) -> int:
        # ... (your existing total_pages logic) ...
        processed_users_len = len(self._processed_users_for_display)
        if not processed_users_len: return 1
        return math.ceil(processed_users_len / self.users_per_page)


    @rx.var
    def user_counts_by_level_var(self) -> dict[str, int]: return self.user_counts_by_level

    @rx.var
    def users_in_channels_count_var(self) -> int: return self.users_in_channels_count

    # ... (rest of your State class: load_entries, _recalculate_stats_async, sort_values, etc.)
    # Ensure _recalculate_stats_async updates total_users_for_current_referral correctly.

    async def load_entries(self, active_referral: Optional[str] = None):
        # If called without active_referral (e.g. from on_load of index page)
        # try to get it from AuthState.
        if active_referral is None:
            try:
                auth_state_instance = await self.get_state(AuthState)
                active_referral = auth_state_instance.current_logged_in_referral
            except Exception as e:
                print(f"Error getting active_referral from AuthState in load_entries: {e}")
                # Potentially yield a toast message if UI is available or log severely
                self.users = []
                await self._recalculate_stats_async()
                return

        if not active_referral:
            print("No active referral in load_entries, clearing users.")
            self.users = []
            await self._recalculate_stats_async()
            return

        mongo = get_mongo_client_instance()
        query_filter = {"referral": active_referral}
        # Fetch all users for the referral, sorting will be handled by _processed_users_for_display
        mongo_users_cursor = mongo.get_all_users_cursor(query_filter=query_filter)

        loaded_users = []
        for user_data in mongo_users_cursor: # type: ignore
            created_at_ts_val = user_data.get('created_at')
            created_at_jalali_str = "-"
            if isinstance(created_at_ts_val, (int, float)):
                try:
                    # Ensure it's a valid timestamp before converting
                    dt_utc_naive = datetime.datetime.utcfromtimestamp(created_at_ts_val)
                    dt_utc_aware = pytz.utc.localize(dt_utc_naive)
                    dt_tehran = dt_utc_aware.astimezone(TEHRAN_TZ)
                    j_datetime_tehran = jdatetime.datetime.fromgregorian(datetime=dt_tehran)
                    created_at_jalali_str = j_datetime_tehran.strftime('%Y/%m/%d  %H:%M:%S')
                except (OSError, OverflowError, ValueError) as e: # Catch potential errors from invalid timestamp
                    print(f"Timestamp conversion error for created_at {created_at_ts_val}: {e}")
                    created_at_jalali_str = "تاریخ نامعتبر"


            updated_at_ts_val = user_data.get('updated_at')
            updated_at_jalali_str = "-"
            if isinstance(updated_at_ts_val, (int, float)):
                try:
                    dt_utc_naive_up = datetime.datetime.utcfromtimestamp(updated_at_ts_val)
                    dt_utc_aware_up = pytz.utc.localize(dt_utc_naive_up)
                    dt_tehran_up = dt_utc_aware_up.astimezone(TEHRAN_TZ)
                    j_datetime_tehran_up = jdatetime.datetime.fromgregorian(datetime=dt_tehran_up)
                    updated_at_jalali_str = j_datetime_tehran_up.strftime('%Y/%m/%d  %H:%M:%S')
                except (OSError, OverflowError, ValueError) as e:
                    print(f"Timestamp conversion error for updated_at {updated_at_ts_val}: {e}")
                    updated_at_jalali_str = "تاریخ نامعتبر"


            display_user = MongoUserDisplay(
                _id_str=str(user_data.get('_id')) if user_data.get('_id') else None,
                username=user_data.get('username'),
                national_id=user_data.get('national_id'),
                raw_chat_state=user_data.get('chat_state'),
                chat_state_fa=CHAT_STATE_TRANSLATIONS.get(user_data.get('chat_state', ""), user_data.get('chat_state', "") or "-"),
                created_at_str=created_at_jalali_str,
                updated_at_str=updated_at_jalali_str,
                created_at_ts=float(created_at_ts_val) if isinstance(created_at_ts_val, (int, float)) else None,
                channel_count=len(user_data.get('channels', [])) if isinstance(user_data.get('channels'), list) else 0,
                level=user_data.get('level') if isinstance(user_data.get('level'), str) else None,
            )
            if display_user._id_str is None:
                continue # Skip users with no ID
            loaded_users.append(display_user)

        self.users = loaded_users
        self.current_page_number = 1 # Reset to first page
        await self._recalculate_stats_async()


    async def _recalculate_stats_async(self):
        self.total_registered_users = len(self.users)
        self.current_month_values = MonthValues(num_customers=self.total_registered_users) # Example stat

        # Calculate users in channels
        count_in_channels = 0
        for user in self.users:
            if user.channel_count > 0:
                count_in_channels += 1
        self.users_in_channels_count = count_in_channels

        # Calculate user counts by level
        # Ensure AuthState is available to get allowed_levels_for_current_referral
        temp_counts: dict[str, int] = {}
        try:
            auth_state_instance = await self.get_state(AuthState)
            allowed_levels_for_stats = auth_state_instance.allowed_levels_for_current_referral
        except Exception:
            allowed_levels_for_stats = [] # Fallback

        if allowed_levels_for_stats:
            # Initialize counts for all allowed levels to 0
            for level_key in allowed_levels_for_stats:
                temp_counts[level_key] = 0

            level_values_in_users = [user.level for user in self.users if user.level is not None and user.level in allowed_levels_for_stats]
            level_counts_from_users = Counter(level_values_in_users)

            for level_key, count in level_counts_from_users.items():
                temp_counts[level_key] = count
        
        self.user_counts_by_level = temp_counts
        # Update total_users_for_current_referral (already done by self.total_registered_users)
        # self.total_users_for_current_referral = self.total_registered_users # This is a @rx.var, not directly set

    def sort_values(self, sort_by: str):
        if self.sort_value == sort_by:
            self.sort_reverse = not self.sort_reverse
        else:
            self.sort_value = sort_by
            self.sort_reverse = False # Default to ascending when changing column
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
        # Find user from self.users list
        user_to_edit = next((u for u in self.users if u._id_str == object_id_str), None)
        if user_to_edit:
            self.current_user_for_edit = user_to_edit.copy() # Create a copy for editing form
        else:
            self.current_user_for_edit = None
            print(f"--- WARNING: User {object_id_str} not found in self.users for edit. ---")


    async def add_customer_to_db(self, form_data: dict):
        # ... (your existing add_customer_to_db logic) ...
        auth_state = await self.get_state(AuthState) # type: ignore
        active_referral = auth_state.current_logged_in_referral
        if not active_referral: return rx.toast.error("کد معرف نامعتبر.", position="bottom-right")
        allowed_levels = auth_state.allowed_levels_for_current_referral
        level_from_form = form_data.get("level")
        level_to_store: Optional[str] = None
        if level_from_form == NO_LEVEL_VALUE_INTERNAL: level_to_store = None
        elif level_from_form and level_from_form in allowed_levels: level_to_store = level_from_form
        # elif not level_from_form and allowed_levels: level_to_store = allowed_levels[0] # Default to first allowed if none selected?
        elif level_from_form: # Level selected but not allowed
            label = LEVEL_TRANSLATIONS.get(level_from_form, level_from_form)
            return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")
        mongo = get_mongo_client_instance()
        new_doc = {
            "username": form_data.get("username"), "national_id": form_data.get("national_id"),
            "chat_state": form_data.get("chat_state"), "level": level_to_store,
            "created_at": int(datetime.datetime.now().timestamp()), "updated_at": int(datetime.datetime.now().timestamp()),
            "channels": [], "referral": active_referral,
            "user_id": mongo.db.users.count_documents({}) + 6000000000 # This user_id generation might need review for scale
        }
        if not new_doc["username"]:
             return rx.toast.error("نام کاربری نمی‌تواند خالی باشد.", position="bottom-right")
        if mongo.db.users.find_one({"username": new_doc["username"], "referral": active_referral}):
            return rx.toast.error(f"کاربری با نام کاربری '{new_doc['username']}' قبلا برای این معرف ثبت شده.", position="bottom-right")
        result = mongo.insert_user(new_doc)
        if result.inserted_id:
            await self.load_entries(active_referral=active_referral)
            return rx.toast.success(f"کاربر {new_doc.get('username', 'جدید')} افزوده شد.", position="bottom-right")
        return rx.toast.error("خطا در افزودن کاربر.", position="bottom-right")


    async def update_customer_to_db(self, form_data: dict):
        # ... (your existing update_customer_to_db logic) ...
        auth_state = await self.get_state(AuthState) # type: ignore
        if not self.current_user_for_edit or not self.current_user_for_edit._id_str:
            return rx.toast.error("کاربری برای ویرایش انتخاب نشده است.", position="bottom-right")
        obj_id_str = self.current_user_for_edit._id_str
        original_data = self.current_user_for_edit # This is a MongoUserDisplay (rx.Base model)
        allowed_levels = auth_state.allowed_levels_for_current_referral
        set_payload: dict[str, Any] = {}; unset_payload: dict[str, Any] = {}; changed = False

        if (val := form_data.get("username")) is not None and val != original_data.username: set_payload["username"] = val; changed = True
        if "national_id" in form_data: # Handle empty string for national_id
            val = form_data.get("national_id")
            if val != original_data.national_id: # national_id can be None or ""
                set_payload["national_id"] = val if val else "" # Store empty string if cleared
                changed = True
        if (val := form_data.get("chat_state")) is not None and val != original_data.raw_chat_state: set_payload["chat_state"] = val; changed = True

        if (val := form_data.get("level")) is not None and val != original_data.level:
            if val == NO_LEVEL_VALUE_INTERNAL: # User wants to remove the level
                if original_data.level is not None: # Only unset if it previously had a level
                    unset_payload["level"] = ""; changed = True
            elif val in allowed_levels: # User selected an allowed level
                set_payload["level"] = val; changed = True
            else: # Selected level is not allowed
                label = LEVEL_TRANSLATIONS.get(val, val)
                return rx.toast.error(f"سطح '{label}' برای این معرف مجاز نیست.", position="bottom-right")

        if not changed:
            self.clear_current_user_for_edit()
            return rx.toast.info("تغییری برای اعمال وجود ندارد.", position="bottom-right")

        set_payload["updated_at"] = int(datetime.datetime.now().timestamp())
        mongo = get_mongo_client_instance()
        active_referral = auth_state.current_logged_in_referral

        # Verify user belongs to this referral before updating
        user_doc_from_db = mongo.get_user_by_object_id(obj_id_str)
        if not user_doc_from_db or user_doc_from_db.get("referral") != active_referral:
            self.clear_current_user_for_edit()
            return rx.toast.error("شما اجازه ویرایش این کاربر را ندارید یا کاربر یافت نشد.", position="bottom-right")

        ops: dict[str, Any] = {}
        if set_payload: ops['$set'] = set_payload
        if unset_payload: ops['$unset'] = unset_payload

        if ops:
            try:
                update_result = mongo.db.users.update_one({'_id': ObjectId(obj_id_str)}, ops)
                if update_result.matched_count == 0:
                    self.clear_current_user_for_edit()
                    return rx.toast.error("کاربر برای به‌روزرسانی یافت نشد (احتمالا حذف شده).", position="bottom-right")

            except Exception as e:
                self.clear_current_user_for_edit()
                return rx.toast.error(f"خطا در پایگاه داده هنگام به‌روزرسانی: {e}", position="bottom-right")

        await self.load_entries(active_referral=active_referral) # Reload all users for the referral
        self.clear_current_user_for_edit()
        display_username = set_payload.get("username", original_data.username or "")
        return rx.toast.success(f"کاربر {display_username} به‌روز شد.", position="bottom-right")


    async def delete_customer(self, object_id_str: Optional[str]):
        # ... (your existing delete_customer logic) ...
        if not object_id_str: return rx.toast.error("شناسه کاربر نامعتبر است.", position="bottom-right")
        auth_state = await self.get_state(AuthState) # type: ignore
        active_referral = auth_state.current_logged_in_referral
        mongo = get_mongo_client_instance()
        user_doc = mongo.get_user_by_object_id(object_id_str) # type: ignore
        if not user_doc: return rx.toast.error("کاربر یافت نشد.", position="bottom-right")
        if user_doc.get("referral") != active_referral: return rx.toast.error("شما اجازه حذف این کاربر را ندارید.", position="bottom-right")
        result = mongo.delete_user_by_object_id(object_id_str) # type: ignore
        if result and result.deleted_count > 0:
            await self.load_entries(active_referral=active_referral)
            if self.current_user_for_edit and self.current_user_for_edit._id_str == object_id_str:
                self.clear_current_user_for_edit()
            return rx.toast.success(f"کاربر {user_doc.get('username', object_id_str)} حذف شد.", position="bottom-right")
        return rx.toast.error("خطا در حذف کاربر یا کاربر قبلا حذف شده.", position="bottom-right")


    @rx.var
    def total_users_for_current_referral(self) -> int:
        return self.total_registered_users

    def next_page_handler(self):
        if self.current_page_number < self.total_pages:
            self.current_page_number += 1

    def prev_page_handler(self):
        if self.current_page_number > 1:
            self.current_page_number -= 1

    def first_page_handler(self):
        self.current_page_number = 1

    def last_page_handler(self):
        self.current_page_number = self.total_pages


def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    if prev_value == 0:
        return float("inf") if value > 0 else 0.0 # Or handle as 100% if value > 0 and prev_value = 0
    return round(((value - prev_value) / prev_value) * 100, 2)