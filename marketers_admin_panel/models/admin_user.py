import reflex as rx
from sqlmodel import Field

class AdminUser(rx.Model, table=True):
    username: str = Field(default=None, unique=True, index=True, nullable=False)
    password_hash: str = Field(default=None, nullable=False)
    referral_type: str = Field(default="", index=True, nullable=True)
    is_super_admin: bool = Field(default=False)
    is_active: bool = Field(default=True)