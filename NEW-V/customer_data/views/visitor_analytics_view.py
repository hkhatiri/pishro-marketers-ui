# customer_data/views/visitor_analytics_view.py
import reflex as rx
from ..components.card import card
from ..backend.backend import State as MainState # MainState شما
from ..backend.auth_state import LEVEL_TRANSLATIONS # برای نام سطوح

# تابع کمکی برای ایجاد نمودار دایره‌ای (مشابه قبل، با کمی تغییرات احتمالی در ظاهر)
def _pie_chart_component(data_var: rx.Var[list[dict]], chart_id: str, title: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="4", weight="medium", align="center", margin_bottom="0.5em"),
        rx.recharts.pie_chart(
            rx.recharts.pie(
                data=data_var,
                data_key="value",
                name_key="name",
                cx="50%",
                cy="45%",
                padding_angle=1,
                inner_radius="50%",
                outer_radius="80%",
                label_line=False,
            ),
            rx.recharts.legend(
                icon_size=10,
                layout="horizontal",
                vertical_align="bottom",
                align="center",
                wrapper_style={"paddingTop": "10px"}
            ),
            rx.recharts.graphing_tooltip(cursor={"fill": "var(--gray-a4)"}), # کمی تغییر رنگ هاور
            height=320, # ارتفاع را کمی تنظیم کردم
            width="100%",
        ),
        width="100%",
        align_items="center", # مرکز کردن نمودار و عنوانش
    )

def visitors_analytics_section() -> rx.Component:
    return card(
        rx.vstack(
            rx.hstack(
                rx.icon("pie-chart", size=20, margin_left="0.5em"),
                rx.heading("تحلیل آماری کاربران", size="5", weight="medium"), # عنوان کلی بخش
                align_items="center",
                width="100%",
                margin_bottom="1em",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("بر اساس سطح", value="levels"),
                    rx.tabs.trigger("وضعیت کلی کاربران", value="all_user_status"),
                    rx.tabs.trigger("وضعیت اعضای کانال", value="channel_member_status"),
                    width="100%",
                    justify_content="center", # یا "start" اگر می‌خواهید از راست شروع شود
                    size="2", # اندازه تب‌ها
                ),
                # تب ۱: آمار بر اساس سطح (مشابه قبل)
                rx.tabs.content(
                    _pie_chart_component(
                        MainState.user_levels_pie_data, # type: ignore
                        "levelsPie",
                        "تفکیک کاربران بر اساس سطح"
                    ),
                    value="levels",
                    padding_top="1.5em",
                ),
                # تب ۲: آمار وضعیت کلی کاربران
                rx.tabs.content(
                    _pie_chart_component(
                        MainState.user_chat_state_pie_data, # type: ignore
                        "allUserStatusPie",
                        "تفکیک وضعیت کلی کاربران"
                    ),
                    value="all_user_status",
                    padding_top="1.5em",
                ),
                # تب ۳: آمار وضعیت اعضای کانال
                rx.tabs.content(
                    _pie_chart_component(
                        MainState.channel_members_chat_state_pie_data, # type: ignore
                        "channelMemberStatusPie",
                        "تفکیک وضعیت اعضای کانال‌ها"
                    ),
                    value="channel_member_status",
                    padding_top="1.5em",
                ),
                default_value="levels", # تب پیش‌فرض فعال
                width="100%",
            ),
            spacing="4",
            width="100%",
            align_items="stretch",
        )
    )