# customer_data/pages/table.py
import reflex as rx

from ..templates import template # Import the main template
from ..backend.auth_state import AuthState
from ..backend.backend import State as MainState # If table data loading is tied to it
from ..views.table import main_table # Your existing view for the table content
from ..components.page_elements import page_header_with_actions # The common page header

@template(route="/table", title="جدول کاربران", on_load=AuthState.require_login_and_load_data)
def table_page() -> rx.Component: # Renamed function to avoid conflict if you have 'table' elsewhere
    """The table page.
    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        page_header_with_actions(), # The same header as the index page
        rx.heading("لیست کاربران", size="6", margin_bottom="1em", text_align="right"), # Page specific heading
        main_table(), # Your existing table component from views.table
        spacing="5",
        width="100%",
        align_items="stretch",
    )