# backend.py
from datetime import datetime
from typing import Union, List
import reflex as rx
from mongo import Mongo, UserBase, ChatState
from rxconfig import MONGO_DB_NAME

class MonthValues(rx.Base):
    """Values for a month."""
    num_users: int = 0
    num_active: int = 0  # Users with HasAccess or HasManualAccess

def _get_percentage_change(value: Union[int, float], prev_value: Union[int, float]) -> float:
    percentage_change = (
        round(((value - prev_value) / prev_value) * 100, 2)
        if prev_value != 0
        else 0.0
        if value == 0
        else float("inf")
    )
    return percentage_change

class State(rx.State):
    """The app state."""
    users: List[UserBase] = []
    sort_value: str = ""
    sort_reverse: bool = False
    search_value: str = ""
    current_user: UserBase = UserBase()
    current_month_values: MonthValues = MonthValues()
    previous_month_values: MonthValues = MonthValues()

    def __init__(self):
        super().__init__()
        self.db = Mongo(MONGO_DB_NAME)

    def load_entries(self) -> None:
        """Load all users from MongoDB."""
        users = []
        for user_data in self.db.get_users():
            user = UserBase(user_id=user_data["user_id"])
            user._db_name = MONGO_DB_NAME
            user.get()
            if self.search_value:
                search_lower = self.search_value.lower()
                if not any(
                    search_lower in str(getattr(user, field) or "").lower()
                    for field in ["username", "national_id", "chat_state"]
                ):
                    continue
            users.append(user)

        if self.sort_value:
            reverse = self.sort_reverse
            users.sort(
                key=lambda u: str(getattr(u, self.sort_value) or "").lower(),
                reverse=reverse
            )

        self.users = users
        self.get_current_month_values()
        self.get_previous_month_values()

    def get_current_month_values(self):
        """Calculate current month's values."""
        now = datetime.now()
        start_of_month = datetime(now.year, now.month, 1)
        users = list(self.db.get_users())
        current_month_users = [
            u for u in users
            if u.get("created_at") and datetime.fromtimestamp(u["created_at"]) >= start_of_month
        ]
        self.current_month_values = MonthValues(
            num_users=len(current_month_users),
            num_active=len([
                u for u in current_month_users
                if u.get("chat_state") in [ChatState.HasAccess.name, ChatState.HasManualAccess.name]
            ])
        )

    def get_previous_month_values(self):
        """Calculate previous month's values."""
        now = datetime.now()
        first_day_of_current_month = datetime(now.year, now.month, 1)
        last_day_of_last_month = first_day_of_current_month - datetime.timedelta(days=1)
        start_of_last_month = datetime(last_day_of_last_month.year, last_day_of_last_month.month, 1)
        
        users = list(self.db.get_users())
        previous_month_users = [
            u for u in users
            if u.get("created_at") and start_of_last_month <= datetime.fromtimestamp(u["created_at"]) <= last_day_of_last_month
        ]
        self.previous_month_values = MonthValues(
            num_users=len(previous_month_users),
            num_active=len([
                u for u in previous_month_users
                if u.get("chat_state") in [ChatState.HasAccess.name, ChatState.HasManualAccess.name]
            ])
        )

    def sort_values(self, sort_value: str):
        self.sort_value = sort_value
        self.load_entries()

    def toggle_sort(self):
        self.sort_reverse = not self.sort_reverse
        self.load_entries()

    def filter_values(self, search_value: str):
        self.search_value = search_value
        self.load_entries()

    def get_user(self, user: UserBase):
        self.current_user = user

    def add_user_to_db(self, form_data: dict):
        """Add a new user to MongoDB."""
        user_id = int(form_data["user_id"])
        if self.db.get_user_by_id(user_id):
            return rx.window_alert("User with this ID already exists")
        self.db.update_user_properties(
            user_id,
            [
                ("username", form_data["username"]),
                ("national_id", form_data["national_id"]),
                ("chat_state", form_data["chat_state"]),
                ("created_at", int(datetime.now().timestamp())),
            ]
        )
        self.load_entries()
        return rx.toast.info(
            f"User {form_data['username']} has been added.", position="bottom-right"
        )

    def update_user_to_db(self, form_data: dict):
        """Update a user in MongoDB."""
        self.db.update_user_properties(
            self.current_user.user_id,
            [
                ("username", form_data["username"]),
                ("national_id", form_data["national_id"]),
                ("chat_state", form_data["chat_state"]),
            ]
        )
        self.load_entries()
        return rx.toast.info(
            f"User {form_data['username']} has been modified.", position="bottom-right"
        )

    def delete_user(self, user_id: int):
        """Delete a user from MongoDB."""
        user = self.db.get_user_by_id(user_id)
        self.db.delete_user(user_id)
        self.load_entries()
        return rx.toast.info(
            f"User {user['username']} has been deleted.", position="bottom-right"
        )

    @rx.var(cache=True)
    def users_change(self) -> float:
        return _get_percentage_change(
            self.current_month_values.num_users,
            self.previous_month_values.num_users,
        )

    @rx.var(cache=True)
    def active_users_change(self) -> float:
        return _get_percentage_change(
            self.current_month_values.num_active,
            self.previous_month_values.num_active,
        )