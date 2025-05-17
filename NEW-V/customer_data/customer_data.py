# customer_data/customer_data.py
import reflex as rx

# Import states first
from .backend.auth_state import AuthState
from .backend.backend import State as MainState
from .templates import ThemeState # Import ThemeState

# Import styles and template system
from . import styles
from .templates import template

# Import page components (that use @template or @rx.page)
from .pages.login_page import login_page # Does not use main template
from .pages.index import index # Uses main template

# Import components used by the template or pages directly in this file
# from .components.sidebar import sidebar_component # Already imported in template.py
# from .components.navbar import navbar_component   # Already imported in template.py
# from .components.stats_cards import stats_cards_group # Used in pages.index
from .components.page_elements import page_header_with_actions # Moved here


app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    # theme is now handled by @template for pages using it
)

# Add pages.
# Pages decorated with @template (like 'index') or @rx.page (like 'login_page')
# and their routes are automatically discovered if the modules are imported.
# So, direct app.add_page is often not needed for them here.
# For login_page, ensure it has @rx.page(route="/login", title="...")
# or if it's a simple function, you might need to add it like this:
# app.add_page(login_page, route="/login", title="ورود به پنل")
# However, since your login_page.py likely uses @rx.page, just importing it
# along with pages.index should be enough for Reflex to find them.

# State ها به طور خودکار شناسایی می‌شوند و نیازی به app.add_state نیست.