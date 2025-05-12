import reflex as rx
from admin_panel.state import AdminState

def auth_form() -> rx.Component:
    return rx.vstack(
        rx.heading("Admin Login"),
        rx.input(
            placeholder="Username",
            on_change=AdminState.set_username,
            width="300px"
        ),
        rx.input(
            placeholder="Password",
            type_="password",
            on_change=AdminState.set_password,
            width="300px"
        ),
        rx.button("Login", on_click=AdminState.login),
        rx.text(AdminState.error_message, color="red"),
        spacing="4",
        padding="20px",
        align_items="center",
    )