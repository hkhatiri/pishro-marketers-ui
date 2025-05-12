import reflex as rx
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from typing import List, Dict, Optional
from enum import Enum
from passlib.context import CryptContext

load_dotenv()

# تنظیمات MongoDB بدون احراز هویت
MONGO_CONFIG = {
    'host': os.getenv("MONGO_HOST", "127.0.0.1"),
    'port': int(os.getenv("MONGO_PORT", 27017)),
}
MONGO_DB = os.getenv("MR_MONGO_DB", "marketersbot")

# تنظیمات برای هش کردن رمز عبور
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ChatState(Enum):
    INITED = "INITED"
    BLOCKED = "BLOCKED"
    WaitForNationalId = "WaitForNationalId"
    WaitForOTP = "WaitForOTP"
    WaitForCaptcha = "WaitForCaptcha"
    LoggedIn = "LoggedIn"
    HasAccess = "HasAccess"
    HasManualAccess = "HasManualAccess"

class AdminState(rx.State):
    is_authenticated: bool = False
    username: str = ""
    password: str = ""
    referral: str = ""
    search_query: str = ""
    users: List[Dict] = []
    error_message: str = ""
    new_admin_username: str = ""
    new_admin_password: str = ""
    new_admin_referral: str = ""
    valid_referrals: List[str] = ["demo", "Etfbaz", "ashrafi", "kahyani"]

    def login(self):
        client = MongoClient(**MONGO_CONFIG)
        db = client[MONGO_DB]
        try:
            admin = db.admins.find_one({"username": self.username})
            if admin and pwd_context.verify(self.password, admin["password"]):
                self.is_authenticated = True
                self.referral = admin["referral"]
                self.error_message = ""
                self.load_users()  # بارگذاری کاربران پس از ورود
            else:
                self.error_message = "Invalid username or password"
                self.is_authenticated = False
        finally:
            client.close()

    def logout(self):
        self.is_authenticated = False
        self.username = ""
        self.password = ""
        self.referral = ""
        self.users = []

    @rx.background
    async def load_users(self):
        client = MongoClient(**MONGO_CONFIG)
        db = client[MONGO_DB]
        try:
            users = list(db.users.find({"referral": self.referral}))
            for user in users:
                user["chat_state"] = ChatState[user.get("chat_state", "INITED")].value if user.get("chat_state") else None
            async with self:
                self.users = users
        finally:
            client.close()

    @rx.background
    async def search_users(self):
        client = MongoClient(**MONGO_CONFIG)
        db = client[MONGO_DB]
        try:
            query = self.search_query.strip()
            if query:
                users = list(db.users.find({
                    "$and": [
                        {"referral": self.referral},
                        {"$or": [
                            {"national_id": {"$regex": query, "$options": "i"}},
                            {"username": {"$regex": query, "$options": "i"}}
                        ]}
                    ]
                }))
            else:
                users = list(db.users.find({"referral": self.referral}))
            for user in users:
                user["chat_state"] = ChatState[user.get("chat_state", "INITED")].value if user.get("chat_state") else None
            async with self:
                self.users = users
        finally:
            client.close()

    @rx.background
    async def delete_user(self, user_id: int):
        client = MongoClient(**MONGO_CONFIG)
        db = client[MONGO_DB]
        try:
            user = db.users.find_one({"user_id": user_id})
            if user and user["referral"] == self.referral:
                db.users.delete_one({"user_id": user_id})
                async with self:
                    self.users = [u for u in self.users if u["user_id"] != user_id]
            else:
                async with self:
                    self.error_message = "Unauthorized: User does not belong to your referral"
        finally:
            client.close()

    @rx.background
    async def add_admin(self):
        client = MongoClient(**MONGO_CONFIG)
        db = client[MONGO_DB]
        try:
            if not self.new_admin_username or not self.new_admin_password or not self.new_admin_referral:
                async with self:
                    self.error_message = "All fields are required"
                return
            if self.new_admin_referral not in self.valid_referrals:
                async with self:
                    self.error_message = "Invalid referral"
                return
            if db.admins.find_one({"username": self.new_admin_username}):
                async with self:
                    self.error_message = "Username already exists"
                return
            hashed_password = pwd_context.hash(self.new_admin_password)
            db.admins.insert_one({
                "username": self.new_admin_username,
                "password": hashed_password,
                "referral": self.new_admin_referral
            })
            async with self:
                self.error_message = "Admin added successfully"
                self.new_admin_username = ""
                self.new_admin_password = ""
                self.new_admin_referral = ""
        finally:
            client.close()

    def set_search_query(self, value: str):
        self.search_query = value

    def set_new_admin_username(self, value: str):
        self.new_admin_username = value

    def set_new_admin_password(self, value: str):
        self.new_admin_password = value

    def set_new_admin_referral(self, value: str):
        self.new_admin_referral = value