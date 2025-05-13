import reflex as rx

styles = {
    "container": {
        "padding": "20px",
        "max_width": "1200px",
        "margin": "0 auto",
    },
    "card": {
        "border": "1px solid #e0e0e0",
        "border_radius": "8px",
        "padding": "16px",
        "margin_bottom": "16px",
        "box_shadow": "0 2px 4px rgba(0,0,0,0.1)",
    },
    "button": {
        "background_color": "#007bff",
        "color": "white",
        "padding": "8px 16px",
        "border_radius": "4px",
        "cursor": "pointer",
        ":hover": {"background_color": "#0056b3"},  # تغییر _hover به :hover
    },
    "danger_button": {
        "background_color": "#dc3545",
        "color": "white",
        "padding": "8px 16px",
        "border_radius": "4px",
        "cursor": "pointer",
        ":hover": {"background_color": "#c82333"},  # تغییر _hover به :hover
    },
}