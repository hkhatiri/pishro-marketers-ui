import reflex as rx
import bcrypt
from typing import Optional
from ..models.admin_user import AdminUser # مسیر صحیح

class AuthState(rx.State):
    error_message: str = ""
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
        self.error_message = ""

    def login(self, form_data: dict):
        username = form_data.get("username", "").strip()
        password = form_data.get("password", "")
        self.error_message = ""

        if not username or not password:
            self.error_message = "نام کاربری و رمز عبور نمی‌توانند خالی باشند."
            return

        with rx.session() as session:
            admin = session.exec(
                AdminUser.select.where(AdminUser.username == username, AdminUser.is_active == True)
            ).first()

            if admin and admin.password_hash and bcrypt.checkpw(password.encode('utf-8'), admin.password_hash.encode('utf-8')):
                self._set_admin_session(admin)
                return rx.redirect("/dashboard")
            else:
                self.error_message = "نام کاربری یا رمز عبور نامعتبر است یا حساب کاربری غیرفعال است."
                return

    def logout(self):
        self.logged_in_admin_username = None
        self.logged_in_admin_referral_type = None
        self.is_logged_in_super_admin = False
        return rx.redirect("/login")

    def create_admin_user_once(self, username, password, referral_type, is_super_admin=False):
        # این تابع فقط برای اولین بار یا برای اضافه کردن ادمین ها به صورت دستی استفاده می شود.
        with rx.session() as session:
            existing_admin = session.exec(
                AdminUser.select.where(AdminUser.username == username)
            ).first()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            if existing_admin:
                print(f"Admin '{username}' already exists. Updating details...")
                existing_admin.password_hash = hashed_password
                existing_admin.referral_type = referral_type
                existing_admin.is_super_admin = is_super_admin
                existing_admin.is_active = True
                session.add(existing_admin)
            else:
                new_admin = AdminUser(
                    username=username,
                    password_hash=hashed_password,
                    referral_type=referral_type,
                    is_super_admin=is_super_admin,
                    is_active=True
                )
                session.add(new_admin)
                print(f"Admin '{username}' created for referral '{referral_type}'.")
            session.commit()