# marketers_admin_panel/marketers_admin_panel/pages/dashboard.py
import reflex as rx
from ..states.admin_state import AdminState
from ..states.auth_state import AuthState # AuthState را نیز وارد کنید
from ..models.bot_user import BotUser # برای type hinting

def display_bot_user_row(user: BotUser):
    return rx.table.row(
        rx.table.cell(str(user.user_id)),
        rx.table.cell(user.username or "-"),
        rx.table.cell(user.national_id or "-"),
        rx.table.cell(user.referral or "-"),
        rx.table.cell(user.agent_code or "-"),
        rx.table.cell(user.level or "-"),
        rx.table.cell(user.chat_state or "-"),
        rx.table.cell(user.created_at_str),
        rx.table.cell(user.updated_at_str),
        rx.table.cell(user.channels_str),
        rx.table.cell(
            rx.hstack( # اینجا rx_hstack نداشتیم، درست بود
                rx.icon_button(
                    rx.icon("edit"),
                    on_click=lambda: AdminState.start_edit_user(user),
                    color_scheme="blue",
                    variant="soft",
                    size="1"
                ),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.icon_button(rx.icon("trash-2"), color_scheme="red", variant="soft", size="1")
                    ),
                    rx.alert_dialog.content(
                        # فرزندان مستقیما پاس داده می شوند
                        rx.alert_dialog.title("تایید حذف"), # به عنوان فرزند
                        rx.alert_dialog.description( # به عنوان فرزند
                            f"آیا از حذف کاربر {user.username or user.user_id} مطمئن هستید؟ این عمل قابل بازگشت نیست."
                        ),
                        rx.hstack( # به عنوان فرزند
                            rx.alert_dialog.cancel(rx.button("لغو", variant="soft", color_scheme="gray")),
                            rx.alert_dialog.action(
                                rx.button("حذف", on_click=lambda: AdminState.delete_bot_user(user.user_id), color_scheme="red")
                            ),
                            spacing="3",
                            justify="end",
                            margin_top="1em",
                        ),
                        style={"direction": "rtl"}, # این پراپرتی برای content معتبر است
                    ),
                ),
                spacing="1"
            )
        ),
        align="center",
        style={"font_size": "0.8em"}
    )

def edit_user_dialog() -> rx.Component:
    # اگر editing_user تعریف نشده باشد، چیزی رندر نکن
    # یا یک Fragment خالی برگردان تا از خطای NoneType جلوگیری شود.
    if AdminState.editing_user is None:
        return rx.fragment() # یا return None اگر مشکلی ایجاد نکند

    return rx.dialog.root(
        # trigger دیگر اینجا لازم نیست چون از طریق show_edit_dialog کنترل می شود
        rx.dialog.content(
            # فرزندان مستقیма پاس داده می شوند
            rx.dialog.title(f"ویرایش کاربر: {AdminState.editing_user.username or AdminState.editing_user.user_id}"), # به عنوان فرزند
            rx.vstack( # به عنوان فرزند
                rx.form.root(
                    rx.vstack(
                        rx.form.field(
                            rx.hstack(rx.text("نام کاربری تلگرام:"), rx.input(
                                value=AdminState.edit_form_data.get("username", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("username", val),
                                placeholder="نام کاربری"
                            ), width="100%"), name="username_edit"
                        ),
                        rx.form.field(
                            rx.hstack(rx.text("کد ملی:"), rx.input(
                                value=AdminState.edit_form_data.get("national_id", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("national_id", val),
                                placeholder="کد ملی"
                            ), width="100%"), name="national_id_edit"
                        ),
                        rx.form.field(
                            rx.hstack(rx.text("وضعیت چت:"), rx.input(
                                value=AdminState.edit_form_data.get("chat_state", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("chat_state", val),
                                placeholder="وضعیت چت"
                            ), width="100%"), name="chat_state_edit"
                        ),
                        rx.form.field(
                             rx.hstack(rx.text("سطح (Level):"), rx.input(
                                value=AdminState.edit_form_data.get("level", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("level", val),
                                placeholder="سطح"
                            ), width="100%"), name="level_edit"
                        ),
                        rx.cond(
                            AdminState.auth_state.is_logged_in_super_admin,
                            rx.form.field(
                                rx.hstack(rx.text("Referral:"), rx.input(
                                    value=AdminState.edit_form_data.get("referral", ""),
                                    on_change=lambda val: AdminState.handle_edit_form_change("referral", val),
                                    placeholder="Referral"
                                ), width="100%"), name="referral_edit"
                            ),
                            rx.form.field(
                                rx.hstack(rx.text("Referral:"), rx.input(
                                    value=AdminState.edit_form_data.get("referral", ""),
                                    read_only=True,
                                ), width="100%"), name="referral_readonly"
                            )
                        ),
                        rx.form.field(
                            rx.hstack(rx.text("کد ایجنت:"), rx.input(
                                value=AdminState.edit_form_data.get("agent_code", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("agent_code", val),
                                placeholder="کد ایجنت"
                            ), width="100%"), name="agent_code_edit"
                        ),
                        rx.form.field(
                             rx.hstack(rx.text("محدودیت سرمایه:"), rx.input(
                                value=AdminState.edit_form_data.get("capital_limit", ""),
                                on_change=lambda val: AdminState.handle_edit_form_change("capital_limit", val),
                                placeholder="محدودیت سرمایه"
                            ), width="100%"), name="capital_limit_edit"
                        ),
                        rx.form.field(
                            rx.hstack(
                                rx.checkbox(
                                    checked=AdminState.edit_form_data.get("trial_noticed", False),
                                    on_change=lambda checked: AdminState.handle_edit_form_change("trial_noticed", checked),
                                ),
                                rx.text("Trial Noticed"),
                                align_items="center", spacing="2" # align_items به جای align
                            ), name="trial_noticed_edit" # name به form.field داده شود
                        ),
                         rx.form.field(
                            rx.hstack(
                                rx.checkbox(
                                    checked=AdminState.edit_form_data.get("trial_ended", False),
                                    on_change=lambda checked: AdminState.handle_edit_form_change("trial_ended", checked),
                                ),
                                rx.text("Trial Ended"),
                                align_items="center", spacing="2" # align_items به جای align
                            ), name="trial_ended_edit" # name به form.field داده شود
                        ),
                        rx.hstack( # این فرزند مستقیم rx.vstack است
                            rx.button("لغو", on_click=AdminState.set_show_edit_dialog(False), variant="soft", color_scheme="gray"),
                            rx.button("ذخیره تغییرات", on_click=AdminState.save_user_changes),
                            spacing="3",
                            margin_top="1em",
                            justify="end",
                            width="100%"
                        ),
                        spacing="3",
                        width="100%"
                    ),
                    width="100%"
                ) # پایان form.root
            ), # پایان rx.vstack داخلی
            style={"direction": "rtl"}, # این پراپرتی برای content معتبر است
            width="clamp(300px, 80vw, 600px)"
        ), # پایان dialog.content
        open=AdminState.show_edit_dialog,
        on_open_change=AdminState.set_show_edit_dialog
    )

def pagination_ui() -> rx.Component:
    # ... (این بخش بدون تغییر به نظر می رسد، اما اگر از rx.button استفاده می کنید،
    # آرگومان های موقعیتی (فرزندان) باید قبل از کلیدواژه ای ها باشند)
    page_numbers_to_show = 5
    start_page = max(1, AdminState.current_page - page_numbers_to_show // 2)
    end_page = min(AdminState.total_pages, start_page + page_numbers_to_show - 1)
    if end_page - start_page + 1 < page_numbers_to_show:
        start_page = max(1, end_page - page_numbers_to_show + 1)

    return rx.hstack(
        rx.button(rx.icon("chevrons-left"), on_click=AdminState.go_to_page(1), disabled=AdminState.current_page == 1, variant="outline", size="1"),
        rx.button(rx.icon("chevron-left"), on_click=AdminState.prev_page, disabled=AdminState.current_page == 1, variant="outline", size="1"),
        rx.cond(start_page > 1, rx.text("...")),
        rx.foreach(
            list(range(start_page, end_page + 1)),
            lambda page_num: rx.button(
                str(page_num), # فرزند
                on_click=AdminState.go_to_page(page_num),
                is_active=AdminState.current_page == page_num,
                variant="outline" if AdminState.current_page != page_num else "solid",
                size="1"
            )
        ),
        rx.cond(end_page < AdminState.total_pages, rx.text("...")),
        rx.button(rx.icon("chevron-right"), on_click=AdminState.next_page, disabled=AdminState.current_page == AdminState.total_pages, variant="outline", size="1"),
        rx.button(rx.icon("chevrons-right"), on_click=AdminState.go_to_page(AdminState.total_pages), disabled=AdminState.current_page == AdminState.total_pages, variant="outline", size="1"),
        spacing="1",
        align_items="center", # به جای align
        justify_content="center", # به جای justify
        margin_top="1em",
        flex_wrap="wrap"
    )

def dashboard_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(f"پنل مدیریت کاربران - Referral: {AuthState.logged_in_admin_referral_type if AuthState.logged_in_admin_referral_type else 'همه'}", size="5"),
            rx.spacer(),
            rx.text(f"ادمین: {AuthState.logged_in_admin_username}", size="2"),
            rx.button("خروج", on_click=AuthState.logout, color_scheme="red", variant="soft", size="2"),
            width="100%",
            padding_y="0.5em",
            padding_x="1em",
            border_bottom="1px solid var(--gray-a3)",
            bg="var(--gray-a1)",
            align_items="center", # به جای align
        ),
        rx.vstack(
            rx.input(
                placeholder="جستجو (نام کاربری، کد ملی، User ID, Referral, Level...)",
                on_change=AdminState.set_search_term,
                value=AdminState.search_term,
                width="100%",
                size="2",
                margin_bottom="1em"
            ),
            rx.cond(
                AdminState.is_loading,
                rx.center(rx.spinner(size="3"), width="100%", height="200px"),
                rx.box(
                    rx.table.root(
                        rx.table.header(
                            rx.table.row(
                                rx.table.column_header_cell("ID"),
                                rx.table.column_header_cell("نام کاربری"),
                                rx.table.column_header_cell("کد ملی"),
                                rx.table.column_header_cell("Referral"),
                                rx.table.column_header_cell("Agent"),
                                rx.table.column_header_cell("Level"),
                                rx.table.column_header_cell("وضعیت چت"),
                                rx.table.column_header_cell("ایجاد"),
                                rx.table.column_header_cell("بروزرسانی"),
                                rx.table.column_header_cell("کانال‌ها"),
                                rx.table.column_header_cell("عملیات"),
                            )
                        ),
                        rx.table.body(
                            rx.foreach(AdminState.paginated_users, display_bot_user_row)
                        ),
                        variant="surface",
                        size="1",
                    ),
                    pagination_ui(),
                    width="100%",
                    overflow_x="auto"
                )
            ),
            edit_user_dialog(),
            width="100%",
            spacing="4",
        ),
        style={"direction": "rtl"},
        align_items="stretch", # به جای align
        width="100%",
        padding="1em",
        on_mount=AdminState.on_dashboard_load
    )