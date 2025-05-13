import reflex as rx

from .pages.login import login_page
from .pages.dashboard import dashboard_page
from .states.auth_state import AuthState
from .states.admin_state import AdminState


@rx.page(route="/", title="Home - Redirecting")
def index() -> rx.Component:
    return rx.redirect(path="/dashboard")

@rx.page(route="/login", title="Admin Login")
def login() -> rx.Component:
    return login_page()

@rx.page(route="/dashboard", title="Admin Dashboard", on_load=AdminState.on_dashboard_load)
def dashboard() -> rx.Component:
    return dashboard_page()

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="sky",
        radius="medium",
        panel_background="solid",
        style={"direction": "rtl"}
    )
)