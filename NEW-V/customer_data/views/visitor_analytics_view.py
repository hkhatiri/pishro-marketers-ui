# customer_data/views/visitor_analytics_view.py
import reflex as rx
from ..components.card import card
from ..backend.backend import State as MainState

def _pie_chart_component(data_var: rx.Var[list[dict]], chart_id: str) -> rx.Component:
    """Helper function to create a pie chart."""
    return rx.recharts.pie_chart(
        rx.recharts.pie(
            data=data_var,
            data_key="value",
            name_key="name",
            cx="50%",
            cy="45%", # Adjusted to make space for legend at bottom
            padding_angle=1,
            inner_radius="50%",
            outer_radius="80%",
            label_line=False,
        ),
        rx.recharts.legend(
            icon_size=10,
            layout="horizontal",
            vertical_align="bottom",
            align="center",
            wrapper_style={"paddingTop": "10px"} # Add padding to legend
        ),
        rx.recharts.graphing_tooltip(cursor={"fill": "var(--gray-4)"}),
        # --- CHANGE THIS LINE ---
        height=350, # Changed from "350px" to 350 (integer for pixels)
        # --- END OF CHANGE ---
        width="100%", # Percentage width is fine
    )

def visitors_analytics_section() -> rx.Component:
    return card(
        rx.vstack(
            rx.hstack(
                rx.icon("pie-chart", size=20, margin_left="0.5em"), # margin_left for RTL
                rx.heading("تحلیل کاربران", size="5", weight="medium"),
                align_items="center",
                width="100%",
                margin_bottom="1em",
            ),
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("بر اساس سطح", value="levels"),
                    rx.tabs.trigger("عضویت کانال", value="channels"),
                    width="100%",
                    justify_content="center",
                ),
                rx.tabs.content(
                    _pie_chart_component(MainState.user_levels_pie_data, "levelsPie"), # type: ignore
                    value="levels",
                    padding_top="1em",
                ),
                rx.tabs.content(
                    _pie_chart_component(MainState.channel_membership_pie_data, "channelsPie"), # type: ignore
                    value="channels",
                    padding_top="1em",
                ),
                default_value="levels",
                width="100%",
            ),
            spacing="4",
            width="100%",
            align_items="stretch",
        )
    )