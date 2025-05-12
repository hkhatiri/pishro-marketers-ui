import reflex as rx
from admin_panel.state import AdminState
from admin_panel.components.user_table import user_table
from admin_panel.components.auth import auth_form
from admin_panel.components.add_admin import add_admin_form

def index() -> rx.Component:
    return rx.cond(
        AdminState.is_authenticated,
        rx.vstack(
            rx.hstack(
                rx.text(f"Logged in as {AdminState.username} (Referral: {AdminState.referral})"),
                rx.button("Logout", on_click=AdminState.logout, color="red"),
                spacing="4",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Search by national_id or username",
                    on_change=AdminState.set_search_query,
                    width="300px"
                ),
                rx.button("Search", on_click=AdminState.search_users),
                rx.button("Refresh", on_click=AdminState.load_users),
                spacing="4",
            ),
            user_table(),
            add_admin_form(),
            rx.text(AdminState.error_message, color="red"),
            spacing="6",
            padding="20px",
            width="100%",
        ),
        auth_form(),
    )

app = rx.App()
app.add_page(index, title="Admin Panel")