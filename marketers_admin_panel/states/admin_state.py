import reflex as rx
from typing import List, Dict, Any, Optional
import datetime

from ..models.bot_user import BotUser
from ..remote_db.mongo import Mongo, DEFAULT_MONGO_DB_NAME, USERS_COLLECTION
from .auth_state import AuthState


class AdminState(rx.State):
    bot_users: List[BotUser] = []
    is_loading: bool = False
    search_term: str = ""
    current_page: int = 1
    items_per_page: int = 15

    show_edit_dialog: bool = False
    editing_user: Optional[BotUser] = None
    edit_form_data: Dict[str, Any] = {}

    _mongo_client_instance: Optional[Mongo] = None

    @rx.var
    def current_admin_username(self) -> Optional[str]:
        auth_s = self.get_substate(AuthState)
        return auth_s.logged_in_admin_username if auth_s and auth_s.logged_in_admin_username is not None else None

    @rx.var
    def current_admin_referral_type(self) -> Optional[str]:
        auth_s = self.get_substate(AuthState)
        return auth_s.logged_in_admin_referral_type if auth_s and auth_s.logged_in_admin_referral_type else None

    @rx.var
    def is_current_admin_super_admin(self) -> bool:
        auth_s = self.get_substate(AuthState)
        return auth_s.is_logged_in_super_admin if auth_s else False

    @rx.var
    def is_admin_authenticated(self) -> bool:
        auth_s = self.get_substate(AuthState)
        return auth_s.is_authenticated if auth_s else False

    def _get_mongo_instance(self) -> Optional[Mongo]:
        if self._mongo_client_instance is None or not self._mongo_client_instance.is_connected():
            print("AdminState: Attempting to create/recreate MongoDB instance...")
            self._mongo_client_instance = Mongo(mongo_db_name=DEFAULT_MONGO_DB_NAME)
            if not self._mongo_client_instance.is_connected():
                print("AdminState: FATAL - Could not connect to MongoDB in _get_mongo_instance.")
                return None
        return self._mongo_client_instance

    def _format_timestamp_str(self, ts: Optional[int]) -> str:
        if ts is not None:
            try:
                return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            except (TypeError, ValueError): return str(ts)
        return "-"

    def _get_trial_status_display_str(self, trial_ended: Optional[bool], trial_noticed: Optional[bool], level: Optional[str]) -> str:
        if trial_ended is True: return "پایان یافته"
        if trial_noticed is True: return "اطلاع داده شده"
        if level == "level_0": return "فعال"
        return "نامشخص"

    def _format_channels_display_str(self, channels_list: Optional[List[int]]) -> str:
        if channels_list and isinstance(channels_list, list):
            return ", ".join(map(str, channels_list))
        return "-"

    def _map_mongo_to_botuser(self, mongo_data: Dict[str, Any]) -> Optional[BotUser]:
        if not mongo_data or mongo_data.get("user_id") is None: return None
        try:
            created_at_ts = mongo_data.get("created_at")
            updated_at_ts = mongo_data.get("updated_at")
            level_checked_at_ts = mongo_data.get("level_checked_at")
            channels_list = mongo_data.get("channels")
            trial_ended_val = bool(mongo_data.get("trial_ended")) if mongo_data.get("trial_ended") is not None else None
            trial_noticed_val = bool(mongo_data.get("trial_noticed")) if mongo_data.get("trial_noticed") is not None else None
            level_val = mongo_data.get("level")

            return BotUser(
                user_id=int(mongo_data["user_id"]),
                national_id=str(mongo_data.get("national_id")) if mongo_data.get("national_id") is not None else None,
                username=mongo_data.get("username"),
                chat_state=mongo_data.get("chat_state"),
                chat_id=int(mongo_data.get("chat_id")) if mongo_data.get("chat_id") is not None else None,
                updated_at=int(updated_at_ts) if isinstance(updated_at_ts, (int, float)) else None,
                created_at=int(created_at_ts) if isinstance(created_at_ts, (int, float)) else None,
                referral=mongo_data.get("referral"),
                agent_code=mongo_data.get("agent_code"),
                trial_noticed=trial_noticed_val,
                trial_ended=trial_ended_val,
                level=level_val,
                level_checked_at=int(level_checked_at_ts) if isinstance(level_checked_at_ts, (int, float)) else None,
                channels=channels_list if isinstance(channels_list, list) else None,
                registration_wizard_step=int(mongo_data.get("registration_wizard_step")) if mongo_data.get("registration_wizard_step") is not None else None,
                capital_limit=mongo_data.get("capital_limit"),
                created_at_str=self._format_timestamp_str(int(created_at_ts) if isinstance(created_at_ts, (int, float)) else None),
                updated_at_str=self._format_timestamp_str(int(updated_at_ts) if isinstance(updated_at_ts, (int, float)) else None),
                level_checked_at_str=self._format_timestamp_str(int(level_checked_at_ts) if isinstance(level_checked_at_ts, (int, float)) else None),
                channels_str=self._format_channels_display_str(channels_list if isinstance(channels_list, list) else None),
                trial_status_str=self._get_trial_status_display_str(trial_ended_val, trial_noticed_val, level_val)
            )
        except Exception as e:
            print(f"AdminState: Error mapping MongoDB data for user_id {mongo_data.get('user_id')}: {type(e).__name__} - {e}")
            return None

    @rx.var
    def filtered_bot_users(self) -> List[BotUser]:
        users = self.bot_users
        if self.search_term:
            term = self.search_term.lower().strip()
            if term:
                users = [
                    u for u in users if
                    (u.username and term in u.username.lower()) or
                    (u.national_id and term in u.national_id) or
                    (str(u.user_id) and term == str(u.user_id)) or
                    (u.referral and term in u.referral.lower()) or
                    (u.agent_code and term in u.agent_code.lower()) or
                    (u.level and term in u.level.lower()) or
                    (u.chat_state and term in u.chat_state.lower())
                ]
        return users

    @rx.var
    def paginated_users(self) -> List[BotUser]:
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page
        return self.filtered_bot_users[start_index:end_index]

    @rx.var
    def total_pages(self) -> int:
        import math
        if not self.filtered_bot_users or self.items_per_page <= 0: return 1
        return math.ceil(len(self.filtered_bot_users) / self.items_per_page)

    def set_search_term(self, term: str):
        self.search_term = term
        self.current_page = 1

    def go_to_page(self, page_num_str: str):
        try:
            page_num = int(page_num_str)
            if 1 <= page_num <= self.total_pages: self.current_page = page_num
        except ValueError: pass

    def next_page(self):
        if self.current_page < self.total_pages: self.current_page +=1

    def prev_page(self):
        if self.current_page > 1: self.current_page -= 1

    async def load_bot_users(self):
        if not self.is_admin_authenticated:
            yield rx.redirect("/login"); return
        self.is_loading = True; yield

        mongo = self._get_mongo_instance()
        if not mongo:
            self.is_loading = False
            yield rx.toast.error("خطا: عدم امکان اتصال به دیتابیس MongoDB.", duration=5000, position="top_center")
            return

        query_filter = {}
        referral_type_for_query = self.current_admin_referral_type
        if not self.is_current_admin_super_admin:
            if referral_type_for_query:
                query_filter["referral"] = referral_type_for_query
            else:
                self.bot_users = []; self.is_loading = False
                yield rx.toast.info("هیچ referral برای این ادمین تعریف نشده است.", position="top_center")
                return
        try:
            mongo_users_cursor = mongo.get_users_cursor(query_filter)
            all_mongo_users_data = list(mongo_users_cursor)
        except Exception as e:
            self.is_loading = False
            yield rx.toast.error(f"خطا در خواندن اطلاعات از دیتابیس: {str(e)}", duration=5000, position="top_center")
            return

        temp_users = [self._map_mongo_to_botuser(ud) for ud in all_mongo_users_data]
        self.bot_users = sorted(
            [u for u in temp_users if u is not None],
            key=lambda u: u.created_at if u.created_at is not None else 0,
            reverse=True
        )
        self.current_page = 1; self.is_loading = False; yield

    def start_edit_user(self, user_to_edit: BotUser):
        self.editing_user = user_to_edit
        self.edit_form_data = {
            "national_id": user_to_edit.national_id or "", "username": user_to_edit.username or "",
            "chat_state": user_to_edit.chat_state or "", "level": user_to_edit.level or "",
            "referral": user_to_edit.referral or "", "agent_code": user_to_edit.agent_code or "",
            "trial_noticed": bool(user_to_edit.trial_noticed) if user_to_edit.trial_noticed is not None else False,
            "trial_ended": bool(user_to_edit.trial_ended) if user_to_edit.trial_ended is not None else False,
            "capital_limit": user_to_edit.capital_limit or "",
            "chat_id": str(user_to_edit.chat_id) if user_to_edit.chat_id is not None else "",
            "registration_wizard_step": str(user_to_edit.registration_wizard_step) if user_to_edit.registration_wizard_step is not None else "",
        }
        self.show_edit_dialog = True

    def handle_edit_form_change(self, field_name: str, value: Any):
        if field_name in ["trial_noticed", "trial_ended"]:
             self.edit_form_data[field_name] = bool(value)
        else:
            self.edit_form_data[field_name] = str(value)

    async def save_user_changes(self):
        if self.editing_user is None:
            yield rx.toast.error("کاربری برای ویرایش انتخاب نشده است.", position="top_center"); return
        mongo = self._get_mongo_instance()
        if not mongo:
            yield rx.toast.error("خطا در اتصال به دیتابیس.", position="top_center"); return

        user_id_to_update = self.editing_user.user_id
        updates_to_apply: Dict[str, Any] = {}
        for key, raw_value_form in self.edit_form_data.items():
            original_value_obj = getattr(self.editing_user, key, None)
            new_value_typed: Any = None
            if key in ["trial_noticed", "trial_ended"]: new_value_typed = bool(raw_value_form)
            elif key in ["chat_id", "registration_wizard_step"]:
                try: new_value_typed = int(str(raw_value_form).strip()) if str(raw_value_form).strip() else None
                except ValueError: new_value_typed = None
            else:
                new_value_typed = str(raw_value_form).strip()
                if new_value_typed == "" and key not in ["username", "national_id", "agent_code", "capital_limit", "referral", "level", "chat_state"]:
                    new_value_typed = None
            if new_value_typed != original_value_obj:
                updates_to_apply[key] = new_value_typed
        
        if not updates_to_apply:
            self.show_edit_dialog = False
            yield rx.toast.info("هیچ تغییری برای ذخیره اعمال نشد.", position="top_center"); return

        updates_to_apply["updated_at"] = int(datetime.datetime.now().timestamp())
        referral_type_for_check = self.current_admin_referral_type
        if not self.is_current_admin_super_admin and "referral" in updates_to_apply:
            if updates_to_apply["referral"] != referral_type_for_check :
                yield rx.toast.error("شما اجازه تغییر referral به این مقدار را ندارید.", position="top_center"); return
        try:
            result = mongo.update_user_properties(user_id_to_update, updates_to_apply)
            if result and result.modified_count > 0 :
                yield rx.toast.success("اطلاعات کاربر با موفقیت به‌روز شد.", position="top_center")
                mongo_user_data_updated = mongo.db[USERS_COLLECTION].find_one({'user_id': user_id_to_update})
                if mongo_user_data_updated:
                    mapped_user = self._map_mongo_to_botuser(mongo_user_data_updated)
                    if mapped_user:
                        for i, u in enumerate(self.bot_users):
                            if u.user_id == user_id_to_update: self.bot_users[i] = mapped_user; break
            elif result and result.matched_count > 0:
                 yield rx.toast.info("تغییری برای اعمال وجود نداشت.", position="top_center")
            else:
                yield rx.toast.error("خطایی در به‌روزرسانی کاربر رخ داد یا کاربری یافت نشد.", position="top_center")
            self.show_edit_dialog = False; self.editing_user = None
        except Exception as e:
            print(f"AdminState: Error saving user changes for user_id {user_id_to_update}: {e}")
            yield rx.toast.error(f"خطا در ذخیره تغییرات: {str(e)}", position="top_center")
        yield

    async def delete_bot_user(self, user_id: int):
        if not self.is_admin_authenticated:
            yield rx.toast.error("ابتدا وارد شوید.", position="top_center"); return
        referral_type_for_check = self.current_admin_referral_type
        if not self.is_current_admin_super_admin:
            user_to_delete = next((u for u in self.bot_users if u.user_id == user_id), None)
            if not user_to_delete or user_to_delete.referral != referral_type_for_check:
                yield rx.toast.error("شما اجازه حذف این کاربر را ندارید.", position="top_center"); return
        mongo = self._get_mongo_instance()
        if not mongo:
            yield rx.toast.error("خطا در اتصال به دیتابیس.", position="top_center"); return
        try:
            result = mongo.delete_user(user_id)
            if result and result.deleted_count > 0:
                self.bot_users = [u for u in self.bot_users if u.user_id != user_id]
                if not self.paginated_users and self.current_page > 1: self.current_page -=1
                elif len(self.filtered_bot_users) == 0 : self.current_page =1
                yield rx.toast.success(f"کاربر با شناسه {user_id} حذف شد.", position="top_center")
            else:
                yield rx.toast.error(f"کاربری با شناسه {user_id} برای حذف پیدا نشد یا خطایی رخ داد.", position="top_center")
        except Exception as e:
            yield rx.toast.error(f"خطا در حذف کاربر: {str(e)}", position="top_center")
        yield

    def on_dashboard_load(self):
        if not self.is_admin_authenticated:
            return rx.redirect("/login")
        return AdminState.load_bot_users