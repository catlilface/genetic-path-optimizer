"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026г
"""

from src.types import Action


class Screen:
    content: str = ""
    base_actions: list[Action] = [
        {
            "short": "q",
            "name": "Выход",
        }
    ]
    additional_actions: list[Action] = []

    @classmethod
    def show(cls) -> None:
        print(cls.content)

    @property
    def actions(self) -> list[Action]:
        return self.base_actions + self.additional_actions
