# customer_data_app/customer_data/views/navbar.py
import reflex as rx
from ..backend.auth_state import AuthState # ایمپورت AuthState

def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="table-2", size=28),
            rx.heading("پنل کاربران", size="6", style={"direction": "rtl"}), # عنوان فارسی
            color_scheme="green",
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        rx.spacer(),
        rx.hstack(
            # نمایش کد معرف لاگین شده اگر کاربر لاگین است
            rx.cond(
                AuthState.is_logged_in,
                rx.text(
                    "کد معرف: ",
                    rx.code(AuthState.current_logged_in_referral),
                    margin_right="1em",
                    size="3"
                )
            ),
            rx.logo(),
            rx.color_mode.button(),
            # دکمه خروج فقط زمانی نمایش داده شود که کاربر لاگین کرده باشد
            rx.cond(
                AuthState.is_logged_in,
                rx.button(
                    rx.icon("log-out", size=18),
                    "خروج",
                    on_click=AuthState.handle_logout,
                    color_scheme="red",
                    variant="soft",
                    size="2"
                ),
                None # اگر لاگین نکرده، دکمه خروج نمایش داده نشود
            ),
            align="center",
            spacing="3",
        ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="1em", # کاهش padding برای هماهنگی با صفحه لاگین
        padding_bottom="1em",
        padding_x="1.5em",
        border_bottom="1px solid var(--gray-a5)", # اضافه کردن یک خط جداکننده
        bg=rx.color("gray", 2), # پس‌زمینه مشابه صفحه لاگین
        position="sticky", # برای چسبیدن به بالا
        z_index="10", # برای قرار گرفتن روی محتوا
    )