import flet as ft


class CounterApp:
    def __init__(self):
        self.count = 0
        self.text = ft.Text(value=f"{self.count}", size=50)

    def increment(self):
        self.count += 1
        self.text.value = f"{self.count}"

    def build(self):
        return ft.SafeArea(
            ft.Container(
                self.text,
                alignment=ft.Alignment.CENTER,
            ),
            expand=True,
        )


def main(page: ft.Page):
    app = CounterApp()

    def on_increment(topic, message):
        app.increment()
        page.update()

    page.pubsub.subscribe_topic("increment", on_increment)

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=lambda e: page.pubsub.send_all_on_topic("increment", None)
    )
    page.add(app.build())


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)
