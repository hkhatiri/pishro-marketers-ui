# customer_data/components/stats_cards.py
import reflex as rx
from reflex.components.radix.themes.base import (
    LiteralAccentColor,
)
from typing import Union, List, Optional, Tuple

try:
    from ..backend.backend import State as MainState
    from ..backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL
except ImportError:
    # فال‌بک‌ها
    from customer_data.backend.backend import State as MainState # type: ignore
    from customer_data.backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL # type: ignore


# ... (توابع _build_trend_badge_display و _build_prev_value_text_display و stats_card بدون تغییر از نسخه قبلی که کار می‌کرد) ...
def _build_trend_badge_display(
    percentage_change_opt: Optional[rx.Var[float]],
    trend_icon_cond_opt: Optional[rx.Var[bool]]
) -> rx.Component:
    if percentage_change_opt is not None and trend_icon_cond_opt is not None:
        condition = percentage_change_opt.is_not_none() & trend_icon_cond_opt.is_not_none()
        
        arrow_icon = rx.cond(trend_icon_cond_opt, "trending-up", "trending-down")
        arrow_color = rx.cond(trend_icon_cond_opt, "grass", "tomato")
        
        badge_content = rx.badge(
            rx.icon(tag=arrow_icon, color=rx.color(arrow_color, 9)), # type: ignore
            rx.text(percentage_change_opt.to_string() + "%", size="2", weight="bold"),
            radius="full", padding_x="0.65rem", padding_y="0.2rem",
            color_scheme=arrow_color, variant="soft" # type: ignore
        )
        return rx.cond(condition, badge_content, rx.text(""))
    return rx.text("")

def _build_prev_value_text_display(
    prev_value_opt: Optional[rx.Var[Union[int, float]]],
    unit_char: str
) -> rx.Component:
    if prev_value_opt is not None:
        condition = prev_value_opt.is_not_none()
        text_content = rx.text(
            "از " + prev_value_opt.to_string() + unit_char,
            size="3", color=rx.color("gray", 10)
        )
        return rx.cond(condition, text_content, rx.text(""))
    return rx.text("")

def stats_card(
    stat_name: Union[str, rx.Var[str]],
    value: rx.Var[Union[int, float]],
    prev_value: Optional[rx.Var[Union[int, float]]] = None,
    percentage_change: Optional[rx.Var[float]] = None,
    trend_icon_cond: Optional[rx.Var[bool]] = None,
    unit: str = "",
    main_icon: Union[str, rx.Var[str]] = "bar-chart-big",
    main_icon_bg_color: Union[LiteralAccentColor, rx.Var[LiteralAccentColor]] = "gray",
) -> rx.Component:
    extra_char = " " + unit if unit else ""
    trend_badge_element = _build_trend_badge_display(percentage_change, trend_icon_cond)
    prev_value_text_element = _build_prev_value_text_display(prev_value, extra_char)

    return rx.card(
        rx.flex(
            rx.badge(
                rx.icon(tag=main_icon, size=28, color=rx.color(main_icon_bg_color, 11)), # type: ignore
                radius="full", padding="0.65rem", color_scheme=main_icon_bg_color, # type: ignore
                variant="surface", high_contrast=True,
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(stat_name, size="3", weight="medium", color=rx.color("gray", 11)),
                    rx.spacer(),
                    trend_badge_element,
                    justify="between", width="100%",
                ),
                rx.hstack(
                    rx.heading(value.to_string() + extra_char, size="7", weight="bold"),
                    prev_value_text_element,
                    spacing="2", align_items="end",
                ),
                align_items="start", justify="between", width="100%",
            ),
            align_items="start", width="100%", justify="between", spacing="4"
        ),
        size="3", width="100%", style={"height": "100%"}
    )


def stats_cards_group() -> rx.Component:
    all_users_card = stats_card(
        stat_name="تعداد کل کاربران شما",
        value=MainState.total_users_for_current_referral,
        unit="کاربر", main_icon="users", main_icon_bg_color="grass",
    )

    users_in_channels_stat_card = stats_card(
        stat_name="کاربران عضو کانال",
        value=MainState.users_in_channels_count_var,
        unit="نفر",
        main_icon="rss",
        main_icon_bg_color="cyan",
    )

    # --- REMOVE OR COMMENT OUT THIS SECTION ---
    # level_cards_display_section = rx.foreach(
    #     AuthState.allowed_levels_for_current_referral,
    #     lambda level_key: rx.cond(
    #         level_key != NO_LEVEL_VALUE_INTERNAL,
    #         stats_card(
    #             stat_name=rx.Var.create(LEVEL_TRANSLATIONS.get(level_key, level_key.replace("level_", "سطح "))), # type: ignore
    #             value=MainState.user_counts_by_level_var.get(level_key.to_string(), 0), # type: ignore
    #             unit="کاربر",
    #             main_icon=rx.cond(level_key == "level_1", "user-round-check",  # type: ignore
    #                         rx.cond(level_key == "level_2", "user-round-cog",  # type: ignore
    #                         rx.cond(level_key == "level_golden", "gem", "award"))), # type: ignore
    #             main_icon_bg_color=rx.cond(level_key == "level_1", "blue",  # type: ignore
    #                                 rx.cond(level_key == "level_2", "orange",  # type: ignore
    #                                 rx.cond(level_key == "level_golden", "yellow", "purple"))), # type: ignore
    #         ),
    #         rx.fragment()
    #     )
    # )
    # --- END OF REMOVAL ---

    return rx.grid(
        all_users_card,
        users_in_channels_stat_card,
        # level_cards_display_section, # This is now removed
        columns={"initial": "1", "sm": "2"}, # Adjust columns as needed
        spacing="3", width="100%", align_items="stretch", padding_y="0.5em",
    )