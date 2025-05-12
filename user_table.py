import reflex as rx
from admin_panel.state import AdminState

def user_table() -> rx.Component:
    return rx.table(
        headers=["User ID", "National ID", "Username", "Chat State", "Level", "Referral", "Actions"],
        rows=[
            [
                rx.text(user["user_id"]),
                rx.text(user.get("national_id", "-")),
                rx.text(user.get("username", "-")),
                rx.text(user.get("chat_state", "-")),
                rx.text(user.get("level", "-")),
                rx.text(user.get("referral", "-")),
                rx.button("Delete", color="red", on_click=lambda: AdminState.delete_user(user["user_id"])),
            ]
            for user in AdminState.users
        ],
        width="100%",
    )