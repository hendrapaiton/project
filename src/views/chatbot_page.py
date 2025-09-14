import flet
from flet import Page, Row, Column, Text, TextField, ElevatedButton, ListView, IconButton, icons, Container, ScrollMode, alignment

def chatbot_page(page: Page):
    page.title = "Chatbot Pages | AI Agent Platform"
    page.window_width = 900
    page.window_height = 600

    chat_history = []
    messages = []

    def update_chat_view():
        chat_view.controls.clear()
        for msg in messages:
            chat_view.controls.append(
                Container(
                    content=Text(msg, size=14, color="#000000"),
                    padding=10,
                    margin=5,
                    bgcolor="#ffffff",
                    border_radius=5,
                    alignment=alignment.CENTER if hasattr(alignment, "CENTER") else None,
                    expand=True,
                )
            )
        chat_view.update()

        history_list.controls.clear()
        for h in chat_history:
            history_list.controls.append(
                Text(h, size=12, selectable=True, opacity=0.7, no_wrap=True)
            )
        history_list.update()

    def send_message(e):
        text = input_field.value.strip()
        if text:
            messages.append(text)
            chat_history.append(text)
            input_field.value = ""
            update_chat_view()

    def clear_history(e):
        chat_history.clear()
        messages.clear()
        update_chat_view()

    history_list = ListView(
        expand=True,
        spacing=5,
        padding=10,
        auto_scroll=True,
    )

    sidebar = Column(
        [
            Text("Riwayat Percakapan", size=16, weight="bold"),
            history_list,
            ElevatedButton("Hapus Riwayat Percakapan", on_click=clear_history),
        ],
        width=250,
        spacing=10,
    )

    chat_view = Column(
        expand=True,
        spacing=10,
        scroll="auto",
    )

    input_field = TextField(
        expand=True,
        hint_text="Ajukan apapun pertanyaan anda",
        autofocus=True,
        on_submit=send_message,
    )

    send_button = ElevatedButton("Kirim", on_click=send_message)

    input_row = Row(
        [
            input_field,
            send_button,
        ],
        spacing=10,
    )

    main_area = Column(
        [
            chat_view,
            input_row,
        ],
        expand=True,
        spacing=10,
    )

    page.add(
        Row(
            [
                sidebar,
                main_area,
            ],
            expand=True,
        )
    )

    update_chat_view()

if __name__ == "__main__":
    flet.app(target=chatbot_page)
