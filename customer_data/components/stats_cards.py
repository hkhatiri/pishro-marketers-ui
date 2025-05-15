import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
from typing import Union
# State اصلی را برای دسترسی به var ها import می‌کنیم
# مسیر import باید با ساختار پروژه شما مطابقت داشته باشد
try:
    from ..backend.backend import State as MainState
except ImportError:
    try:
        from customer_data.backend.backend import State as MainState
    except ImportError:
        # Mock State برای جلوگیری از خطای کامل برنامه در صورت مشکل import
        class MainState(rx.State): # type: ignore
            class MockMonthValues(rx.Base):
                num_customers: int = 0
            current_month_values: MockMonthValues = MockMonthValues()
            previous_month_values: MockMonthValues = MockMonthValues()
            
            @rx.var
            def total_users_for_current_referral(self) -> int: return 0
            @rx.var
            def customers_change(self) -> float: return 0.0


def _arrow_badge(arrow_icon: rx.Var[str], percentage_change: rx.Var[float], arrow_color: rx.Var[str]):
    # --- اصلاح شده: حذف آرگومان decimals از to_string() ---
    change_text = percentage_change.to_string() + "%" 
    return rx.badge(
        rx.icon(tag=arrow_icon, color=rx.color(arrow_color, 9)),
        rx.text(change_text, size="2", color=rx.color(arrow_color, 9), weight="medium"),
        color_scheme=arrow_color, radius="large", align_items="center",
    )


def stats_card(
    stat_name: str,
    value: rx.Var[Union[int, float]], 
    prev_value: rx.Var[Union[int, float]], 
    percentage_change: rx.Var[float], 
    icon: str,
    icon_color: LiteralAccentColor,
    extra_char: str = "",
) -> rx.Component:
    
    cond_prev_value_not_zero = prev_value != 0 
    cond_percentage_not_inf = percentage_change != float("inf")
    cond_percentage_not_neg_inf = percentage_change != -float("inf")
    
    show_arrow_badge_condition = cond_prev_value_not_zero & cond_percentage_not_inf & cond_percentage_not_neg_inf

    cond_value_ge_prev = value >= prev_value

    return rx.card(
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.hstack(
                        rx.icon(tag=icon, size=22, color=rx.color(icon_color, 11)),
                        rx.text(stat_name, size="4", weight="medium", color=rx.color("gray", 11)),
                        spacing="2", align="center",
                    ),
                    rx.cond( 
                        show_arrow_badge_condition,
                         _arrow_badge(
                            rx.cond(cond_value_ge_prev, "trending-up", "trending-down"),
                            percentage_change, 
                            rx.cond(cond_value_ge_prev, "grass", "tomato")
                        ),
                        rx.text("") 
                    ),
                    justify="between", width="100%",
                ),
                rx.hstack(
                    rx.heading(extra_char + value.to_string(), size="7", weight="bold"),
                    rx.cond(
                        cond_prev_value_not_zero, 
                        rx.text("از " + extra_char + prev_value.to_string(), size="3", color=rx.color("gray", 10)),
                        rx.text(""),
                    ),
                    spacing="2", align_items="end",
                ),
                align_items="start", justify="between", width="100%",
            ),
            align_items="start", width="100%", justify="between",
        ),
        size="3", width="100%", max_width="22rem",
    )


def stats_cards_group() -> rx.Component:
    """گروه کارت‌های آمار."""
    return rx.flex(
        stats_card(
            "تعداد کل کاربران معرف", 
            MainState.total_users_for_current_referral,
            MainState.previous_month_values.num_customers, 
            MainState.customers_change,
            "users", "blue",
        ),
        spacing="5", width="100%", wrap="wrap", justify_content="center",
    )
