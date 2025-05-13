import reflex as rx
from typing import Optional, List
import datetime # برای created_at_str و updated_at_str

class BotUser(rx.Base): # از rx.Base استفاده می‌کنیم چون داده از MongoDB می‌آید
    user_id: int
    national_id: Optional[str] = None
    username: Optional[str] = None
    chat_state: Optional[str] = None
    chat_id: Optional[int] = None
    updated_at: Optional[int] = None
    created_at: Optional[int] = None
    referral: Optional[str] = None
    agent_code: Optional[str] = None
    trial_noticed: Optional[bool] = None
    trial_ended: Optional[bool] = None
    level: Optional[str] = None
    level_checked_at: Optional[int] = None
    channels: Optional[List[int]] = None # مطمئن شوید نوع داده با MongoDB یکی است
    registration_wizard_step: Optional[int] = None
    capital_limit: Optional[str] = None

    @rx.var
    def created_at_str(self) -> str:
        if self.created_at:
            try:
                return datetime.datetime.fromtimestamp(self.created_at).strftime('%Y-%m-%d %H:%M:%S')
            except TypeError: # اگر created_at از قبل رشته باشد یا نوع دیگری
                return str(self.created_at)
        return "-"

    @rx.var
    def updated_at_str(self) -> str:
        if self.updated_at:
            try:
                return datetime.datetime.fromtimestamp(self.updated_at).strftime('%Y-%m-%d %H:%M:%S')
            except TypeError:
                return str(self.updated_at)
        return "-"

    @rx.var
    def channels_str(self) -> str:
        if self.channels:
            return ", ".join(map(str, self.channels))
        return "-"