import flet as ft


def main(page: ft.Page):



    #Page initialization
    #page.client_storage.set("key", "arvin")

    value = page.client_storage.get("key")

    print(value)



ft.app(target=main, port=8886, assets_dir="assets")