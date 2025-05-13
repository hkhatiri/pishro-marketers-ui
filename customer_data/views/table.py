import reflex as rx
from ..backend.backend import UserBase, State, ChatState
from ..components.form_field import form_field
from ..components.status_badges import status_badge

def show_user(user: UserBase):
    """Show a user in a table row."""
    return rx.table.row(
        rx.table.cell(str(user.user_id)),
        rx.table.cell(user.username or ""),
        rx.table.cell(user.national_id or ""),
        rx.table.cell(
            status_badge(user.chat_state or "INITED")
        ),
        rx.table.cell(
            rx.hstack(
                update_user_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: State.delete_user(user.user_id),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},
        align="center",
    )

def add_user_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add User", size="4", display=["none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title("Add New User", weight="bold", margin="0"),
                    rx.dialog.description("Fill the form with the user's info"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        form_field("User ID", "Unique ID", "number", "user_id", "hash"),
                        form_field("Username", "User Name", "text", "username", "user"),
                        form_field("National ID", "National ID", "text", "national_id", "id-card"),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("user-check", size=16, stroke_width=1.5),
                                rx.text("Chat State"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                [state.name for state in ChatState],
                                name="chat_state",
                                direction="row",
                                default_value=ChatState.INITED.name,
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit User"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_user_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )

def update_user_dialog(user: UserBase):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Edit", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                on_click=lambda: State.get_user(user),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title("Edit User", weight="bold", margin="0"),
                    rx.dialog.description("Edit the user's info"),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        form_field(
                            "Username",
                            "User Name",
                            "text",
                            "username",
                            "user",
                            user.username or "",
                        ),
                        form_field(
                            "National ID",
                            "National ID",
                            "text",
                            "national_id",
                            "id-card",
                            user.national_id or "",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("user-check", size=16, stroke_width=1.5),
                                rx.text("Chat State"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                [state.name for state in ChatState],
                                default_value=user.chat_state or ChatState.INITED.name,
                                name="chat_state",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button("Cancel", variant="soft", color_scheme="gray"),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update User"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.update_user_to_db,
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )

def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )

def main_table():
    return rx.fragment(
        rx.flex(
            add_user_button(),
            rx.spacer(),
            rx.cond(
                State.sort_reverse,
                rx.icon(
                    "arrow-down-z-a",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
                rx.icon(
                    "arrow-down-a-z",
                    size=28,
                    stroke_width=1.5,
                    cursor="pointer",
                    on_click=State.toggle_sort,
                ),
            ),
            rx.select(
                ["user_id", "username", "national_id", "chat_state"],
                placeholder="Sort By: Username",
                size="3",
                on_change=lambda sort_value: State.sort_values(sort_value),
            ),
            rx.input(
                rx.input.slot(rx.icon("search")),
                placeholder="Search here...",
                size="3",
                max_width="225px",
                width="100%",
                variant="surface",
                on_change=lambda value: State.filter_values(value),
            ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("User ID", "hash"),
                    _header_cell("Username", "user"),
                    _header_cell("National ID", "id-card"),
                    _header_cell("Chat State", "user-check"),
                    _header_cell("Actions", "cog"),
                ),
            ),
            rx.table.body(rx.foreach(State.users, show_user)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )