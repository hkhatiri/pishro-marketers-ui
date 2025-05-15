import datetime
import reflex as rx

from ..backend.backend import MongoUserDisplay, State, ChatState, CHAT_STATE_TRANSLATIONS
from ..components.form_field import form_field
from ..components.status_badges import channel_membership_badge


def show_customer(user: MongoUserDisplay):
    object_id_str_for_actions = user.get('_id_str', "")
    # نمایش مقدار فارسی وضعیت کاربر در جدول
    chat_state_fa_display_in_table = user.get('chat_state_fa', user.get('raw_chat_state', '-'))


    return rx.table.row(
        rx.table.cell(user.get('username', '-')),
        rx.table.cell(user.get('national_id', '-')),
        rx.table.cell(chat_state_fa_display_in_table), 
        rx.table.cell(user.get('created_at_str', '-')),
        rx.table.cell(channel_membership_badge(user.get('channel_count', 0))),
        rx.table.cell(
            rx.hstack(
                update_customer_dialog(user, object_id_str_for_actions),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_customer(object_id_str_for_actions),
                    size="2", variant="solid", color_scheme="red",
                    disabled=(object_id_str_for_actions == "")
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}}, align="center",
    )

def add_customer_button() -> rx.Component:
    # گزینه‌های فارسی برای select در فرم افزودن
    # به صورت لیست تاپل (لیبل_فارسی, مقدار_انگلیسی)
    chat_state_options_add = [
        (CHAT_STATE_TRANSLATIONS.get(state.name, state.name), state.name) 
        for state in ChatState
    ]
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("plus", size=26), rx.text("افزودن کاربر", size="4", display=["none", "none", "block"]), size="3"),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(rx.icon(tag="users", size=34), color_scheme="grass", radius="full", padding="0.65rem"),
                rx.vstack(
                    rx.dialog.title("افزودن کاربر جدید", weight="bold", margin="0"),
                    rx.dialog.description("اطلاعات کاربر جدید را وارد کنید"),
                    spacing="1", height="100%", align_items="start",
                ),
                height="100%", spacing="4", margin_bottom="1.5em", align_items="center", width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        form_field("نام کاربری", "نام کاربری", "text", "username", "user", required=True),
                        form_field("کد ملی", "کد ملی (اختیاری)", "text", "national_id", "credit-card"),
                        rx.vstack(
                            rx.hstack(rx.icon("user-cog", size=16, stroke_width=1.5), rx.text("وضعیت کاربر"), align="center", spacing="2"),
                            rx.select.root( 
                                rx.select.trigger(placeholder="انتخاب وضعیت..."),
                                rx.select.content(
                                    *[
                                        rx.select.item(label, value=value)
                                        for label, value in chat_state_options_add # استفاده از لیست تاپل‌ها
                                    ]
                                ),
                                name="chat_state", 
                                default_value=ChatState.HasAccess.name, # مقدار انگلیسی
                                width="100%",
                                size="3", 
                            ),
                            width="100%", spacing="1",
                        ),
                        direction="column", spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(rx.button("لغو", variant="soft", color_scheme="gray")),
                        rx.form.submit(rx.dialog.close(rx.button("ثبت کاربر")), as_child=True),
                        padding_top="2em", spacing="3", mt="4", justify="end",
                    ),
                    on_submit=State.add_customer_to_db, reset_on_submit=True,
                ),
                width="100%", direction="column", spacing="4",
            ),
            max_width="450px", padding="1.5em", border=f"2px solid {rx.color('accent', 7)}", border_radius="25px",
        ),
    )


def update_customer_dialog(user_row_data: MongoUserDisplay, object_id_for_trigger: str):
    # گزینه‌های فارسی برای select در فرم ویرایش
    chat_state_options_edit = [
        (CHAT_STATE_TRANSLATIONS.get(state.name, state.name), state.name)
        for state in ChatState
    ]
    
    # default_value باید مقدار انگلیسی (value) باشد.
    # این مقدار از State.current_user_for_edit.raw_chat_state خوانده می‌شود.
    # استفاده از rx.Var برای default_value که خود به یک فیلد از rx.Var دیگر (current_user_for_edit) اشاره دارد.
    default_chat_state_english_for_edit_form = rx.cond(
        State.current_user_for_edit, # بررسی وجود current_user_for_edit
        State.current_user_for_edit.get("raw_chat_state", ChatState.HasAccess.name), # اگر وجود دارد، مقدار raw_chat_state
        ChatState.HasAccess.name # مقدار پیش‌فرض اگر current_user_for_edit هنوز None است
    )

    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("square-pen", size=22), rx.text("ویرایش", size="3"), color_scheme="blue", size="2", variant="solid",
                on_click=lambda: State.set_current_user_for_edit(object_id_for_trigger),
                disabled=(object_id_for_trigger == "")
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
                    State.current_user_for_edit, # فرم فقط زمانی رندر شود که current_user_for_edit مقدار دارد
                    rx.form.root(
                        rx.flex(
                            rx.vstack(
                                rx.hstack(rx.icon("fingerprint", size=16), rx.text("شناسه داخلی (فقط خواندنی)", weight="medium")),
                                rx.input(value=State.current_user_for_edit.get("_id_str", ""), disabled=True, width="100%"),
                                align_items="start", width="100%", spacing="1", margin_bottom="0.75em"
                            ),
                            form_field("نام کاربری", "نام کاربری", "text", "username", "user",
                                       default_value=State.current_user_for_edit.get("username", ""), # خواندن مستقیم از State
                                       required=True),
                            form_field("کد ملی", "کد ملی (اختیاری)", "text", "national_id", "credit-card",
                                       default_value=State.current_user_for_edit.get("national_id", "")),
                            rx.vstack(
                                rx.hstack(rx.icon("user-cog", size=16, stroke_width=1.5), rx.text("وضعیت کاربر"), align="center", spacing="2"),
                                rx.select.root( 
                                    rx.select.trigger(placeholder="انتخاب وضعیت..."),
                                    rx.select.content(
                                        *[
                                            rx.select.item(label, value=value)
                                            for label, value in chat_state_options_edit # استفاده از لیست تاپل‌ها
                                        ]
                                    ),
                                    name="chat_state",
                                    # default_value باید مقدار انگلیسی (value) باشد
                                    default_value=default_chat_state_english_for_edit_form, 
                                    width="100%",
                                    size="3",
                                ),
                                width="100%", spacing="1",
                            ),
                            direction="column", spacing="3",
                        ),
                        rx.flex(
                            rx.dialog.close(rx.button("لغو", variant="soft", color_scheme="gray", on_click=State.clear_current_user_for_edit)),
                            rx.form.submit(rx.dialog.close(rx.button("به‌روزرسانی کاربر")), as_child=True),
                            padding_top="2em", spacing="3", mt="4", justify="end",
                        ),
                        on_submit=State.update_customer_to_db,
                        reset_on_submit=False,
                    ),
                    rx.center(rx.text("..."), width="100%", height="200px")
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
        rx.button(rx.icon(tag="chevrons-left"), "اولین",on_click=State.first_page_handler,disabled=State.current_page_number <= 1,size="2", variant="outline"),
        rx.button(rx.icon(tag="chevron-left"), "قبلی",on_click=State.prev_page_handler,disabled=State.current_page_number <= 1,size="2", variant="outline"),
        rx.text("صفحه ", State.current_page_number.to_string(), " از ", State.total_pages.to_string(),size="3"),
        rx.button("بعدی", rx.icon(tag="chevron-right"),on_click=State.next_page_handler,disabled=State.current_page_number >= State.total_pages,size="2", variant="outline"),
        rx.button("آخرین", rx.icon(tag="chevrons-right"),on_click=State.last_page_handler,disabled=State.current_page_number >= State.total_pages,size="2", variant="outline"),
        justify="center", align="center", spacing="3", width="100%", padding_y="1em",
    )

def main_table():
    return rx.fragment(
        rx.flex(
            add_customer_button(), rx.spacer(),
            rx.cond(State.sort_reverse, rx.icon("arrow-down-z-a", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort),
                      rx.icon("arrow-down-a-z", size=28, stroke_width=1.5, cursor="pointer", on_click=State.toggle_sort)),
            rx.select(
                ["username", "national_id", "raw_chat_state", "created_at_str", "channel_count"],
                placeholder="مرتب‌سازی بر اساس: نام کاربری", default_value="username", size="3",
                on_change=State.sort_values,
            ),
            rx.input(rx.input.slot(rx.icon("search")), placeholder="جستجوی کاربران...", size="3", max_width="225px", width="100%", variant="surface",
                on_change=State.filter_values, value=State.search_value,
            ),
            justify="end", align="center", spacing="3", wrap="wrap", width="100%", padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("نام کاربری", "user"),
                    _header_cell("کد ملی", "credit-card"),
                    _header_cell("وضعیت کاربر", "user-cog"), 
                    _header_cell("تاریخ عضویت", "calendar"),
                    _header_cell("وضعیت عضویت", "users"),
                    _header_cell("عملیات", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.paginated_users, show_customer)),
            variant="surface", size="3", width="100%",
        ),
        _pagination_controls(),
    )
