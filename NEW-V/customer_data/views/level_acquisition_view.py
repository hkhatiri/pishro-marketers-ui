# customer_data/views/level_acquisition_view.py
import reflex as rx
from reflex.components.radix.themes.base import LiteralAccentColor

from ..components.card import card
from ..backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL
from ..backend.backend import State as MainState

LEVEL_COLORS: dict[str, LiteralAccentColor] = {
    "level_0": "gray", "level_1": "blue", "level_2": "orange",
    "level_3": "purple", "level_golden": "amber",
    NO_LEVEL_VALUE_INTERNAL: "gray",
    "_default_": "green"
}
LEVEL_ICONS: dict[str, str] = {
    "level_0": "bar-chart-3", "level_1": "user-check", "level_2": "user-cog",
    "level_3": "users", "level_golden": "gem",
    NO_LEVEL_VALUE_INTERNAL: "minus-circle",
    "_default_": "award"
}

def level_progress_item(level_key: rx.Var[str], user_count: rx.Var[int], total_users_in_referral: rx.Var[int]) -> rx.Component:
    # --- UPDATED SECTION for level_display_name ---
    # If level_key can be None, it's safer to handle it in a @rx.var or ensure it's always a string
    # For now, assuming level_key.to_string() will work if level_key is guaranteed to be a string Var.
    # If level_key itself can be a None Var, then this could be an issue.
    # The list `AuthState.allowed_levels_for_current_referral` should contain strings.
    # The Var passed to `level_k` in `rx.foreach` will be one of those strings.

    # We'll construct the display name using rx.cond if level_key could be tricky,
    # but let's try a simpler approach first assuming level_key.to_string() gives a usable key.
    level_key_as_str = level_key.to_string() # Get the string value of the Var

    # Create a Var for the display name, looking up the translation
    # This logic might be better inside a @rx.var in the State if it gets complex
    # or if LEVEL_TRANSLATIONS needs to be dynamically accessed.
    # For direct use in component, we create a Var from the result of the lookup.
    level_display_name = rx.Var.create(
        LEVEL_TRANSLATIONS.get(level_key_as_str, level_key_as_str.replace("level_", "سطح "))
    )
    # --- END OF UPDATED SECTION ---

    progress_percentage = rx.cond(
        total_users_in_referral > 0,
        (user_count / total_users_in_referral) * 100,
        0
    )
    clamped_progress = rx.cond(progress_percentage < 0, 0, rx.cond(progress_percentage > 100, 100, progress_percentage))

    # --- UPDATED SECTION for icon and color ---
    current_level_key_as_str = level_key.to_string() # Get string value
    icon_to_use = LEVEL_ICONS.get(current_level_key_as_str, LEVEL_ICONS["_default_"])
    color_to_use = LEVEL_COLORS.get(current_level_key_as_str, LEVEL_COLORS["_default_"])
    # --- END OF UPDATED SECTION ---

    return rx.vstack(
        rx.hstack(
            rx.icon(
                icon_to_use,
                size=18,
                color=rx.color(color_to_use, 9), # type: ignore
                margin_left="0.5em"
            ),
            rx.text(level_display_name, size="3", weight="medium", color=rx.color("gray", 11)),
            rx.spacer(),
            rx.text(user_count.to_string() + " کاربر", size="2", color=rx.color("gray", 10)),
            align_items="center",
            width="100%",
        ),
        rx.progress(
            value=clamped_progress,
            color_scheme=color_to_use, # type: ignore
            size="2",
            width="100%",
            margin_top="0.25em",
        ),
        width="100%",
        spacing="1",
    )

def level_acquisition_section() -> rx.Component:
    return card(
        rx.vstack(
            rx.hstack(
                rx.icon("users", size=20, margin_left="0.5em"),
                rx.heading("آمار سطوح کاربران", size="5", weight="medium"),
                align_items="center",
                width="100%",
                margin_bottom="1em",
            ),
            rx.cond(
                AuthState.allowed_levels_for_current_referral.length() > 0,
                rx.foreach(
                    AuthState.allowed_levels_for_current_referral,
                    lambda level_k: rx.cond(
                        (level_k != NO_LEVEL_VALUE_INTERNAL),
                        level_progress_item(
                            level_k, # level_k is an rx.Var[str] from the foreach iteration
                            MainState.user_counts_by_level_var.get(level_k.to_string(), 0), # Use .to_string() for dict key
                            MainState.total_users_for_current_referral
                        ),
                        rx.fragment()
                    )
                ),
                rx.center(rx.text("سطحی برای نمایش تعریف نشده است.", color_scheme="gray"), height="100px")
            ),
            spacing="4",
            width="100%",
            align_items="stretch",
        )
    )