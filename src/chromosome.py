"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026
"""

from random import choice, randint
from typing import Literal, TypedDict

from src.settings import Settings


class Chromosome:
    """Класс хромосомы"""

    def __init__(
        self,
        settings: Settings,
        genes: list[int] | None = None,
    ):
        self.length = settings.chromosome_length
        self.num_of_vertices = settings.matrix_length
        self.start = settings.departure_vertex
        self.end = settings.destination_vertex

        if genes is None:
            genes = [
                randint(0, self.num_of_vertices - 1) for _ in range(self.length - 2)
            ]

        # Изменяемая часть - это часть хромосомы, которая подвержена мутациям
        # и кроссоверу. Первый и последний ген (вершины) не могут меняться
        self.variable_part = genes

    def mutate(
        self,
        variant: Literal[
            "inversion", "random_swap", "neighbor_swap", "random"
        ] = "random",
    ):
        """
        Метод мутации хромосомы

        Args:
            variant (str): Вариант мутации. Поддерживается 4 варианта:
                - inversion: Инверсия. Взаимное перемещение зеркальных элементов
                - random_swap: Случайное изменение. Вершина в хромосоме меняется на случайную в матрице
                - neighbor_swap: Взаимное перемещение соседних генов
                - random: Случайный выбор и описанных выше
        """

        match variant:
            case "inversion":
                self.inversion()
            case "random_swap":
                self.random_swap()
            case "neighbor_swap":
                self.neighbor_swap()
            case "random":
                self.mutate(choice(["inversion", "random_swap", "neighbor_swap"]))

    def random_swap(self):
        """Случайная замена вершины"""

        variable_length = len(self.variable_part)
        i = randint(0, variable_length - 1)
        vertex = randint(0, variable_length - 1)

        self.variable_part[i] = vertex

    def neighbor_swap(self):
        """Взаимное перемещение соседних генов"""

        variable_length = len(self.variable_part)
        i = randint(0, variable_length - 2)

        self.variable_part[i], self.variable_part[i + 1] = (
            self.variable_part[i + 1],
            self.variable_part[i],
        )

    def inversion(self):
        """Мутация инверсии"""

        variable_length = len(self.variable_part)
        i = randint(0, variable_length - 1)

        self.variable_part[i], self.variable_part[variable_length - 1 - i] = (
            self.variable_part[variable_length - 1 - i],
            self.variable_part[i],
        )

    def __len__(self):
        """Общее число генов в хромосоме"""
        return len(self.genes)

    def __repr__(self) -> str:
        return str(self.genes)

    def __iter__(self):
        return iter(self.genes)

    def __getitem__(self, index):
        return self.genes[index]

    def __xor__(self, other):
        """Метод для скрещивания хромосом"""

        # Вычисление точек кроссовера
        crossover_breakpoints = [
            randint(0, len(self.variable_part) - 1)
            for _ in range(
                len(self.variable_part) // 2
            )  # Число точек не может быть больше половины от изменяемой части
        ]
        crossover_breakpoints = set(crossover_breakpoints)
        crossover_breakpoints = sorted([*crossover_breakpoints])

        current_position = 0
        result_a = []
        result_b = []
        for i in range(len(crossover_breakpoints)):
            # При скрещивании хромосомы должны поменяться генами в "зеркальных" участках
            if i % 2 == 0:
                result_a.extend(
                    self.variable_part[current_position : crossover_breakpoints[i]]
                )
                result_b.extend(
                    other.variable_part[current_position : crossover_breakpoints[i]]
                )
            else:
                result_a.extend(
                    other.variable_part[current_position : crossover_breakpoints[i]]
                )
                result_b.extend(
                    self.variable_part[current_position : crossover_breakpoints[i]]
                )

            # После обмена участками обновляем позицию.
            # Последняя часть участка - это первая часть нового участка.
            current_position = crossover_breakpoints[i]

        # После скрещивания остается последний участок, которому не назначен брекпоинт.
        # Добавляем его в хромосомы
        result_a.extend(self.variable_part[current_position:])
        result_b.extend(other.variable_part[current_position:])

        return (
            Chromosome(
                settings=Settings(),
                genes=result_a,
            ),
            Chromosome(
                settings=Settings(),
                genes=result_b,
            ),
        )

    @property
    def genes(self):
        return [self.start, *self.variable_part, self.end]


class Loss(TypedDict):
    """Класс "лосса" """

    chromosome: Chromosome
    loss: int
