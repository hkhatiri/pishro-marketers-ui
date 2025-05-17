# customer_data/components/page_elements.py
import reflex as rx
from ..backend.auth_state import AuthState # مسیر import صحیح است

def page_header_with_actions() -> rx.Component:
    return rx.flex(
        rx.box(), # Placeholder for left-aligned content or title if needed
        rx.spacer(),
        rx.hstack(
            rx.cond(
                AuthState.is_logged_in,
                rx.button(
                    rx.icon("link", size=16, margin_left="0.25em"), # margin_left for RTL
                    "دریافت لینک دعوت",
                    on_click=AuthState.copy_invite_link, # type: ignore
                    variant="soft", color_scheme="blue", size="2", margin_right="1em",
                ),
                rx.fragment() # Empty fragment if not logged in
            ),
            rx.color_mode.button(size="2"),
            rx.cond(
                AuthState.is_logged_in,
                rx.button(
                    rx.icon("log-out", size=18, margin_left="0.25em"), # margin_left for RTL
                     "خروج",
                    on_click=AuthState.handle_logout, # type: ignore
                    color_scheme="red", variant="soft", size="2"
                ),
                rx.fragment() # Empty fragment if not logged in
            ),
            align="center", spacing="3",
        ),
        # --- CHANGE THIS LINE ---
        justify="between", # Changed from "space-between"
        # --- END OF CHANGE ---
        align="center",
        width="100%",
        padding_y="0.75em",
        margin_bottom="1.5em",
    )