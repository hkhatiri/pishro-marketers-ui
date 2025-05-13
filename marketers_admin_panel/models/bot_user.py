import reflex as rx
from typing import Optional, List

class BotUser(rx.Base):
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
    channels: Optional[List[int]] = None
    registration_wizard_step: Optional[int] = None
    capital_limit: Optional[str] = None

    # فیلدهای پر شده توسط AdminState برای نمایش
    created_at_str: Optional[str] = None
    updated_at_str: Optional[str] = None
    level_checked_at_str: Optional[str] = None
    channels_str: Optional[str] = None
    trial_status_str: Optional[str] = None