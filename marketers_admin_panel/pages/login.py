import reflex as rx
from ..states.auth_state import AuthState

def login_page() -> rx.Component:
    return rx.center(
        rx.card(
            rx.vstack(
                rx.heading("ورود ادمین", size="6", text_align="center", margin_bottom="1em"),
                rx.form.root(
                    rx.vstack(
                        rx.form.field(
                            rx.form.label("نام کاربری", html_for="username_field_id"),
                            rx.input(name="username", id="username_field_id", placeholder="نام کاربری", required=True, width="100%"),
                            name="username_form_field",
                            width="100%"
                        ),
                        rx.form.field(
                            rx.form.label("رمز عبور", html_for="password_field_id"),
                            rx.input(name="password", id="password_field_id", type="password", placeholder="رمز عبور", required=True, width="100%"),
                            name="password_form_field",
                            width="100%"
                        ),
                        rx.cond(
                            AuthState.error_message != "",
                            rx.callout.root(
                                rx.callout.icon(rx.icon(tag="info")), # آیکن معتبر
                                rx.callout.text(AuthState.error_message),
                                color_scheme="red",
                                role="alert",
                                margin_y="1em",
                                width="100%"
                            ),
                            None
                        ),
                        rx.form.submit(
                            rx.button("ورود", type="submit", width="100%"),
                            as_child=True,
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    on_submit=AuthState.login,
                    width="100%",
                ),
                align_items="stretch",
                width="300px",
            ),
            padding="2em",
            style={"direction": "rtl"}
        ),
        height="100vh",
    )