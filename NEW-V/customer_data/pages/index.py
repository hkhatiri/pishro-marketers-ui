# customer_data/pages/index.py
"""The overview page of the app."""
import reflex as rx

from ..templates import template
from ..backend.auth_state import AuthState
from ..backend.backend import State as MainState

from ..components.stats_cards import stats_cards_group
from ..views.visitor_analytics_view import visitors_analytics_section
from ..views.level_acquisition_view import level_acquisition_section
# --- CHANGE THIS IMPORT ---
from ..components.page_elements import page_header_with_actions # Import from the new location

@template(route="/", title="داشبورد مدیریت کاربران", on_load=[AuthState.require_login_and_load_data, MainState.load_entries]) # type: ignore
def index() -> rx.Component:
    """The overview page."""
    return rx.vstack(
        page_header_with_actions(),
        stats_cards_group(),
        rx.grid(
            visitors_analytics_section(),
            level_acquisition_section(),
            # --- CHANGE THIS SECTION ---
            columns={
                "initial": "1", # یا 1 (integer string)
                "sm": "1",
                "md": "1",
                "lg": "2",
                "xl": "2",
            },
            # --- END OF CHANGE ---
            spacing="5", # This was likely meant to be 'gap'
            width="100%",
            gap="1.5em",
            margin_top="1.5em",
        ),
        spacing="5",
        width="100%",
        align_items="stretch",
    )