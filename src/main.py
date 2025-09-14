import flet as ft
import views.chatbot_page as chatbot_module


def main(page: ft.Page):
    chatbot_module.chatbot_page(page)


ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)
