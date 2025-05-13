import reflex as rx
import os

ADMIN_PANEL_DATABASE_URL = os.getenv("ADMIN_PANEL_DATABASE_URL", "sqlite:///admin_reflex.db")

config = rx.Config(
    app_name="marketers_admin_panel", # نام اپ شما
    db_url=ADMIN_PANEL_DATABASE_URL,
    telemetry_enabled=False,
)