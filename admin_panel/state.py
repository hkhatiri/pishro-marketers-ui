import reflex as rx
from pymongo import MongoClient
import os
import json
from typing import List, Optional
from mongo import Mongo, ChatState, UserBase

# تنظیمات محیطی
MONGO_CONFIG = {
    'host': os.environ.get("MONGO_HOST", "127.0.0.1"),
    'port': int(os.environ.get("MONGO_PORT", 27017)),
}
MONGO_DB = os.environ.get("MONGO_DB", "marketersbot")
ADMIN_PASSWORDS = json.loads(os.environ.get("ADMIN_PASSWORDS", '{}'))

class AuthState(rx.State):
    username: str = ""
    password: str = ""
    is_authenticated: bool = False
    error_message: str = ""

    def login(self):
        if self.username in ADMIN_PASSWORDS and self.password == ADMIN_PASSWORDS[self.username]:
            self.is_authenticated = True
            self.error_message = ""
            UserState.referral = self.username
        else:
            self.error_message = "نام کاربری یا رمز عبور اشتباه است."
            self.is_authenticated = False

    def logout(self):
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        UserState.referral = ""

class UserState(rx.State):
    referral: str = ""
    users: List[dict] = []
    selected_user: Optional[dict] = None
    loading: bool = False

    def __init__(self):
        super().__init__()
        self.mongo = Mongo(MONGO_DB)
        self.user_base = UserBase()
        self.user_base._db_name = MONGO_DB

    def load_users(self):
        self.loading = True
        try:
            self.users = [
                {
                    "user_id": user.user_id,
                    "national_id": user.national_id or "نامشخص",
                    "username": user.username or "نامشخص",
                    "level": user.level or "نامشخص",
                    "chat_state": user.chat_state or "نامشخص",
                    "joined_count": user.joined_count,
                }
                for user in self.user_base.list_approved({"referral": self.referral})
            ]
        finally:
            self.loading = False

    def select_user(self, user_id: int):
        user = next((u for u in self.user_base.list_approved({"user_id": user_id, "referral": self.referral})), None)
        if user:
            self.selected_user = {
                "user_id": user.user_id,
                "national_id": user.national_id or "نامشخص",
                "username": user.username or "نامشخص",
                "level": user.level or "نامشخص",
                "chat_state": user.chat_state or "نامشخص",
                "joined_count": user.joined_count,
                "channels": user.channels or [],
                "created_at": user.created_at or 0,
                "level_checked_at": user.level_checked_at or 0,
            }

    def delete_user(self, user_id: int):
        self.mongo.delete_user(user_id)
        self.load_users()
        self.selected_user = None