import os
import reflex as rx

# database_url = os.getenv("DATABASE_URL", "sqlite:///reflex.db") # این خط برای MongoDB لازم نیست

config = rx.Config(
    app_name="customer_data", # تغییر از "customer_data_mongo" به "customer_data"
    # db_url=database_url, # کامنت یا حذف شد
)