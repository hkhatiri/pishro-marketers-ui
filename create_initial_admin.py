import asyncio
import bcrypt
import reflex as rx
import os
import sys

# اضافه کردن مسیر ریشه پروژه به sys.path
current_script_path = os.path.abspath(__file__)
project_root_directory = os.path.dirname(current_script_path)
if project_root_directory not in sys.path:
    sys.path.insert(0, project_root_directory)

# ایمپورت‌ها پس از تنظیم sys.path
# فرض بر این است که rxconfig.py در ریشه پروژه (همان جایی که create_initial_admin.py است) قرار دارد
# و پکیج اپ شما marketers_admin_panel نام دارد
from marketers_admin_panel.models.admin_user import AdminUser
from rxconfig import config as app_config # تغییر نام برای جلوگیری از تداخل احتمالی


def create_admin_sync(username, password, referral_type, is_super_admin=False, is_active=True):
    """یک کاربر ادمین ایجاد یا آپدیت می‌کند."""
    if not (app_config and app_config.db_url):
         print("Fatal: db_url not found in app_config from rxconfig.py. Ensure rxconfig.py is correct and imported.")
         return

    # برای اطمینان از اینکه Reflex context برای rx.session آماده است،
    # می‌توان یک نمونه موقت از App ایجاد کرد.
    # این کار به rx.session کمک می‌کند تا db_url صحیح را پیدا کند.
    # اگرچه در نسخه‌های جدیدتر، ایمپورت کردن rxconfig باید کافی باشد.
    # _ = rx.App(db_url=app_config.db_url) # این خط را فعلا کامنت می‌کنیم، اگر لازم شد برمی‌گردانیم.

    try:
        with rx.session() as session:
            existing_admin = session.exec(
                AdminUser.select().where(AdminUser.username == username) # <<<--- select() با پرانتز
            ).first()

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            if existing_admin:
                print(f"Admin '{username}' already exists. Updating details...")
                existing_admin.password_hash = hashed_password
                existing_admin.referral_type = referral_type
                existing_admin.is_super_admin = is_super_admin
                existing_admin.is_active = is_active
                session.add(existing_admin)
            else:
                new_admin = AdminUser(
                    username=username,
                    password_hash=hashed_password,
                    referral_type=referral_type,
                    is_super_admin=is_super_admin,
                    is_active=is_active
                )
                session.add(new_admin)
            session.commit()
            print(f"Admin '{username}' processed successfully for referral '{referral_type}'.")
    except Exception as e:
        print(f"Error during database session for admin '{username}': {type(e).__name__} - {e}")
        print("Ensure 'reflex db init' and 'reflex db migrate' have been run successfully and tables exist.")


def main_sync():
    # لیست referral ها را با مقادیر واقعی خودتان جایگزین کنید
    # اینها باید کلیدهای دیکشنری self.bot_config در marketers.py بات شما باشند.
    referral_names_from_bot = ['demo', 'Etfbaz', 'ashrafi', 'kahyani'] # مثال

    admins_to_create = [
        {"username": "superadmin", "password": "YOUR_SECURE_PASSWORD_1", "referral_type": "", "is_super_admin": True},
    ]
    for ref_name in referral_names_from_bot:
        admins_to_create.append(
            {"username": f"admin_{ref_name.lower()}", "password": f"pass_{ref_name.lower()}_Secure123!", "referral_type": ref_name}
        )

    print("Creating/Updating admin users...")
    for admin_data in admins_to_create:
        print(f"Processing admin: {admin_data['username']}")
        create_admin_sync(
            username=admin_data["username"],
            password=admin_data["password"], # پسوردهای امن انتخاب کنید
            referral_type=admin_data["referral_type"],
            is_super_admin=admin_data.get("is_super_admin", False)
        )
    print("Admin user creation/update process finished.")

if __name__ == "__main__":
    print("Please ensure you have run 'python -m reflex db init' and 'python -m reflex db migrate' from your terminal first.")
    if not (app_config and app_config.db_url):
        print("Error: Database URL is not configured in rxconfig.py. Cannot run admin creation script.")
        # تلاش برای مقداردهی اولیه موقت اپ برای بارگذاری config
        try:
            print("Attempting to initialize a temporary App to load db_url from rxconfig...")
            temp_app = rx.App() # این ممکن است rxconfig.py را پیدا و db_url را تنظیم کند
            if not temp_app.db_url: # یا از طریق rx.config.get_config().db_url
                print("Failed to load db_url even after temporary App instantiation.")
                sys.exit(1)
            print(f"DB URL seems loaded: {temp_app.db_url}")
            # پس از اینکه db_url لود شد، app_config هم باید مقدار داشته باشد
            # این فرض بر این است که rxconfig.py به درستی app_name و db_url را تعریف کرده است
            # و در مسیر پایتون قرار دارد یا در همان پوشه اسکریپت است.
            # اگر از rxconfig.py مستقیماً ایمپورت شده، باید app_config.db_url مقدار داشته باشد.
        except Exception as e:
            print(f"Error during temporary App instantiation for config loading: {e}")
            sys.exit(1)
            
    main_sync()