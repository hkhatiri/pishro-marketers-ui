# customer_data/views/table.py
import datetime
from typing import Optional
import reflex as rx

try:
    from ..backend.backend import MongoUserDisplay, State, ChatState, CHAT_STATE_TRANSLATIONS
    from ..backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL
except ImportError:
    # فال‌بک‌ها
    from customer_data.backend.backend import MongoUserDisplay, State, ChatState, CHAT_STATE_TRANSLATIONS # type: ignore
    from customer_data.backend.auth_state import AuthState, LEVEL_TRANSLATIONS, NO_LEVEL_VALUE_INTERNAL # type: ignore

from ..components.form_field import form_field
from ..components.status_badges import channel_membership_badge

def display_level_string(level_var: rx.Var[Optional[str]]) -> rx.Var[str]:
    return rx.cond(
        level_var.is_not_none() & (level_var != ""),
        rx.cond(
            level_var == NO_LEVEL_VALUE_INTERNAL,
            LEVEL_TRANSLATIONS.get(NO_LEVEL_VALUE_INTERNAL, "-"),
            LEVEL_TRANSLATIONS.get(level_var, level_var.replace("level_", "")),
        ),
        "-"
    )

def show_customer(user: MongoUserDisplay): # user اینجا یک rx.Var از MongoUserDisplay است
    object_id_var = user.get('_id_str', "") # این یک rx.Var[str] است
    return rx.table.row(
        rx.table.cell(user.get('username', '-')),
        rx.table.cell(user.get('national_id', '-')),
        rx.table.cell(user.get('chat_state_fa', user.get('raw_chat_state', '-'))),
        rx.table.cell(display_level_string(user.get('level'))),
        rx.table.cell(user.get('created_at_str', '-')), # این باید شمسی باشد
        rx.table.cell(channel_membership_badge(user.get('channel_count', 0))),
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(object_id_var), # پاس دادن rx.Var[str]
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_customer(object_id_var), # type: ignore
                    size="2", variant="solid", color_scheme="red",
                    disabled=(object_id_var == "")
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}}, align="center",
    )


def update_customer_dialog(object_id_var: rx.Var[str]):
    chat_state_options_for_edit_dropdown = [
        (label, state_name) for state_name, label in CHAT_STATE_TRANSLATIONS.items()
    ]
    level_options_for_edit_dropdown = AuthState.level_options_for_dropdown

    default_chat_state = rx.cond(State.current_user_for_edit.is_not_none(), State.current_user_for_edit.get("raw_chat_state", ChatState.HasAccess.name), ChatState.HasAccess.name) # type: ignore
    default_level = rx.cond(State.current_user_for_edit.is_not_none(), State.current_user_for_edit.get("level", NO_LEVEL_VALUE_INTERNAL), NO_LEVEL_VALUE_INTERNAL) # type: ignore
    current_username = rx.cond(State.current_user_for_edit.is_not_none(), State.current_user_for_edit.get("username", ""), "") # type: ignore
    current_national_id = rx.cond(State.current_user_for_edit.is_not_none(), State.current_user_for_edit.get("national_id", ""), "") # type: ignore
    current_id_str = rx.cond(State.current_user_for_edit.is_not_none(), State.current_user_for_edit.get("_id_str", ""), "") # type: ignore

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("square-pen", size=22), rx.text("ویرایش", size="3"), color_scheme="blue", size="2", variant="solid",
                on_click=State.set_current_user_for_edit(object_id_var), # type: ignore
                disabled=(object_id_var == "")
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(rx.icon(tag="square-pen", size=34), color_scheme="grass", radius="full", padding="0.65rem"),
                rx.vstack(
                    rx.dialog.title("ویرایش کاربر", weight="bold", margin="0"),
                    rx.dialog.description("اطلاعات کاربر را ویرایش کنید"),
                    spacing="1", height="100%", align_items="start",
                ),
                height="100%", spacing="4", margin_bottom="1.5em", align_items="center", width="100%",
            ),
            rx.flex(
                rx.cond(
                    State.current_user_for_edit.is_not_none(),
                    rx.form.root(
                        rx.flex(
                            rx.vstack(
                                rx.hstack(rx.icon("fingerprint", size=16), rx.text("شناسه داخلی (فقط خواندنی)", weight="medium")),
                                rx.input(value=current_id_str, disabled=True, width="100%"),
                                align_items="start", width="100%", spacing="1", margin_bottom="0.75em"
                            ),
                            form_field("نام کاربری", "نام کاربری", "text", "username", "user", default_value=current_username, required=True),
                            form_field("کد ملی", "کد ملی (اختیاری)", "text", "national_id", "credit-card", default_value=current_national_id),
                            rx.vstack(
                                rx.hstack(rx.icon("user-cog", size=16, stroke_width=1.5), rx.text("وضعیت کاربر"), align="center", spacing="2"),
                                rx.select.root(
                                    rx.select.trigger(placeholder="انتخاب وضعیت..."),
                                    rx.select.content(*[rx.select.item(label, value=value) for label, value in chat_state_options_for_edit_dropdown]),
                                    name="chat_state", default_value=default_chat_state, width="100%", size="3",
                                ), width="100%", spacing="1",
                            ),
                            rx.vstack(
                                rx.hstack(rx.icon("bar-chart-2", size=16, stroke_width=1.5), rx.text("سطح کاربر"), align="center", spacing="2"),
                                rx.select.root(
                                    rx.select.trigger(placeholder="انتخاب سطح..."),
                                    rx.select.content(rx.foreach(level_options_for_edit_dropdown, lambda opt: rx.select.item(opt[0], value=opt[1]))),
                                    name="level", default_value=default_level, width="100%", size="3",
                                ), width="100%", spacing="1",
                            ),
                            direction="column", spacing="3",
                        ),
                        rx.flex(
                            rx.dialog.close(rx.button("لغو", variant="soft", color_scheme="gray", on_click=State.clear_current_user_for_edit)), # type: ignore
                            rx.form.submit(rx.dialog.close(rx.button("به‌روزرسانی کاربر")), as_child=True),
                            padding_top="2em", spacing="3", mt="4", justify="end",
                        ),
                        on_submit=State.update_customer_to_db, reset_on_submit=False, # type: ignore
                    ),
                    rx.center(rx.text("کاربری برای ویرایش انتخاب نشده یا در حال بارگذاری است..."), width="100%", height="200px")
                ),
                width="100%", direction="column", spacing="4",
            ),
            max_width="450px", padding="1.5em", border=f"2px solid {rx.color('accent', 7)}", border_radius="25px",
        ),
    )

def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(rx.hstack(rx.icon(icon, size=18), rx.text(text), align="center", spacing="2"))

def _pagination_controls() -> rx.Component:
    return rx.hstack(
        rx.button(rx.icon(tag="chevrons-left"), "اولین",on_click=State.first_page_handler,disabled=State.current_page_number <= 1,size="2", variant="outline"), # type: ignore
        rx.button(rx.icon(tag="chevron-left"), "قبلی",on_click=State.prev_page_handler,disabled=State.current_page_number <= 1,size="2", variant="outline"), # type: ignore
        rx.text("صفحه ", State.current_page_number.to_string(), " از ", State.total_pages.to_string(),size="3"),
        rx.button("بعدی", rx.icon(tag="chevron-right"),on_click=State.next_page_handler,disabled=State.current_page_number >= State.total_pages,size="2", variant="outline"), # type: ignore
        rx.button("آخرین", rx.icon(tag="chevrons-right"),on_click=State.last_page_handler,disabled=State.current_page_number >= State.total_pages,size="2", variant="outline"), # type: ignore
        justify="center", align="center", spacing="3", width="100%", padding_y="1em",
    )

def main_table():
    # تعریف گزینه‌ها برای Select مرتب‌سازی
    sort_options = [
        ("created_at_ts", "تاریخ عضویت"), # مقدار برای بک‌اند، لیبل برای نمایش
        ("username", "نام کاربری"),
        ("national_id", "کد ملی"),
        ("raw_chat_state", "وضعیت کاربر"), # این باید با کلیدهای MongoUserDisplay مطابقت داشته باشد
        ("level", "سطح"),
        ("channel_count", "تعداد کانال")
    ]

    return rx.fragment(
        rx.flex(
            rx.spacer(),
            rx.cond(State.sort_reverse, rx.icon("arrow-down-z-a", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort), # type: ignore
                      rx.icon("arrow-down-a-z", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort)), # type: ignore
            
            # --- اصلاح rx.select برای مرتب‌سازی ---
            rx.select.root(
                rx.select.trigger(placeholder="مرتب‌سازی بر اساس..."),
                rx.select.content(
                    # برای هر آیتم در sort_options، یک SelectItem ایجاد می‌کنیم
                    # لیبل فارسی نمایش داده می‌شود، ولی مقدار انگلیسی (value) به on_value_change ارسال می‌شود
                    *[rx.select.item(label, value=value) for value, label in sort_options]
                ),
                default_value=State.sort_value, # این باید یک @rx.var باشد که مقدار پیش‌فرض را نگه می‌دارد
                on_change=State.sort_values, # تغییر به on_change اگر on_value_change خطا می‌دهد
                                            # یا اطمینان از اینکه sort_values می‌تواند value را بپذیرد
                name="sort_selector", # اضافه کردن name
                size="3",
            ),
            # --- پایان اصلاح rx.select ---
            
            rx.input(rx.input.slot(rx.icon("search")), placeholder="جستجوی کاربران...", size="3", max_width="225px", width="100%", variant="surface",
                on_change=State.filter_values, value=State.search_value, # type: ignore
            ),
            justify="end", align="center", spacing="3", wrap="wrap", width="100%", padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("نام کاربری", "user"),
                    _header_cell("کد ملی", "credit-card"),
                    _header_cell("وضعیت کاربر", "user-cog"),
                    _header_cell("سطح", "bar-chart-horizontal-big"),
                    _header_cell("تاریخ عضویت", "calendar"), # این ستون created_at_str را نمایش می‌دهد
                    _header_cell("وضعیت عضویت", "users"),
                    _header_cell("عملیات", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.paginated_users, show_customer)),
            variant="surface", size="3", width="100%",
        ),
        _pagination_controls(),
    )