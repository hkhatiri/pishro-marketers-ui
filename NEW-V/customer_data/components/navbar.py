# customer_data/components/navbar.py
"""Navbar component for the app (primarily for mobile)."""
import reflex as rx
from .. import styles
# from ..templates.template import ALL_PAGES # Not using for now

def menu_item_icon(icon: str) -> rx.Component:
    return rx.icon(icon, size=20, margin_left="0.75em") # margin_left for RTL

def menu_item(text: str, url: str, icon_name: str) -> rx.Component:
    """Menu item for the drawer."""
    active = (rx.State.router.page.path == url.lower()) | (
        (rx.State.router.page.path == "/") & (url == "/")
    )
    return rx.link(
        rx.hstack(
            # Icon first then text for drawer items, or text then icon if preferred
            menu_item_icon(icon_name),
            rx.text(text, size="4", weight="medium"),
            bg=rx.cond(active, styles.accent_bg_color, "transparent"),
            color=rx.cond(active, styles.accent_text_color, styles.text_color),
            style={
                "_hover": {
                    "background_color": styles.accent_bg_color,
                    "color": styles.accent_text_color,
                },
            },
            align="center",
            border_radius=styles.border_radius,
            width="100%",
            padding="0.5em",
        ),
        href=url,
        width="100%",
        underline="none",
    )

def menu_button_drawer_content(project_pages: list) -> rx.Component:
    """Content for the drawer menu."""
    return rx.vstack(
        rx.hstack(
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg", height="1.25em"),
                rx.image(src="/reflex_white.svg", height="1.25em"),
            ),
            rx.spacer(),
            rx.drawer.close(rx.icon(tag="x", size=22)),
            justify="between",
            width="100%",
            padding_bottom="0.5em",
        ),
        rx.divider(),
        *[
            menu_item(
                text=page["title"],
                url=page["route"],
                icon_name=page["icon"]
            )
            for page in project_pages
        ],
        rx.spacer(),
        rx.hstack(
            rx.link("راهنما", href="#", color_scheme="gray", size="3"),
            rx.spacer(),
            rx.color_mode.button(opacity=0.8, size="2"),
            width="100%",
            padding_top="1em",
            border_top=f"1px solid {rx.color('gray', 4)}",
        ),
        spacing="3",
        width="100%",
        height="100%",
        padding="1em",
    )

def menu_button(project_pages: list) -> rx.Component:
    """Menu button that triggers a drawer."""
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.icon("align-justify", size=24)
        ),
        rx.drawer.overlay(z_index="49"),
        rx.drawer.portal(
            rx.drawer.content(
                menu_button_drawer_content(project_pages),
                top="auto",
                left="auto", # For RTL, drawer comes from right
                right="0", # Position drawer to the right for RTL
                height="100%",
                width="20em",
                padding="0",
                bg=rx.color("gray", 1),
                border_right=styles.border, # border_right for RTL
            )
        ),
        direction="right", # Drawer comes from the right for RTL
    )

def navbar_component() -> rx.Component:
    """The navbar for mobile view."""
    project_pages = [
        {"title": "داشبورد اصلی", "route": "/", "icon": "layout-dashboard"},
        {"title": "جدول کاربران", "route": "/table", "icon": "table-2"},
    ]
    return rx.box(
        rx.hstack(
            # Menu button on the right for RTL
            rx.spacer(),
            rx.color_mode_cond(
                rx.image(src="/reflex_black.svg", height="1.25em"),
                rx.image(src="/reflex_white.svg", height="1.25em"),
            ),
            rx.spacer(),
            menu_button(project_pages),
            align="center",
            width="100%",
            padding_y="0.75em",
            padding_x="1em",
        ),
        display=["flex", "flex", "flex", "none", "none", "none"],
        position="sticky",
        top="0px",
        z_index="20",
        bg=rx.color("gray", 1),
        border_bottom=styles.border,
        width="100%",
    )