# customer_data/components/card.py
import reflex as rx
from .. import styles

def card(*children, **props) -> rx.Component:
    default_props = {
        "box_shadow": styles.box_shadow_style,
        "size": "3",
        "width": "100%",
        "padding": "1em",
        "border_radius": styles.border_radius,
    }
    final_props = {**default_props, **props}
    return rx.card(
        *children,
        **final_props,
    )