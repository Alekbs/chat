import flet as ft
from handler.db_handler import *


def main(page: ft.Page):
    page.title = "Routes Example"
    text_email = ft.TextField(label="email")
    text_login = ft.TextField(label="login")
    text_password = ft.TextField(label="password")
    # Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper


    @check_input
    def auth():
        login = text_login.value()
        passw = text_password.value()
        ck_login(login, passw)


    @check_input
    def reg():
        login = text_login.value()
        passw = text_password.value()
        email = text_email.value()
        self.check_db.thr_register(login, passw, email)
   
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
                        ]
                    ),
                    ft.Row(
                        vertical_alignment=ft.MainAxisAlignment.CENTER,

                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            text_password,
                        ]
                    ),
                    ft.Row(
                        
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton(
                                "Log in", on_click=lambda _: page.go("/store")
                            ),
                            ft.ElevatedButton(
                                "Sign in", on_click=lambda _: page.go("/signin")
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.ElevatedButton("About us", on_click=lambda _: page.go("/about")),
                        ]
                    )
                    
                ],
            )
        )
        if page.route == "/signin":
            page.views.append(
                ft.View(
                    "/signin",
                    [
                        
                        ft.AppBar(title=ft.Text("Регистрация"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_email,
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_login,
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                text_password,
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    "Confirm", on_click=reg
                                ),
                            ]

                        )
                        
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
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,


ft.app(target=main)
