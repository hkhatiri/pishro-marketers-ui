import reflex as rx
from .components.login import login_form
from .components.user_list import user_list
from .components.user_details import user_details
from .state import AuthState, UserState

def index():
    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            UserState.selected_user,
            user_details(),
            user_list(),
        ),
        login_form(),
    )

app = rx.App()
app.add_page(index, on_load=UserState.load_users)