# status_badges.py
import reflex as rx
from ..backend.backend import ChatState

def _badge(icon: str, text: str, color_scheme: str):
    return rx.badge(
        rx.icon(icon, size=16),
        text,
        color_scheme=color_scheme,
        radius="full",
        variant="soft",
        size="3",
    )

def status_badge(status: str):
    badge_mapping = {
        ChatState.INITED.name: ("circle", "Inited", "gray"),
        ChatState.BLOCKED.name: ("ban", "Blocked", "red"),
        ChatState.WaitForNationalId.name: ("id-card", "Waiting ID", "yellow"),
        ChatState.WaitForOTP.name: ("lock", "Waiting OTP", "yellow"),
        ChatState.WaitForCaptcha.name: ("shield", "Waiting Captcha", "yellow"),
        ChatState.LoggedIn.name: ("log-in", "Logged In", "blue"),
        ChatState.HasAccess.name: ("check", "Has Access", "green"),
        ChatState.HasManualAccess.name: ("check-circle", "Manual Access", "green"),
    }
    return _badge(*badge_mapping.get(status, ("circle", "Inited", "gray")))