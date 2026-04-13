"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026
"""

from typing import Literal

MutationStrategy = Literal["inversion", "random_swap", "neighbor_swap", "random"]
CrossoverStrategy = Literal["repeat", "no_repeat", "best_repeat", "best_no_repeat"]
