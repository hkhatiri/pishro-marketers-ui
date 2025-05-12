import reflex as rx
from admin_panel.state import AdminState

def add_admin_form() -> rx.Component:
    return rx.vstack(
        rx.heading("Add New Admin"),
        rx.input(
            placeholder="New Admin Username",
            on_change=AdminState.set_new_admin_username,
            width="300px"
        ),
        rx.input(
            placeholder="New Admin Password",
            type_="password",
            on_change=AdminState.set_new_admin_password,
            width="300px"
        ),
        rx.select(
            options=AdminState.valid_referrals,
            placeholder="Select Referral",
            on_change=AdminState.set_new_admin_referral,
            width="300px"
        ),
        rx.button("Add Admin", on_click=AdminState.add_admin),
        spacing="4",
        padding="20px",
        align_items="center",
    )