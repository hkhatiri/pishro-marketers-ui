# customer_data/backend/mongo.py
import datetime
from enum import Enum
from typing import Any, Union, List, Tuple, Optional, Iterator # Iterator اضافه شد
from bson import ObjectId
from pymongo import MongoClient, DESCENDING, ASCENDING # DESCENDING, ASCENDING اضافه شد
from pymongo.errors import ConnectionFailure # برای مدیریت خطای اتصال

# رشته اتصال MongoDB Atlas شما
# هشدار: قرار دادن مستقیم اطلاعات حساس (مانند نام کاربری و رمز عبور) در کد منبع،
# به خصوص اگر کد شما به اشتراک گذاشته می‌شود یا در محیط پروداکشن استفاده می‌شود،
# از نظر امنیتی توصیه نمی‌شود. بهتر است از متغیرهای محیطی استفاده کنید.
MONGO_CONNECTION_URI = "mongodb+srv://hkhatiri:Hkhatiri1471@pishro.ij89k3u.mongodb.net/?retryWrites=true&w=majority&appName=pishro"

ChatState = Enum(
    'ChatState', [
        'INITED', 'BLOCKED', 'WaitForNationalId', 'WaitForOTP',
        'WaitForCaptcha', 'LoggedIn', 'HasAccess', 'HasManualAccess',
    ]
)

class Mongo:
    def __init__(self, mongo_db_name: str) -> None:
        self.mongo_db_name = mongo_db_name
        try:
            # اتصال به MongoDB با استفاده از رشته اتصال (URI)
            # می‌توانید گزینه‌های اضافی مانند timeoutMS را هم اینجا اضافه کنید اگر نیاز بود
            # self.client = MongoClient(MONGO_CONNECTION_URI, serverSelectionTimeoutMS=5000)
            self.client = MongoClient(MONGO_CONNECTION_URI)

            # این دستور برای تست و اطمینان از برقراری موفقیت‌آمیز اتصال است.
            # اگر اتصال ناموفق باشد (مثلاً به دلیل اطلاعات کاربری اشتباه، مشکل شبکه، یا فایروال)،
            # این بخش یک Exception ایجاد خواهد کرد.
            self.client.admin.command('ping')
            print("--- Successfully connected to remote MongoDB via Atlas URI! ---")

        except ConnectionFailure as e:
            print(f"--- FATAL ERROR: Failed to connect to MongoDB using Atlas URI. ---")
            print(f"--- Connection String Used (hide credentials in production logs): {MONGO_CONNECTION_URI[:MONGO_CONNECTION_URI.find('//')+2]}********:********@{MONGO_CONNECTION_URI[MONGO_CONNECTION_URI.find('@')+1:]}")
            print(f"--- MongoDB Connection Error: {e} ---")
            print("--- Please check: ---")
            print("    1. Your internet connection.")
            print("    2. The MongoDB Atlas cluster is running and accessible.")
            print("    3. The username/password in the URI are correct.")
            print("    4. The IP address of this server is whitelisted in MongoDB Atlas Network Access settings.")
            print("    5. You have the 'dnspython' library installed if using an srv URI ('pip install dnspython').")
            # برنامه متوقف می‌شود چون اتصال به دیتابیس برقرار نشده است.
            raise  # این Exception باعث توقف برنامه می‌شود.

        except Exception as e: # سایر خطاهای احتمالی در زمان اتصال
            print(f"--- FATAL ERROR: An unexpected error occurred while connecting to MongoDB. ---")
            print(f"--- Error details: {e} ---")
            raise

        # نام دیتابیس از آرگومان ورودی گرفته می‌شود.
        # در فایل backend.py شما، این مقدار برابر "marketersbot" تنظیم شده است.
        # رشته اتصال شما به کلاستر متصل می‌شود و سپس این خط دیتابیس مورد نظر را انتخاب می‌کند.
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
            return None
        try:
            return self.db.users.delete_one({'_id': ObjectId(object_id_str)})
        except Exception as e:
            print(f"--- ERROR in delete_user_by_object_id: {e} ---")
            raise

    def get_user(self, key: str, value: Any) -> Union[None, dict]:
        query = {}
        if key == '_id':
            if not ObjectId.is_valid(value):
                return None
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
            return

        update_operation: dict[str, Any] = {}
        if values_to_set:
            update_operation['$set'] = values_to_set
        if values_to_unset:
            update_operation['$unset'] = values_to_unset
            
        if not update_operation:
            return

        try:
            self.db.users.update_one(
                {'_id': ObjectId(object_id_str)},
                update_operation
            )
        except Exception as e:
            print(f"--- ERROR in update_user_properties_by_object_id: {e} ---")
            # raise e

    def get_all_users_cursor(self, query_filter: Optional[dict] = None, sort_field: Optional[str] = None, sort_direction: Optional[int] = None) -> Iterator[dict[str, Any]]:
        if query_filter is None:
            query_filter = {}
        
        cursor = self.db.users.find(query_filter)
        if sort_field and sort_direction is not None:
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