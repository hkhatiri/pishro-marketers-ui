import reflex as rx

def form_field(
    label: str, # این لیبل فارسی خواهد بود
    placeholder: str, # این placeholder فارسی خواهد بود
    type: str,
    name: str, # نام انگلیسی برای ارجاع در backend
    icon: str,
    default_value: rx.Var[str] | str = "",
    required: bool = False, # پارامتر required اضافه شد
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.hstack(
                rx.icon(icon, size=16, stroke_width=1.5),
                rx.form.label(label), # نمایش لیبل فارسی
                align="center",
                spacing="2",
            ),
            rx.form.control(
                rx.input(
                    placeholder=placeholder, # نمایش placeholder فارسی
                    type=type,
                    default_value=default_value,
                    name=name,
                    required=required, # استفاده از پارامتر required
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name, # نام فیلد برای rx.form.field باید انگلیسی بماند
        width="100%",
    )