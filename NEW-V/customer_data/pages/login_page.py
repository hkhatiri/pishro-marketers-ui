# customer_data/pages/login_page.py
import reflex as rx

try:
    from ..backend.auth_state import AuthState
except ImportError:
    # Fallback اگر ساختار پوشه متفاوت است یا برای تست مستقیم
    # این فال‌بک در زمان اجرا توسط Reflex و با ساختار صحیح پوشه، نباید استفاده شود.
    from customer_data.backend.auth_state import AuthState # type: ignore


@rx.page(route="/login", title="ورود به پنل ادمین")
def login_page() -> rx.Component:
    """UI for the login page."""
    return rx.center(
        rx.vstack(
            rx.heading("ورود به پنل ادمین", size="7", text_align="center", margin_bottom="1.5em"), # Increased margin
            rx.form.root(
                rx.vstack(
                    rx.form.field(
                        rx.hstack(
                            rx.icon("user", size=18, margin_left="0.25em"), # margin_left for RTL
                            rx.form.label("نام کاربری ادمین", margin_bottom="0.25em"), # Added margin
                            align_items="center",
                        ),
                        rx.input(
                            placeholder="نام کاربری...",
                            value=AuthState.entered_username,
                            on_change=AuthState.set_entered_username,
                            size="3",
                            width="320px", # Increased width slightly
                            text_align="right", # Align text to right for RTL input
                        ),
                        name="username_field", # Name for the form field itself
                        width="100%",
                        align_items="stretch", # Ensure label and input align well vertically
                        spacing="1", # Reduced spacing in field
                    ),
                    rx.form.field(
                        rx.hstack(
                            rx.icon("key-round", size=18, margin_left="0.25em"), # margin_left for RTL
                            rx.form.label("رمز عبور", margin_bottom="0.25em"), # Added margin
                            align_items="center",
                        ),
                        rx.input(
                            placeholder="رمز عبور...",
                            type="password",
                            value=AuthState.entered_password,
                            on_change=AuthState.set_entered_password,
                            size="3",
                            width="320px", # Increased width slightly
                            text_align="right", # Align text to right for RTL input
                        ),
                        name="password_field", # Name for the form field itself
                        width="100%",
                        align_items="stretch",
                        spacing="1",
                    ),
                    rx.cond(
                        AuthState.error_message != "",
                        rx.callout.root(
                            rx.callout.icon(rx.icon("shield-alert", margin_left="0.3em")), # margin_left for RTL
                            rx.callout.text(AuthState.error_message),
                            color_scheme="red",
                            variant="soft",
                            margin_top="1em",
                            width="320px",
                        ),
                        rx.fragment() # Else, render nothing
                    ),
                    rx.button(
                        "ورود",
                        type="submit",
                        size="3",
                        width="320px",
                        margin_top="1.5em", # Increased margin
                        color_scheme="grass",
                    ),
                    align_items="center", # Center items in vstack
                    spacing="4", # Spacing between form elements
                ),
                on_submit=AuthState.handle_login, # type: ignore
                width="auto", # Let the vstack determine the width
                # style={"direction": "rtl"} # This might be inherited from base_style
            ),
            padding="2.5em", # Increased padding
            border_radius="var(--radius-4)", # Use theme radius variable
            box_shadow="var(--shadow-4)", # Use theme shadow variable
            bg=rx.color("gray", 2), # Background color from theme
            align_items="center",
        ),
        height="100vh",
        width="100%",
        # Optional: Add a subtle background pattern or gradient
        # background="url('/bg-pattern.svg')", # Example
        # bg=rx.color("gray",1) # If you want a plain background from theme
    )