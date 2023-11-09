import flet as ft

# from handler.db_handler import *
import socket
import json


def main(page: ft.Page):
    page.title = "Routes Example"
    text_phone = ft.TextField(label="phone")
    text_login = ft.TextField(label="login")
    text_password = ft.TextField(label="password")
    dlg = ft.AlertDialog(on_dismiss=lambda e: print("Dialog dismissed!"))

    def open_dlg(e, msg):
        dlg.title = ft.Text(msg)
        page.dialog = dlg
        dlg.open = True
        page.update()

    """# Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper
"""

    # @check_input
    def auth(e):
        login = text_login.value
        passw = text_password.value
        # Создаем клиентский сокет
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Определяем хост и порт, на котором сервер слушает
        host = input("Введите ip: ")
        port = 8000

        # Подключаемся к серверу
        client_socket.connect((host, port))
        # Подготавливаем данные в формате JSON
        request_data = {"function": "ck_login", "username": login, "password": passw}
        data = json.dumps(request_data).encode("utf-8")

        # Отправляем данные серверу
        client_socket.send(data)

        # Принимаем ответ от сервера
        response_data = client_socket.recv(1024)

        # Декодируем JSON-данные
        response = json.loads(response_data.decode("utf-8"))
        # Закрываем клиентский сокет
        client_socket.close()

        if response["result"]:
            page.go("/about")
        else:
            open_dlg(e, "Неправильный логин или пароль")

    # @check_input
    def reg(e):
        login = text_login.value
        passw = text_password.value
        phone = text_phone.value
        # Создаем клиентский сокет
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Определяем хост и порт, на котором сервер слушает
        host = "26.153.159.45"
        port = 8000

        # Подключаемся к серверу
        client_socket.connect((host, port))
        # Подготавливаем данные в формате JSON
        request_data = {
            "function": "register",
            "username": login,
            "password": passw,
            "phone": phone,
        }
        data = json.dumps(request_data).encode("utf-8")

        # Отправляем данные серверу
        client_socket.send(data)

        # Принимаем ответ от сервера
        response_data = client_socket.recv(1024)

        # Декодируем JSON-данные
        response = json.loads(response_data.decode("utf-8"))
        # Закрываем клиентский сокет
        client_socket.close()
        open_dlg(e, response["result"])

    def route_change(route):
        page.views.clear()

        page.views.append(
            ft.View(
                "/login",
                [
                    ft.AppBar(title=ft.Text("Вход"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Row(
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            text_login,
                        ],
                    ),
                    ft.Row(
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            text_password,
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton("Log in", on_click=auth),
                            ft.ElevatedButton(
                                "Sign up", on_click=lambda _: page.go("/signup")
                            ),
                        ],
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                "About us", on_click=lambda _: page.go("/about")
                            ),
                        ],
                    ),
                ],
            )
        )
        if page.route == "/signup":
            page.views.append(
                ft.View(
                    "/signup",
                    [
                        ft.AppBar(
                            title=ft.Text("Регистрация"),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_phone,
                            ],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_login,
                            ],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_password,
                            ],
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton("Confirm", on_click=reg),
                            ],
                        ),
                    ],
                )
            )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(
                            title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT
                        ),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        if page.route == "/about":
            page.views.append(
                ft.View(
                    "/about",
                    [
                        ft.AppBar(
                            title=ft.Text("About"), bgcolor=ft.colors.SURFACE_VARIANT
                        ),
                        ft.Text("Information"),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.window_center()
    alignment = (ft.MainAxisAlignment.SPACE_BETWEEN,)
    vertical_alignment = (ft.CrossAxisAlignment.CENTER,)


ft.app(target=main)
