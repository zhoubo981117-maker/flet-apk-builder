import flet as ft


def main(page: ft.Page):
    page.title = "Flet APK"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 24

    counter = ft.Text("0", size=48, weight=ft.FontWeight.BOLD)

    def inc(e):
        counter.value = str(int(counter.value) + 1)
        page.update()

    def dec(e):
        counter.value = str(int(counter.value) - 1)
        page.update()

    page.add(
        ft.Text("Flet 构建管道验证成功", size=20, weight=ft.FontWeight.W_600),
        ft.Text("本 APK 由 GitHub Actions (x86_64 runner) 编译产出", size=12, color=ft.Colors.GREY),
        ft.Divider(height=24),
        counter,
        ft.Row(
            [ft.FilledButton("-1", on_click=dec), ft.FilledButton("+1", on_click=inc)],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=16,
        ),
    )


ft.app(target=main)
