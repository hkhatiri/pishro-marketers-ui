import reflex as rx
from .pages.login import login_page
from .pages.dashboard import dashboard_page
from .states.auth_state import AuthState # برای دسترسی به is_authenticated

# این یک template پایه برای صفحاتی است که نیاز به احراز هویت دارند
def protected_page(page_component_fn):
    def wrapper():
        # اگر کاربر احراز هویت نشده باشد، به صفحه لاگین ریدایرکت کن
        if not AuthState.is_authenticated: # از var استفاده می کنیم
            return rx.redirect("/login", external=False) # external=False برای ریدایرکت داخلی
        return page_component_fn()
    return wrapper

# تعریف صفحات با استفاده از template محافظت شده
@rx.page(route="/dashboard", title="Dashboard")
def protected_dashboard():
    return protected_page(dashboard_page)()

@rx.page(route="/login", title="Login")
def login():
    return login_page()

@rx.page(route="/")
def index():
    # صفحه اصلی، اگر کاربر لاگین کرده به داشبورد برود، در غیر این صورت به لاگین
    if not AuthState.is_authenticated: # از var استفاده می کنیم
        return rx.redirect("/login", external=False)
    return rx.redirect("/dashboard", external=False)


# ایجاد اپلیکیشن
app = rx.App(
    theme=rx.theme(
        appearance="light", # یا "dark"
        accent_color="blue",
        radius="medium"
    )
)
# app.add_page(index) # index الان خودش ریدایرکت میکنه
# app.add_page(login, route="/login") # login_page الان با دکوراتور @rx.page تعریف شده
# app.add_page(protected_dashboard, route="/dashboard") # dashboard_page الان با دکوراتور @rx.page تعریف شده