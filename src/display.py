"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026г
"""

from src.screens import Screen


class Display:
    current_screen_id: int = 0

    def __init__(self, *args: Screen):
        self.screens = args

    @property
    def current(self) -> Screen:
        return self.screens[self.current_screen_id]

    def next(self):
        self.current_screen_id += 1

    def prev(self):
        self.current_screen_id -= 1

    def show(self):
        return self.screens[self.current_screen_id].show()

    @property
    def last(self) -> bool:
        return self.current_screen_id == len(self.screens) - 1

    @property
    def first(self) -> bool:
        return self.current_screen_id == 0

    def prompt(self):
        actions = self.current.actions

        description = "\n".join(
            f"{action['short']}: {action['name']}" for action in actions
        )
        next_action = input(
            f"Для продолжения выберите действие:\n\nгде:\n{description}\n\n:"
        )

        return next_action
