import reflex as rx

from .components.stats_cards import stats_cards_group
from .views.navbar import navbar
from .views.table import main_table
from .backend.backend import State as MainState 
from .backend.auth_state import AuthState
from .pages.login_page import login_page # اطمینان از وجود این فایل و کامپوننت


def main_dashboard_content() -> rx.Component:
    return rx.vstack(
        navbar(),
        stats_cards_group(),
        rx.box(
            main_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
        padding_bottom="2em",
    )

# دکوراتور @rx.page از اینجا حذف شد
def index() -> rx.Component:
    return main_dashboard_content()


app = rx.App(
    theme=rx.theme(
        appearance="dark", has_background=True, radius="large", accent_color="grass"
    ),
)

# صفحه اصلی از طریق app.add_page با on_load تعریف می‌شود
app.add_page(
    index,
    route="/",
    title="پنل مدیریت کاربران",
    on_load=AuthState.require_login_and_load_data
)

app.add_page(
    login_page,
    route="/login",
    title="ورود به پنل"
)
