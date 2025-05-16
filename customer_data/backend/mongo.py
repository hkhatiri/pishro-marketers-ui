# customer_data/backend/mongo.py
import datetime
from enum import Enum
from typing import Any, Union, List, Tuple, Optional, Iterator # Iterator اضافه شد
from bson import ObjectId
from pymongo import MongoClient, DESCENDING, ASCENDING # DESCENDING, ASCENDING اضافه شد

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
        self.client = MongoClient(**MONGO_CONFIG)
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
            # به جای raise کردن یک ValueError عمومی، می‌توانید یک نتیجه ناموفق برگردانید
            # یا خطای خاص‌تری raise کنید. فعلاً None برمی‌گردانیم.
            return None
        try:
            return self.db.users.delete_one({'_id': ObjectId(object_id_str)})
        except Exception as e:
            print(f"--- ERROR in delete_user_by_object_id: {e} ---")
            raise # یا None برگردانید

    def get_user(self, key: str, value: Any) -> Union[None, dict]:
        query = {}
        if key == '_id':
            if not ObjectId.is_valid(value):
                # print(f"--- WARNING: Invalid ObjectId string for get_user: {value} ---")
                return None # اگر ObjectId نامعتبر است، None برگردان
            query[key] = ObjectId(value)
        else:
            query[key] = value
        return self.db.users.find_one(query)

    def get_user_by_object_id(self, object_id_str: str) -> Union[None, dict]:
        return self.get_user('_id', object_id_str)

    def get_user_by_user_id_numeric(self, user_id_num: int) -> Union[None, dict]:
        return self.get_user('user_id', user_id_num)

    def update_user_properties_by_object_id(self, object_id_str: str, values_to_set: Optional[dict] = None, values_to_unset: Optional[dict] = None) -> None:
        if not ObjectId.is_valid(object_id_str):
            print(f"--- ERROR: Invalid ObjectId string for update: {object_id_str} ---")
            # raise ValueError(f"Invalid ObjectId string: {object_id_str}") # یا مدیریت خطا به شکل دیگر
            return

        update_operation: dict[str, Any] = {}
        if values_to_set:
            update_operation['$set'] = values_to_set
        if values_to_unset:
            update_operation['$unset'] = values_to_unset
            
        if not update_operation:
            # print(f"--- WARNING: No update operation specified for ObjectId {object_id_str} ---")
            return

        try:
            self.db.users.update_one(
                {'_id': ObjectId(object_id_str)},
                update_operation
            )
        except Exception as e:
            print(f"--- ERROR in update_user_properties_by_object_id: {e} ---")
            # raise e # یا مدیریت خطا به شکل دیگر

    # --- تغییر در اینجا برای پذیرش آرگومان‌های مرتب‌سازی ---
    def get_all_users_cursor(self, query_filter: Optional[dict] = None, sort_field: Optional[str] = None, sort_direction: Optional[int] = None) -> Iterator[dict[str, Any]]:
        if query_filter is None:
            query_filter = {}
        
        cursor = self.db.users.find(query_filter)
        if sort_field and sort_direction is not None:
            # اطمینان از اینکه sort_direction معتبر است (1 برای صعودی، -1 برای نزولی)
            if sort_direction in [ASCENDING, DESCENDING]:
                cursor = cursor.sort(sort_field, sort_direction)
            else:
                print(f"--- WARNING: Invalid sort_direction '{sort_direction}' provided. Ignoring sort. ---")
        return cursor

    def insert_user(self, user_data: dict):
        try:
            return self.db.users.insert_one(user_data)
        except Exception as e:
            print(f"--- ERROR in insert_user: {e} ---")
            raise

    def count_all_users(self, query_filter: Optional[dict] = None) -> int:
        if query_filter is None:
            query_filter = {}
        return self.db.users.count_documents(query_filter)