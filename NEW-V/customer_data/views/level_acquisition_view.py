# customer_data/views/level_acquisition_view.py
import reflex as rx
from reflex.components.radix.themes.base import LiteralAccentColor # برای type hinting رنگ‌ها

from ..components.card import card
from ..backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL
from ..backend.backend import State as MainState

# دیکشنری‌های کمکی برای استایل‌دهی (مشابه قبل)
LEVEL_COLORS: dict[str, LiteralAccentColor] = {
    "level_0": "gray", "level_1": "blue", "level_2": "orange",
    "level_3": "purple", "level_golden": "amber", # رنگ "طلایی" به amber تغییر کرد
    NO_LEVEL_VALUE_INTERNAL: "gray", # برای سطحی که تعریف نشده
    "_default_": "green" # رنگ پیش‌فرض اگر سطح در دیکشنری نباشد
}
LEVEL_ICONS: dict[str, str] = {
    "level_0": "bar-chart-3", "level_1": "user-check", "level_2": "user-cog",
    "level_3": "users", "level_golden": "gem",
    NO_LEVEL_VALUE_INTERNAL: "minus-circle", # آیکون برای سطح تعریف نشده
    "_default_": "award" # آیکون پیش‌فرض
}

def level_progress_item(
    level_key_var: rx.Var[str], # ورودی یک rx.Var[str] از rx.foreach است
    user_count_var: rx.Var[int], # تعداد کاربران برای این سطح (از MainState.user_counts_by_level_var)
    total_users_in_referral_var: rx.Var[int] # کل کاربران برای محاسبه درصد
) -> rx.Component:
    """
    یک آیتم (سطر) برای نمایش آمار یک سطح خاص با نوار پیشرفت.
    """

    # برای گرفتن مقدار رشته‌ای از rx.Var برای استفاده به عنوان کلید دیکشنری
    # این بخش باید در زمان رندر توسط Reflex به درستی به رشته تبدیل شود.
    # اگر در عمل با مشکل مواجه شد، باید این تبدیل به رشته را در یک @rx.var کمکی انجام داد.
    # اما معمولاً Reflex می‌تواند Varها را در جای مناسب به مقدارشان تبدیل کند.

    # نام نمایشی سطح
    # ما یک rx.Var جدید برای نام نمایشی نمی‌سازیم، بلکه مستقیماً از مقدار Var ورودی استفاده می‌کنیم.
    # Reflex این تبدیل را در زمان رندر انجام می‌دهد.
    level_display_name = rx.text(
        LEVEL_TRANSLATIONS.get(level_key_var, level_key_var.to_string().replace("level_", "سطح ")), # type: ignore
        size="3", weight="medium", color=rx.color("gray", 11)
    )

    # محاسبه درصد پیشرفت
    progress_percentage = rx.cond(
        total_users_in_referral_var > 0,
        (user_count_var / total_users_in_referral_var) * 100,
        0
    )
    # اطمینان از اینکه مقدار پیشرفت بین ۰ تا ۱۰۰ است برای نوار پیشرفت
    clamped_progress = rx.cond(progress_percentage < 0, 0, rx.cond(progress_percentage > 100, 100, progress_percentage))

    return rx.vstack(
        rx.hstack(
            # آیکون و رنگ بر اساس سطح
            # ما مستقیماً رشته‌های نام آیکون و رنگ را پاس می‌دهیم.
            rx.icon(
                # استفاده از rx.match برای انتخاب آیکون و رنگ بر اساس level_key_var
                rx.match(
                    level_key_var,
                    ("level_0", LEVEL_ICONS["level_0"]),
                    ("level_1", LEVEL_ICONS["level_1"]),
                    ("level_2", LEVEL_ICONS["level_2"]),
                    ("level_3", LEVEL_ICONS["level_3"]),
                    ("level_golden", LEVEL_ICONS["level_golden"]),
                    (NO_LEVEL_VALUE_INTERNAL, LEVEL_ICONS[NO_LEVEL_VALUE_INTERNAL]),
                    LEVEL_ICONS["_default_"], # مقدار پیش‌فرض
                ),
                size=18,
                color=rx.match( # انتخاب رنگ برای آیکون
                    level_key_var,
                    ("level_0", rx.color(LEVEL_COLORS["level_0"], 9)),
                    ("level_1", rx.color(LEVEL_COLORS["level_1"], 9)),
                    ("level_2", rx.color(LEVEL_COLORS["level_2"], 9)),
                    ("level_3", rx.color(LEVEL_COLORS["level_3"], 9)),
                    ("level_golden", rx.color(LEVEL_COLORS["level_golden"], 9)),
                    (NO_LEVEL_VALUE_INTERNAL, rx.color(LEVEL_COLORS[NO_LEVEL_VALUE_INTERNAL], 9)),
                    rx.color(LEVEL_COLORS["_default_"], 9),
                ),
                margin_left="0.5em" # برای RTL
            ),
            level_display_name, # کامپوننت rx.text که در بالا ساختیم
            rx.spacer(),
            rx.text(user_count_var.to_string() + " کاربر", size="2", color=rx.color("gray", 10)),
            align_items="center",
            width="100%",
        ),
        rx.progress(
            value=clamped_progress,
            # انتخاب color_scheme برای نوار پیشرفت
            color_scheme=rx.match( # type: ignore
                level_key_var,
                ("level_0", LEVEL_COLORS["level_0"]),
                ("level_1", LEVEL_COLORS["level_1"]),
                ("level_2", LEVEL_COLORS["level_2"]),
                ("level_3", LEVEL_COLORS["level_3"]),
                ("level_golden", LEVEL_COLORS["level_golden"]),
                (NO_LEVEL_VALUE_INTERNAL, LEVEL_COLORS[NO_LEVEL_VALUE_INTERNAL]),
                LEVEL_COLORS["_default_"],
            ),
            size="2",
            width="100%",
            margin_top="0.25em",
        ),
        width="100%",
        spacing="1",
    )

def level_acquisition_section() -> rx.Component:
    """
    بخشی که آمار سطوح مختلف کاربران را با نوارهای پیشرفت نمایش می‌دهد.
    """
    return card( # استفاده از کامپوننت کارت که قبلاً ساختیم
        rx.vstack(
            rx.hstack(
                rx.icon("users", size=20, margin_left="0.5em"), # آیکون برای عنوان بخش در RTL
                rx.heading("آمار سطوح کاربران", size="5", weight="medium"),
                align_items="center",
                width="100%",
                margin_bottom="1em", # فاصله زیر عنوان
            ),
            # کامپوننت‌های دیباگ (می‌توانید پس از اطمینان از صحت عملکرد حذف کنید)
            # rx.box(
            #     rx.text(f"سطوح مجاز (AuthState): {AuthState.allowed_levels_for_current_referral.to_string()}"),
            #     rx.text(f"تعداد کاربران بر اساس سطح (MainState): {MainState.user_counts_by_level_var.to_string()}"),
            #     rx.text(f"کل کاربران معرف (MainState): {MainState.total_users_for_current_referral.to_string()}"),
            #     border="1px solid red", padding="0.5em", margin_y="0.5em" # برای مشخص شدن در UI
            # ),
            rx.cond(
                AuthState.allowed_levels_for_current_referral.length() > 0,
                rx.foreach(
                    AuthState.allowed_levels_for_current_referral, # این یک rx.Var[List[str]] است
                    lambda level_key_from_foreach: rx.cond( # نام متغیر لامبدا را تغییر دادم
                        (level_key_from_foreach != NO_LEVEL_VALUE_INTERNAL), # سطح "بدون سطح" را نمایش نده
                        level_progress_item(
                            level_key_from_foreach, # این یک rx.Var[str] است که مقدار یکی از آیتم‌های لیست است
                            MainState.user_counts_by_level_var.get(level_key_from_foreach, 0), # دسترسی به دیکشنری با Var
                            MainState.total_users_for_current_referral
                        ),
                        rx.fragment() # اگر شرط برقرار نبود، چیزی رندر نکن
                    )
                ),
                # اگر هیچ سطح مجازی برای نمایش وجود نداشت
                rx.center(rx.text("سطحی برای نمایش تعریف نشده است.", color_scheme="gray"), height="100px")
            ),
            spacing="4", # فاصله بین آیتم‌های سطوح
            width="100%",
            align_items="stretch", # آیتم‌ها عرض کامل را بگیرند
        )
    )