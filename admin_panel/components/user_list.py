import reflex as rx
from ..styles import styles
from ..state import AuthState, UserState  # اصلاح import

def user_list():
    return rx.vstack(
        rx.heading(f"کاربران با رفرال {UserState.referral}"),
        rx.cond(
            UserState.loading,
            rx.text("در حال بارگذاری..."),
            rx.table(
                headers=["شناسه", "کدملی", "نام کاربری", "سطح", "وضعیت", "تعداد کانال‌ها", "عملیات"],
                rows=[
                    [
                        user["user_id"],
                        user["national_id"],
                        user["username"],
                        user["level"],
                        user["chat_state"],
                        user["joined_count"],
                        rx.button(
                            "مشاهده",
                            on_click=lambda: UserState.select_user(user["user_id"]),
                            style=styles["button"],
                        ),
                    ]
                    for user in UserState.users
                ],
                width="100%",
            ),
        ),
        rx.button(
            "خروج",
            on_click=AuthState.logout,
            style=styles["danger_button"],
        ),
        spacing="4",
        style=styles["container"],
    )