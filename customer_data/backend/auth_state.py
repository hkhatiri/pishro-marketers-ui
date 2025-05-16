# customer_data/backend/auth_state.py
import reflex as rx
from typing import Optional, List, Dict, Tuple

try:
    # اگر NO_LEVEL_VALUE_INTERNAL را در یک فایل کانفیگ مشترک دارید:
    # from .backend_config import NO_LEVEL_VALUE_INTERNAL
    # در غیر این صورت، اینجا تعریف کنید یا از backend.py ایمپورت کنید اگر تعریف شده
    NO_LEVEL_VALUE_INTERNAL = "_NO_LEVEL_" 
except ImportError:
    NO_LEVEL_VALUE_INTERNAL = "_NO_LEVEL_"


ADMIN_CREDENTIALS = {
    "admin_kahyani": {"password": "pass_kahyani", "referral": "kahyani"},
    "admin_ashrafi": {"password": "pass_ashrafi", "referral": "ashrafi"},
    "admin_etfbaz": {"password": "pass_etfbaz", "referral": "Etfbaz"},
}

REFERRAL_LEVEL_CONFIG: Dict[str, List[str]] = {
    "Etfbaz": ['level_0', 'level_1', 'level_2', 'level_3', 'level_golden'],
    "ashrafi": ['level_0', 'level_1', 'level_2'],
    "kahyani": ['level_1'],
    "_default_": ['level_0']
}

LEVEL_TRANSLATIONS: Dict[str, str] = {
    "level_0": "پایه", "level_1": "سطح ۱", "level_2": "سطح ۲",
    "level_3": "سطح ۳", "level_golden": "طلایی",
    NO_LEVEL_VALUE_INTERNAL: "بدون سطح / نامشخص"
}

REFERRAL_INVITE_LINKS: Dict[str, str] = {
    "Etfbaz": "https://t.me/vip_ganj_bot?start=Etfbaz",
    "ashrafi": "https://t.me/vip_ganj_bot?start=ashrafi",
    "kahyani": "https://t.me/vip_ganj_bot?start=kahyani",
}


class AuthState(rx.State):
    entered_username: str = ""
    entered_password: str = ""
    error_message: str = ""
    is_logged_in: bool = False
    current_logged_in_referral: Optional[str] = None
    current_admin_username: Optional[str] = None

    @rx.var
    def token_is_valid(self) -> bool:
        return self.is_logged_in and bool(self.current_logged_in_referral)

    @rx.var
    def allowed_levels_for_current_referral(self) -> List[str]:
        if self.current_logged_in_referral:
            return REFERRAL_LEVEL_CONFIG.get(self.current_logged_in_referral, REFERRAL_LEVEL_CONFIG.get("_default_", []))
        return REFERRAL_LEVEL_CONFIG.get("_default_", [])

    @rx.var
    def level_options_for_dropdown(self) -> List[Tuple[str, str]]:
        options: List[Tuple[str, str]] = []
        current_allowed_levels = self.allowed_levels_for_current_referral
        for level_val in current_allowed_levels:
            label = LEVEL_TRANSLATIONS.get(level_val, level_val)
            options.append((label, level_val))
        no_level_label = LEVEL_TRANSLATIONS.get(NO_LEVEL_VALUE_INTERNAL, "بدون سطح")
        options.append((no_level_label, NO_LEVEL_VALUE_INTERNAL))
        return options
    
    async def copy_invite_link(self):
        if self.current_logged_in_referral:
            link_to_copy = REFERRAL_INVITE_LINKS.get(self.current_logged_in_referral)
            if link_to_copy:
                # --- تغییر در اینجا: استفاده از yield ---
                yield rx.set_clipboard(link_to_copy)
                yield rx.toast.success("لینک دعوت کپی شد!", position="bottom-right")
                return 
            else:
                yield rx.toast.error("لینک دعوت برای این معرف تعریف نشده.", position="bottom-right")
                return
        yield rx.toast.warning("ابتدا وارد شوید یا خطای نامشخص.", position="bottom-right")


    async def handle_login(self):
        from customer_data.backend.backend import State as MainState

        self.error_message = ""
        admin_user_details = ADMIN_CREDENTIALS.get(self.entered_username)

        if admin_user_details and admin_user_details["password"] == self.entered_password:
            self.is_logged_in = True
            self.current_admin_username = self.entered_username
            self.current_logged_in_referral = admin_user_details["referral"]
            self.entered_username = ""
            self.entered_password = ""
            
            if self.current_logged_in_referral:
                yield MainState.load_entries(active_referral=self.current_logged_in_referral) # type: ignore
            yield rx.redirect("/")
        else:
            self.error_message = "نام کاربری یا رمز عبور نامعتبر است!"
            self.is_logged_in = False
            self.current_logged_in_referral = None
            self.current_admin_username = None

    async def handle_logout(self):
        from customer_data.backend.backend import State as MainState

        self.is_logged_in = False
        self.current_logged_in_referral = None
        self.current_admin_username = None
        self.entered_username = ""
        self.entered_password = ""
        self.error_message = ""
        yield MainState.clear_all_users_data # type: ignore
        yield rx.redirect("/login")

    async def require_login_and_load_data(self):
        from customer_data.backend.backend import State as MainState
        
        if not self.token_is_valid:
            yield rx.redirect("/login")
        else:
            if self.current_logged_in_referral:
                yield MainState.load_entries(active_referral=self.current_logged_in_referral) # type: ignore