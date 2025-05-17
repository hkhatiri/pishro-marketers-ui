# customer_data/components/sidebar.py
"""Sidebar component for the app."""
import reflex as rx
from .. import styles
# from ..templates.template import ALL_PAGES # Not using ALL_PAGES for now for simplicity

def sidebar_header() -> rx.Component:
    """Sidebar header."""
    return rx.hstack(
        rx.color_mode_cond(
            rx.image(src="/reflex_black.svg", height="1.5em"),
            rx.image(src="/reflex_white.svg", height="1.5em"),
        ),
        rx.spacer(),
        # Example: Link to your project's source or docs
        # rx.link(
        #     rx.icon("github", size=24),
        #     href="#",
        #     color_scheme="gray",
        #     is_external=True,
        # ),
        align="center",
        width="100%",
        padding_x="0.35em",
        margin_bottom="1em",
    )

def sidebar_footer() -> rx.Component:
    """Sidebar footer."""
    return rx.hstack(
        rx.link(
            rx.text("راهنما", size="3"),
            href="#", # Link to your help/docs
            color_scheme="gray",
            underline="hover",
        ),
        rx.spacer(),
        rx.color_mode.button(opacity=0.8, size="2"),
        justify="start",
        align="center",
        width="100%",
        padding="0.35em",
    )

def sidebar_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=18, margin_left="0.5em") # margin_left for RTL

def sidebar_item(text: str, url: str, icon_name: str) -> rx.Component:
    """Sidebar item."""
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & (url == "/")
    )
    return rx.link(
        rx.hstack(
            rx.text(text, size="3", weight="medium"), # Text first for RTL
            rx.spacer(), # Pushes icon to the left
            sidebar_item_icon(icon_name),
            bg=rx.cond(active, styles.accent_bg_color, "transparent"),
            color=rx.cond(active, styles.accent_text_color, styles.text_color),
            style={
                "_hover": {
                    "background_color": styles.accent_bg_color,
                    "color": styles.accent_text_color,
                    "opacity": "1",
                },
                "opacity": rx.cond(active, "1","0.85"),
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            padding_y="0.5em",
            padding_x="0.75em",
        ),
        href=url,
        width="100%",
        underline="none",
    )

def sidebar_component() -> rx.Component:
    """The sidebar."""
    project_pages = [
        {"title": "داشبورد اصلی", "route": "/", "icon": "layout-dashboard"},
        {"title": "جدول کاربران", "route": "/table", "icon": "table-2"},
        # Add other pages as they are created
        # {"title": "پروفایل", "route": "/profile", "icon": "user"},
        # {"title": "تنظیمات", "route": "/settings", "icon": "settings"},
        # {"title": "درباره ما", "route": "/about", "icon": "book-open"},
    ]
    return rx.flex(
        rx.vstack(
            sidebar_header(),
            rx.vstack(
                *[
                    sidebar_item(
                        text=page["title"],
                        url=page["route"],
                        icon_name=page["icon"],
                    )
                    for page in project_pages
                ],
                spacing="2",
                width="100%",
                align_items="stretch",
            ),
            rx.spacer(),
            sidebar_footer(),
            width=styles.sidebar_content_width,
            height="100dvh",
            padding="1em",
            bg=rx.color("gray", 2),
            border_left=styles.border, # border_left for RTL
        ),
        display=["none", "none", "none", "flex", "flex", "flex"],
        min_width=styles.sidebar_width,
        height="100%",
        position="sticky",
        top="0px",
        right="0px", # Position to the right for RTL
        z_index="10",
    )