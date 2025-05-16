# customer_data/views/navbar.py
import reflex as rx
from ..backend.auth_state import AuthState # ایمپورت AuthState

def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("پنل کاربران", size="6", style={"direction": "rtl"}),
            color_scheme="green", radius="large", align="center",
            variant="surface", padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            # --- تغییر نمایش کد معرف به لینک دعوت ---
            rx.cond(
                AuthState.is_logged_in,
                rx.button( # استفاده از دکمه برای ظاهر بهتر و قابلیت کلیک
                    rx.icon("link", size=16, margin_right="0.25em"), # آیکون لینک
                    "دریافت لینک دعوت",
                    on_click=AuthState.copy_invite_link, # فراخوانی event handler
                    variant="soft", # یا "outline" یا "ghost"
                    color_scheme="blue", # رنگ دلخواه
                    size="2",
                    margin_right="1em",
                ),
                rx.text("") # اگر لاگین نکرده، چیزی نمایش نده
            ),
            # rx.logo(), # اگر می‌خواهید لوگو را نگه دارید
            rx.color_mode.button(size="2"),
            rx.cond(
                AuthState.is_logged_in,
                rx.button(
                    rx.icon("log-out", size=18), "خروج",
                    on_click=AuthState.handle_logout,
                    color_scheme="red", variant="soft", size="2"
                ),
            ),
            align="center", spacing="3",
        ),
        spacing="2", flex_direction=["column", "column", "row"],
        align="center", width="100%", top="0px",
        padding_top="1em", padding_bottom="1em", padding_x="1.5em",
        border_bottom="1px solid var(--gray-a5)",
        bg=rx.color("gray", 1) # پس‌زمینه navbar برای تمایز
    )