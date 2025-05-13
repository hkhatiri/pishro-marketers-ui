import reflex as rx

class AdminUser(rx.Model, table=True):
    username: str = rx.Field(unique=True, index=True)
    password_hash: str
    referral_type: str = rx.Field(index=True) # e.g., "Etfbaz", "ashrafi"
    is_super_admin: bool = False
    is_active: bool = True