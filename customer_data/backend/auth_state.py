import reflex as rx
from typing import Optional

# MainState دیگر در سطح بالا import نمی‌شود تا از circular import جلوگیری شود.
# در صورت نیاز، به صورت محلی داخل متدها import خواهد شد.

ADMIN_CREDENTIALS = {
    "admin_kahyani": {"password": "pass_kahyani", "referral": "kahyani"},
    "admin_ashrafi": {"password": "pass_ashrafi", "referral": "ashrafi"},
    "admin_etfbaz": {"password": "pass_etfbaz", "referral": "Etfbaz"},
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

    async def handle_login(self):
        # ایمپورت محلی برای جلوگیری از circular import
        # مسیر باید از ریشه پکیج customer_data شروع شود
        from customer_data.backend.backend import State as MainState

        self.error_message = ""
        admin_user = ADMIN_CREDENTIALS.get(self.entered_username)

        if admin_user and admin_user["password"] == self.entered_password: # رمزها باید هش شوند!
            self.is_logged_in = True
            self.current_logged_in_referral = admin_user["referral"]
            self.current_admin_username = self.entered_username
            self.entered_username = ""
            self.entered_password = ""
            if self.current_logged_in_referral:
                # پاس دادن referral به عنوان آرگومان
                yield MainState.load_entries(active_referral=self.current_logged_in_referral)
            yield rx.redirect("/")
        else:
            self.error_message = "نام کاربری یا رمز عبور نامعتبر است!"
            self.is_logged_in = False
            self.current_logged_in_referral = None
            self.current_admin_username = None

    async def handle_logout(self):
        from customer_data.backend.backend import State as MainState # ایمپورت محلی

        self.is_logged_in = False
        self.current_logged_in_referral = None
        self.current_admin_username = None
        self.entered_username = ""
        self.entered_password = ""
        self.error_message = ""
        yield MainState.clear_all_users_data
        yield rx.redirect("/login")

    async def require_login_and_load_data(self):
        from customer_data.backend.backend import State as MainState # ایمپورت محلی
        
        if not self.token_is_valid:
            yield rx.redirect("/login")
        else:
            if self.current_logged_in_referral:
                yield MainState.load_entries(active_referral=self.current_logged_in_referral)
            else:
                print("--- ERROR: AuthState - Logged in but no referral! Redirecting to login. ---")
                yield rx.redirect("/login")
