import reflex as rx
from ..styles import styles
from ..state import UserState  # احتمالاً درست است، اما چک می‌کنیم
from datetime import datetime

def user_details():
    return rx.cond(
        UserState.selected_user,
        rx.vstack(
            rx.heading(f"جزئیات کاربر {UserState.selected_user['user_id']}"),
            rx.box(
                rx.text(f"کدملی: {UserState.selected_user['national_id']}"),
                rx.text(f"نام کاربری: {UserState.selected_user['username']}"),
                rx.text(f"سطح: {UserState.selected_user['level']}"),
                rx.text(f"وضعیت: {UserState.selected_user['chat_state']}"),
                rx.text(f"تعداد کانال‌ها: {UserState.selected_user['joined_count']}"),
                rx.text(f"کانال‌ها: {', '.join(map(str, UserState.selected_user['channels']))}"),
                rx.text(f"زمان ایجاد: {datetime.fromtimestamp(UserState.selected_user['created_at'])}"),
                rx.text(f"آخرین بررسی سطح: {datetime.fromtimestamp(UserState.selected_user['level_checked_at'])}"),
                style=styles["card"],
            ),
            rx.hstack(
                rx.button(
                    "حذف کاربر",
                    on_click=lambda: UserState.delete_user(UserState.selected_user["user_id"]),
                    style=styles["danger_button"],
                ),
                rx.button(
                    "بازگشت",
                    on_click=lambda: UserState.set_selected_user(None),
                    style=styles["button"],
                ),
            ),
            spacing="4",
            style=styles["container"],
        ),
    )