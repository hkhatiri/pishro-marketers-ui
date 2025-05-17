# customer_data/customer_data.py
import reflex as rx

# Import states first
from .backend.auth_state import AuthState
from .backend.backend import State as MainState
from .templates import ThemeState

# Import styles and template system
from . import styles
from .templates import template

# Import page components (that use @template or @rx.page)
from .pages.login_page import login_page
from .pages.index import index
from .pages.table import table_page # <--- IMPORT THE NEW TABLE PAGE

from .components.page_elements import page_header_with_actions

app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
)
