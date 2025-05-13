# rxconfig.py
import os
import reflex as rx

MONGO_CONFIG = {
    "host": "127.0.0.1",
    "port": 27017,
}
MONGO_DB_NAME = "marketersbot"

config = rx.Config(
    app_name="customer_data",
    # Remove db_url since we'll use MongoDB
    mongo_config=MONGO_CONFIG,
    mongo_db_name=MONGO_DB_NAME,
)
