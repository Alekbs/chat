import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "Routes Example"
    text_email = ft.TextField(label="email")
    text_login = ft.TextField(label="login")
    text_password = ft.TextField(label="password")
    #создаем бд
    connection = sqlite3.connect('chat.db')
    cursor = connection.cursor()

    #создадим таблицу user
    cursor.execute("""
    CREATE TABLE if NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL               
    )
    """)
        
    #сохраняем и закрываем соединение
    connection.commit()
    print(cursor.execute('SELECT * FROM Users').fetchall())

    connection.close()
    def route_change(route):
        page.views.clear()
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,

        page.views.append(
            ft.View(
                
                "/login",
                [
                    ft.AppBar(title=ft.Text("Вход"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Row(
                        vertical_alignment=ft.MainAxisAlignment.CENTER,

                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.TextField(label="login", width=250),
                        ]
                    ),
                    ft.Row(
                        vertical_alignment=ft.MainAxisAlignment.CENTER,

                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.TextField(label="Password", width=250),
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
                                ft.TextField(label="login"),
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.TextField(label="Password"),
                            ]
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.ElevatedButton(
                                    "Confirm", on_click=add_user
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
    
    def add_user(e):
        #создаем бд
        connection = sqlite3.connect('chat.db')
        cursor = connection.cursor()

        #добавляем пользователя
        cursor.execute('INSERT INTO Users (login, password, email) VALUES (?,?,?)', ('','',text_email.value))
            
        #сохраняем и закрываем соединение
        connection.commit()
        print(cursor.execute('SELECT * FROM Users').fetchall())

        connection.close()
        print(text_email.value)
        

        page.go("/login")


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    page.window_center()
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    vertical_alignment=ft.CrossAxisAlignment.CENTER,


ft.app(target=main)
