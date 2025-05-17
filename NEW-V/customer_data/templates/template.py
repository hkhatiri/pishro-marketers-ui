# customer_data/templates/template.py
from __future__ import annotations
from typing import Callable
import reflex as rx
from .. import styles

# Import the new sidebar and navbar components
from ..components.sidebar import sidebar_component
from ..components.navbar import navbar_component # This is the mobile navbar

default_meta = [
    {"name": "viewport", "content": "width=device-width, shrink-to-fit=no, initial-scale=1"},
]

class ThemeState(rx.State):
    accent_color: str = "grass" # Your project's default
    gray_color: str = "gray"
    radius: str = "large"
    scaling: str = "100%"

ALL_PAGES = [] # Populated by @template decorator to be used by sidebar/navbar

def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: list[dict] | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventType | list[rx.event.EventType] | None = None,
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.flex( # Main flex container for sidebar and content
                sidebar_component(), # Sidebar for larger screens
                rx.vstack( # Content area that includes mobile navbar and page content
                    navbar_component(), # Mobile navbar for smaller screens
                    rx.box( # Main page content wrapper
                        page_content(), # The actual page content
                        width="100%",
                        style=styles.template_content_style, # Padding for the content itself
                    ),
                    width="100%", # Takes remaining width after sidebar
                    height="100dvh",
                    overflow_y="auto", # Allow vertical scroll for content area
                    style=styles.template_page_style, # General padding and max_width for the vstack
                    # max_width=["100%", "100%", "100%", "100%", "100%", styles.max_width],
                ),
                flex_direction="row", # Sidebar and content side-by-side
                align_items="start", # Align items to the top
                width="100%",
                position="relative",
            )

        @rx.page(
            route=route, title=title, description=description, meta=all_meta,
            script_tags=script_tags, on_load=on_load, # type: ignore
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True, accent_color=ThemeState.accent_color,
                gray_color=ThemeState.gray_color, radius=ThemeState.radius,
                scaling=ThemeState.scaling,
                # For RTL support in Radix Themes components if needed:
                # dir="rtl" # This might be inherited from html/body if `styles.base_style` sets it globally
            )

        if route is not None:
            page_info = {"route": route}
            if title is not None: page_info["title"] = title
            # Avoid adding duplicate routes
            if not any(p["route"] == route for p in ALL_PAGES):
                ALL_PAGES.append(page_info)
        return theme_wrap
    return decorator