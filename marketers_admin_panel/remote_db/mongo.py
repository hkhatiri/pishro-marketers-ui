import datetime
import os
from enum import Enum
from typing import Any, Union, List, Tuple, Optional

from pymongo import MongoClient, errors

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))
DEFAULT_MONGO_DB_NAME = os.environ.get("MR_MONGO_DB", "marketersbot") # نام دیتابیس شما
USERS_COLLECTION = "users" # نام کالکشن کاربران شما

ChatState = Enum(
    'ChatState', [
        'INITED', 'BLOCKED', 'WaitForNationalId', 'WaitForOTP', 'WaitForCaptcha',
        'LoggedIn', 'HasAccess', 'HasManualAccess',
    ]
)

class Mongo:
    def __init__(self, mongo_db_name: Optional[str] = None) -> None:
        self.mongo_db_name = mongo_db_name or DEFAULT_MONGO_DB_NAME
        self.client = None
        self.db = None
        try:
            self.client = MongoClient(
                host=MONGO_HOST,
                port=MONGO_PORT,
                serverSelectionTimeoutMS=3000
            )
            self.client.admin.command('ping')
            self.db = self.client[self.mongo_db_name]
            print(f"Successfully connected to MongoDB: {MONGO_HOST}:{MONGO_PORT}, DB: {self.mongo_db_name}")
        except errors.ServerSelectionTimeoutError as err:
            print(f"MongoDB connection failed (Timeout): {err}")
        except Exception as e:
            print(f"An unexpected error occurred during MongoDB connection: {e}")

    def is_connected(self) -> bool:
        if self.client and self.db:
            try:
                self.client.admin.command('ping')
                return True
            except errors.ConnectionFailure:
                print("MongoDB connection lost.")
                return False
            except Exception:
                return False
        return False

    def delete_user(self, user_id: int):
        if not self.is_connected(): return None
        try:
            return self.db[USERS_COLLECTION].delete_one({'user_id': user_id})
        except Exception as e:
            print(f"Error deleting user {user_id}: {e}")
            return None

    def update_user_properties(self, user_id: int, updates: dict[str, Any]) -> Optional[Any]:
        if not self.is_connected(): return None
        try:
            return self.db[USERS_COLLECTION].update_one(
                {'user_id': user_id},
                {'$set': updates},
                upsert=False
            )
        except Exception as e:
            print(f"Error updating user {user_id}: {e}")
            return None

    def get_users_cursor(self, query_filter: Optional[dict] = None):
        if not self.is_connected():
            print("Cannot get users: Not connected to MongoDB.")
            return iter([])
        actual_filter = query_filter if query_filter is not None else {}
        try:
            return self.db[USERS_COLLECTION].find(actual_filter)
        except Exception as e:
            print(f"Error fetching users with filter {actual_filter}: {e}")
            return iter([])