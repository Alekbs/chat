import flet as ft


def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/login",
                [
                    ft.AppBar(title=ft.Text("Вход"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.TextField(label="login"),
                    ft.TextField(label="Password"),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                "Log in", on_click=lambda _: page.go("/store")
                            ),
                            ft.ElevatedButton(
                                "Sign in", on_click=lambda _: page.go("/store")
                            ),
                        ]
                    ),
                    ft.ElevatedButton("About us", on_click=lambda _: page.go("/about")),
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


ft.app(target=main)
