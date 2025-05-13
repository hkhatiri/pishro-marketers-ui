import reflex as rx
from ..styles import styles
from state import *
def login_form():
    return rx.vstack(
        rx.heading("ورود به پنل مدیریتی"),
        rx.input(
            placeholder="نام کاربری (مراجعه‌کننده)",
            on_change=AuthState.set_username,
            width="100%",
        ),
        rx.input(
            placeholder="رمز عبور",
            type_="password",
            on_change=AuthState.set_password,
            width="100%",
        ),
        rx.button(
            "ورود",
            on_click=AuthState.login,
            style=styles["button"],
        ),
        rx.cond(
            AuthState.error_message,
            rx.text(AuthState.error_message, color="red"),
        ),
        spacing="4",
        width="300px",
        align_items="center",
        justify_content="center",
        height="100vh",
    )