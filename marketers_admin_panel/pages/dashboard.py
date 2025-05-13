import reflex as rx
from ..states.admin_state import AdminState
from ..states.auth_state import AuthState
from ..models.bot_user import BotUser

def display_bot_user_row(user: BotUser): # user در اینجا rx.Var[BotUser] است
    return rx.table.row(
        rx.table.cell(user.user_id.to_string()),
        rx.table.cell(rx.cond(user.username.is_not_none(), user.username, "-")),
        rx.table.cell(rx.cond(user.national_id.is_not_none(), user.national_id, "-")),
        rx.table.cell(rx.cond(user.referral.is_not_none(), user.referral, "-")),
        rx.table.cell(rx.cond(user.agent_code.is_not_none(), user.agent_code, "-")),
        rx.table.cell(rx.cond(user.level.is_not_none(), user.level, "-")),
        rx.table.cell(rx.cond(user.chat_state.is_not_none(), user.chat_state, "-")),
        rx.table.cell(rx.cond(user.created_at_str.is_not_none(), user.created_at_str, "-")),
        rx.table.cell(rx.cond(user.updated_at_str.is_not_none(), user.updated_at_str, "-")),
        rx.table.cell(rx.cond(user.level_checked_at_str.is_not_none(), user.level_checked_at_str, "-")),
        rx.table.cell(rx.cond(user.channels_str.is_not_none(), user.channels_str, "-")),
        rx.table.cell(rx.cond(user.trial_status_str.is_not_none(), user.trial_status_str, "-")),
        rx.table.cell(
            rx.hstack(
                rx.icon_button(
                    rx.icon("pencil", size=16), # آیکن اصلاح شده
                    on_click=AdminState.start_edit_user(user),
                    color_scheme="blue", variant="soft", size="1"
                ),
                rx.alert_dialog.root(
                    rx.alert_dialog.trigger(
                        rx.icon_button(rx.icon("trash-2", size=16), color_scheme="red", variant="soft", size="1")
                    ),
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("تایید حذف"),
                        rx.alert_dialog.description(
                            rx.text(
                                "آیا از حذف کاربر ",
                                rx.cond(user.username.is_not_none(), user.username, user.user_id.to_string()),
                                " با کد معرف ",
                                rx.cond(user.referral.is_not_none(), user.referral, "نامشخص"),
                                " مطمئن هستید؟ این عمل قابل بازگشت نیست."
                            )
                        ),
                        rx.hstack(
                            rx.alert_dialog.cancel(rx.button("لغو", variant="soft", color_scheme="gray")),
                            rx.alert_dialog.action(
                                rx.button("حذف", on_click=AdminState.delete_bot_user(user.user_id), color_scheme="red")
                            ),
                            spacing="3", justify_content="end", margin_top="1em",
                        ),
                        style={"direction": "rtl"},
                    ),
                ),
                spacing="1"
            )
        ),
        align="center", style={"font_size": "0.75em"}
    )

def edit_user_dialog() -> rx.Component:
    dialog_title_content = rx.cond(
        AdminState.editing_user.is_not_none(),
        rx.text(
            "ویرایش کاربر: ",
            rx.cond(AdminState.editing_user.username.is_not_none(), AdminState.editing_user.username, ""),
            " (ID: ",
            rx.cond(AdminState.editing_user.user_id.is_not_none(), AdminState.editing_user.user_id.to_string(), ""),
            ")"
        ),
        "ویرایش کاربر"
    )
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(dialog_title_content),
            rx.form.root(
                rx.vstack(
                    rx.form.field(rx.flex(rx.text("نام کاربری تلگرام:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("username", ""),on_change=lambda val: AdminState.handle_edit_form_change("username", val), placeholder="نام کاربری"), direction="row", align_items="center", width="100%"), name="username_edit"),
                    rx.form.field(rx.flex(rx.text("کد ملی:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("national_id", ""),on_change=lambda val: AdminState.handle_edit_form_change("national_id", val), placeholder="کد ملی"), direction="row", align_items="center", width="100%"), name="national_id_edit"),
                    rx.form.field(rx.flex(rx.text("وضعیت چت:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("chat_state", ""),on_change=lambda val: AdminState.handle_edit_form_change("chat_state", val), placeholder="وضعیت چت"), direction="row", align_items="center", width="100%"), name="chat_state_edit"),
                    rx.form.field(rx.flex(rx.text("سطح (Level):", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("level", ""),on_change=lambda val: AdminState.handle_edit_form_change("level", val), placeholder="سطح"), direction="row", align_items="center", width="100%"), name="level_edit"),
                    rx.cond(
                        AdminState.is_current_admin_super_admin,
                        rx.form.field(rx.flex(rx.text("Referral:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("referral", ""),on_change=lambda val: AdminState.handle_edit_form_change("referral", val), placeholder="Referral"), direction="row", align_items="center", width="100%"), name="referral_edit"),
                        rx.form.field(rx.flex(rx.text("Referral:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("referral", ""), read_only=True), direction="row", align_items="center", width="100%"), name="referral_readonly")
                    ),
                    rx.form.field(rx.flex(rx.text("کد ایجنت:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("agent_code", ""),on_change=lambda val: AdminState.handle_edit_form_change("agent_code", val), placeholder="کد ایجنت"), direction="row", align_items="center", width="100%"), name="agent_code_edit"),
                    rx.form.field(rx.flex(rx.text("محدودیت سرمایه:", width="130px", text_align="right", margin_left="1em"), rx.input(value=AdminState.edit_form_data.get("capital_limit", ""),on_change=lambda val: AdminState.handle_edit_form_change("capital_limit", val), placeholder="محدودیت سرمایه"), direction="row", align_items="center", width="100%"), name="capital_limit_edit"),
                    rx.form.field(rx.hstack(rx.checkbox(id="trial_noticed_checkbox", checked=AdminState.edit_form_data.get("trial_noticed", False),on_change=lambda checked: AdminState.handle_edit_form_change("trial_noticed", checked)), rx.form.label("Trial Noticed", html_for="trial_noticed_checkbox"),align_items="center", spacing="2", width="100%", justify_content="start"), name="trial_noticed_edit"),
                    rx.form.field(rx.hstack(rx.checkbox(id="trial_ended_checkbox", checked=AdminState.edit_form_data.get("trial_ended", False),on_change=lambda checked: AdminState.handle_edit_form_change("trial_ended", checked)), rx.form.label("Trial Ended", html_for="trial_ended_checkbox"),align_items="center", spacing="2", width="100%", justify_content="start"), name="trial_ended_edit"),
                    rx.hstack(
                        rx.button("لغو", on_click=AdminState.set_show_edit_dialog(False), variant="soft", color_scheme="gray"),
                        rx.form.submit(rx.button("ذخیره تغییرات", type="submit"), as_child=True),
                        spacing="3", margin_top="1.5em", justify_content="end", width="100%"
                    ),
                    spacing="3", width="100%"
                ),
                on_submit=AdminState.save_user_changes,
                width="100%"
            ),
            style={"direction": "rtl"}, width="clamp(380px, 90vw, 700px)", max_height="85vh", overflow_y="auto"
        ),
        open=AdminState.show_edit_dialog,
        on_open_change=AdminState.set_show_edit_dialog
    )

def pagination_ui() -> rx.Component:
    return rx.hstack(
        rx.button(rx.icon("chevrons-right", style={"transform": "rotate(180deg)"}), on_click=AdminState.go_to_page("1"), disabled=AdminState.current_page <= 1, variant="outline", size="1"),
        rx.button(rx.icon("chevron-right", style={"transform": "rotate(180deg)"}), on_click=AdminState.prev_page, disabled=AdminState.current_page <= 1, variant="outline", size="1"),
        rx.text(f"صفحه {AdminState.current_page} از {AdminState.total_pages}", padding_x="1em", size="2", weight="medium"),
        rx.button(rx.icon("chevron-left", style={"transform": "rotate(180deg)"}), on_click=AdminState.next_page, disabled=AdminState.current_page >= AdminState.total_pages, variant="outline", size="1"),
        rx.button(rx.icon("chevrons-left", style={"transform": "rotate(180deg)"}), on_click=AdminState.go_to_page(AdminState.total_pages.to_string()), disabled=AdminState.current_page >= AdminState.total_pages, variant="outline", size="1"),
        spacing="1", align_items="center", justify_content="center", margin_top="1em", flex_wrap="wrap"
    )

def dashboard_page() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading(
                rx.text.strong("پنل مدیریت کاربران - Referral: "),
                rx.cond(
                    AdminState.current_admin_referral_type.is_not_none(),
                    AdminState.current_admin_referral_type,
                    "همه"
                ),
                size="5"
            ),
            rx.spacer(),
            rx.text(
                "ادمین: ",
                rx.cond(
                    AdminState.current_admin_username.is_not_none(),
                    AdminState.current_admin_username,
                    "ناشناس"
                ),
                size="2", weight="bold"
            ),
            rx.button("خروج", on_click=AuthState.logout, color_scheme="red", variant="soft", size="2"),
            width="100%", padding_y="0.75em", padding_x="1em",
            border_bottom="1px solid var(--gray-a4)", bg="var(--gray-a1)", align_items="center",
        ),
        rx.vstack(
            rx.input(
                placeholder="جستجو (نام کاربری، کد ملی، User ID, Referral, Level, وضعیت چت)",
                on_change=AdminState.set_search_term,
                value=AdminState.search_term,
                width="100%", size="2", margin_bottom="1em", variant="surface"
            ),
            rx.cond(
                AdminState.is_loading,
                rx.center(rx.spinner(size="3"), width="100%", min_height="300px"),
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
                                rx.table.column_header_cell("چک Level"),
                                rx.table.column_header_cell("کانال‌ها"),
                                rx.table.column_header_cell("وضعیت Trial"),
                                rx.table.column_header_cell("عملیات"),
                            )
                        ),
                        rx.table.body(
                            rx.foreach(AdminState.paginated_users, display_bot_user_row)
                        ),
                        variant="surface", size="1",
                    ),
                    rx.cond(
                        (AdminState.filtered_bot_users.length() == 0) & ~AdminState.is_loading,
                        rx.center(
                            rx.text(
                                rx.cond(
                                    AdminState.search_term != "",
                                    "نتیجه‌ای برای جستجوی شما یافت نشد.",
                                    "کاربری برای نمایش وجود ندارد."
                                ),
                                color_scheme="gray"
                            ),
                            padding_y="2em"
                        )
                    ),
                    pagination_ui(),
                    width="100%", overflow_x="auto"
                )
            ),
            edit_user_dialog(),
            width="100%", spacing="4",
        ),
        style={"direction": "rtl"}, align_items="stretch", width="100%", padding="1em",
    )