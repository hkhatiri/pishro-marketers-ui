import reflex as rx
import bcrypt
from typing import Optional
from ..models.admin_user import AdminUser

class AuthState(rx.State):
    error_message: str = ""
    redirect_to: Optional[str] = None

    # اطلاعات ادمین لاگین کرده
    logged_in_admin_username: Optional[str] = None
    logged_in_admin_referral_type: Optional[str] = None
    is_logged_in_super_admin: bool = False

    @rx.var
    def is_authenticated(self) -> bool:
        return self.logged_in_admin_username is not None

    def _set_admin_session(self, admin: AdminUser):
        self.logged_in_admin_username = admin.username
        self.logged_in_admin_referral_type = admin.referral_type
        self.is_logged_in_super_admin = admin.is_super_admin

    def login(self, form_data: dict):
        username = form_data["username"]
        password = form_data["password"]
        self.error_message = ""

        if not username or not password:
            self.error_message = "نام کاربری و رمز عبور نمی‌توانند خالی باشند."
            return

        with rx.session() as session:
            admin = session.exec(
                AdminUser.select.where(AdminUser.username == username, AdminUser.is_active == True)
            ).first()

            if admin and bcrypt.checkpw(password.encode(), admin.password_hash.encode()):
                self._set_admin_session(admin)
                self.redirect_to = "/dashboard" # یا هر صفحه اصلی دیگری
                return rx.redirect(self.redirect_to) # اضافه شد برای ریدایرکت فوری
            else:
                self.error_message = "نام کاربری یا رمز عبور نامعتبر است."

    def logout(self):
        self.logged_in_admin_username = None
        self.logged_in_admin_referral_type = None
        self.is_logged_in_super_admin = False
        self.redirect_to = "/login"
        return rx.redirect(self.redirect_to)

    # یک تابع برای ایجاد ادمین اولیه (می‌توانید از طریق شل پایتون یا یک اسکریپت جدا اجرا کنید)
    def create_admin_user_once(self, username, password, referral_type, is_super_admin=False):
        # این تابع فقط برای اولین بار یا برای اضافه کردن ادمین ها به صورت دستی استفاده می شود.
        # در محیط پروداکشن، مدیریت ادمین ها باید از طریق پنل یا ابزارهای دیگر انجام شود.
        with rx.session() as session:
            existing_admin = session.exec(
                AdminUser.select.where(AdminUser.username == username)
            ).first()
            if existing_admin:
                print(f"Admin with username '{username}' already exists.")
                return

            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_admin = AdminUser(
                username=username,
                password_hash=hashed_password,
                referral_type=referral_type,
                is_super_admin=is_super_admin,
                is_active=True
            )
            session.add(new_admin)
            session.commit()
            print(f"Admin '{username}' created successfully for referral '{referral_type}'.")

# برای ایجاد ادمین اولیه:
# از شل Reflex استفاده کنید: reflex shell
# سپس:
# from marketers_admin_panel.states.auth_state import AuthState
# state = AuthState()
# state.create_admin_user_once("admin_etfbaz", "your_secure_password", "Etfbaz")
# state.create_admin_user_once("admin_ashrafi", "another_password", "ashrafi")
# state.create_admin_user_once("superadmin", "super_secret_password", "", is_super_admin=True)