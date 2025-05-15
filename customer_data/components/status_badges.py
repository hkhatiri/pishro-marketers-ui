import reflex as rx

def _badge(icon: str, text: str, color_scheme: str):
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="full",
        variant="soft",
        size="2",
    )

def channel_membership_badge(channel_count: rx.Var[int]):
    return rx.cond(
        channel_count > 0,
        _badge("users", "عضو در " + channel_count.to_string() + " کانال", "grass"),
        _badge("user-x", "عضو نیست", "tomato")
    )

def status_badge(channel_count: rx.Var[int]):
    return channel_membership_badge(channel_count)