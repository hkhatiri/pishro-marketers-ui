import datetime
from enum import Enum
from typing import Any, Union, List, Tuple, Optional
from bson import ObjectId # برای کار با ObjectId

from pymongo import MongoClient

# اگر فایل settings.py و MONGO_CONFIG را دارید، از آن استفاده کنید
# در غیر این صورت، برای اتصال به لوکال هاست پیش فرض، MONGO_CONFIG را خالی بگذارید
try:
    import settings # type: ignore
    MONGO_CONFIG = settings.MONGO_CONFIG
except (ImportError, AttributeError):
    MONGO_CONFIG = {}


ChatState = Enum(
    'ChatState', [
        'INITED', 'BLOCKED', 'WaitForNationalId', 'WaitForOTP',
        'WaitForCaptcha', 'LoggedIn', 'HasAccess', 'HasManualAccess',
    ]
)

class Mongo:
    def __init__(self, mongo_db_name: str) -> None:
        self.mongo_db_name = mongo_db_name
        self.client = MongoClient(**MONGO_CONFIG) # به پیش‌فرض لوکال‌هاست وصل می‌شود اگر MONGO_CONFIG خالی باشد
        self.db = self.client[self.mongo_db_name]

    def drop_database(self):
        self.client.drop_database(self.mongo_db_name)

    def store_event(self, event: dict) -> None:
        self.db.events.insert_one(event)

    def store_check_level(self, check_level: dict) -> None:
        self.db.check_level.insert_one(check_level)

    def delete_user_by_object_id(self, object_id_str: str):
        if not ObjectId.is_valid(object_id_str):
            print(f"--- ERROR: Invalid ObjectId string for delete: {object_id_str} ---")
            class MockDeleteResult:
                deleted_count = 0
            return MockDeleteResult()
        try:
            return self.db.users.delete_one({'_id': ObjectId(object_id_str)})
        except Exception as e:
            print(f"--- ERROR in delete_user_by_object_id: {e} ---")
            raise

    def get_user(self, key: str, value: Any) -> Union[None, dict]:
        query = {}
        if key == "_id":
            if isinstance(value, str):
                if not ObjectId.is_valid(value):
                    print(f"--- ERROR: Invalid ObjectId string for get_user with key _id: {value} ---")
                    return None
                try:
                    query[key] = ObjectId(value)
                except Exception as e:
                    print(f"--- ERROR: Could not convert string to ObjectId: {value}, Error: {e} ---")
                    return None
            elif isinstance(value, ObjectId):
                query[key] = value
            else:
                print(f"--- ERROR: Invalid type for _id query, expected ObjectId or valid string, got {type(value)} ---")
                return None
        else:
            query[key] = value
        return self.db.users.find_one(query)

    def get_user_by_object_id(self, object_id_str: str) -> Union[None, dict]: # این متد باید وجود داشته باشد
        return self.get_user('_id', object_id_str)

    def get_user_by_user_id_numeric(self, user_id_num: int) -> Union[None, dict]:
        return self.get_user('user_id', user_id_num)

    def update_user_properties_by_object_id(self, object_id_str: str, values: dict) -> None: # این متد باید وجود داشته باشد
        if not ObjectId.is_valid(object_id_str):
            print(f"--- ERROR: Invalid ObjectId string for update: {object_id_str} ---")
            raise ValueError(f"Invalid ObjectId string: {object_id_str}")
        try:
            self.db.users.update_one(
                {'_id': ObjectId(object_id_str)},
                {'$set': values}
            )
        except Exception as e:
            print(f"--- ERROR in update_user_properties_by_object_id: {e} ---")
            raise

    def get_all_users_cursor(self, query_filter: Optional[dict] = None):
        if query_filter is None:
            query_filter = {}
        return self.db.users.find(query_filter)

    def insert_user(self, user_data: dict):
        try:
            return self.db.users.insert_one(user_data)
        except Exception as e:
            print(f"--- ERROR in insert_user: {e} ---")
            raise

# کلاس UserBase دیگر مستقیماً در State استفاده نمی‌شود و می‌توانید آن را حذف کنید اگر جای دیگری استفاده نمی‌شود.