# marketers_admin_panel/marketers_admin_panel/remote_db/settings.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # اگر از .env استفاده می‌کنید

MONGO_CONFIG = {
    'host': os.environ.get("MONGO_HOST", "localhost"), # یا "127.0.0.1"
    'port': int(os.environ.get("MONGO_PORT", 27017)), # MONGO_PROT به MONGO_PORT تغییر یافت
    # اگر یوزرنیم و پسورد ندارید، این خطوط را حذف کنید یا خالی بگذارید
    # 'username': os.environ.get("MONGO_USERNAME"),
    # 'password': os.environ.get("MONGO_PASSWORD"),
}

SETTINGS = {
    # ... (سایر تنظیمات بات شما)
    'marketers': {
        'bot_name': 'marketers', # یا هر نامی که برای بات marketers در نظر گرفته‌اید
        # ... سایر تنظیمات بات marketers
        'MONGO_DB': os.environ.get("MR_MONGO_DB", "marketersbot"), 
        # ...
    },
    # ...
}