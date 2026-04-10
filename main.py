"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026
"""

import sys

from src.chromosome import Chromosome
from src.optimizer import Optimizer
from src.settings import Settings

greetings_text = """
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026

a - Автоматический режим
s - Режим по шагам
q - Выход

Для продолжения выберите [a, s, q]:
"""


def print_path(chromosome: Chromosome, matrix: list[list[int]]):
    path = ""

    for index, gene in enumerate(chromosome, start=1):
        if index == len(chromosome):
            path += f"{gene}"
            break
        path += f"{gene} --({matrix[gene][chromosome[index]]})--> "

    print("\nПуть:\n", path)


def auto():
    settings = Settings()
    optimizer = Optimizer(settings)
    optimizer.fit()
    print_path(optimizer.best_chromosome, settings.matrix)


def step():
    settings = Settings()
    optimizer = Optimizer(settings)

    for _ in range(settings.number_of_generations):
        optimizer.step()
        print_path(optimizer.best_chromosome, settings.matrix)
        input("Для продолжения нажмите Enter")


action = input(greetings_text)

match action:
    case "q":
        print("До свидания!")
        sys.exit(0)
    case "a":
        auto()
    case "s":
        step()
