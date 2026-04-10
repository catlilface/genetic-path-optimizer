"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026г
"""

from src.types import Action

from .screen import Screen


class Greetings(Screen):
    content = """
Теоретические основы искуственного интеллекта
URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Лабораторная работа №1

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026г
    """
    additional_actions: list[Action] = [
        {
            "short": "s",
            "name": "Начать симуляцию",
        }
    ]
