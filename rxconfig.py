import reflex as rx

config = rx.Config(
    app_name="admin_panel",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEVELOPMENT,
)