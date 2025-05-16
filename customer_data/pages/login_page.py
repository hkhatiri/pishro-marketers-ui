# customer_data/pages/login_page.py
import reflex as rx
# اطمینان از اینکه AuthState به درستی import شده است
try:
    from ..backend.auth_state import AuthState
except ImportError:
    # Fallback اگر ساختار پوشه متفاوت است یا برای تست مستقیم
    from customer_data.backend.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("ورود به پنل ادمین", size="7", text_align="center", margin_bottom="1em"),
            rx.form.root(
                rx.vstack(
                    rx.form.field(
                        rx.hstack(rx.icon("user", size=18), rx.form.label("نام کاربری ادمین"), align_items="center"),
                        rx.input(
                            placeholder="نام کاربری...",
                            value=AuthState.entered_username,
                            on_change=AuthState.set_entered_username,
                            size="3", width="300px",
                        ),
                        name="username_field", width="100%", align_items="center"
                    ),
                    rx.form.field(
                        rx.hstack(rx.icon("key-round", size=18), rx.form.label("رمز عبور"), align_items="center"),
                        rx.input(
                            placeholder="رمز عبور...",
                            type="password",
                            value=AuthState.entered_password,
                            on_change=AuthState.set_entered_password,
                            size="3", width="300px",
                        ),
                        name="password_field", width="100%", align_items="center"
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.callout.root(
                            rx.callout.icon(rx.icon("shield-alert")), # <--- آیکون معتبر
                            rx.callout.text(AuthState.error_message),
                            color_scheme="red", variant="soft", margin_top="1em", width="300px",
                        ),
                    ),
                    rx.button("ورود", type="submit", size="3", width="300px", margin_top="1em", color_scheme="grass"),
                    align_items="center", spacing="4"
                ),
                on_submit=AuthState.handle_login, width="auto"
            ),
            padding="2em", border_radius="md", box_shadow="lg", bg=rx.color("gray", 2), align_items="center" # رنگ پس‌زمینه کمی تیره‌تر شد
        ),
        height="100vh", width="100%",
        # background="radial-gradient(circle, var(--gray-a3), var(--gray-a1))", # پس‌زمینه گرادیان برای صفحه
    )