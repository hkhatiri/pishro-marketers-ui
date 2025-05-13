import reflex as rx
from ..states.auth_state import AuthState

def login_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("ورود ادمین", size="6", align="center", margin_bottom="1em"),
                rx.form.root(
                    rx.vstack(
                        rx.form.field(
                            rx.form.label("نام کاربری"),
                            rx.input(name="username", placeholder="نام کاربری", required=True),
                            name="username_field",
                            width="100%"
                        ),
                        rx.form.field(
                            rx.form.label("رمز عبور"),
                            rx.input(name="password", type="password", placeholder="رمز عبور", required=True),
                            name="password_field",
                            width="100%"
                        ),
                        rx.cond(
                            AuthState.error_message,
                            rx.callout(
                                AuthState.error_message,
                                icon="alert_triangle",
                                color_scheme="red",
                                role="alert",
                                margin_y="1em"
                            )
                        ),
                        rx.form.submit(
                            rx.button("ورود", type="submit", width="100%"),
                            as_child=True,
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    on_submit=AuthState.login, # استفاده از login که ریدایرکت هم انجام می‌دهد
                    width="100%",
                ),
                align_items="stretch",
                width="300px",
            ),
            padding="2em"
        ),
        height="100vh",
    )