import json

from src.types import CrossoverStrategy, MutationStrategy


class Settings:
    elitism_rate = 0.3
    """Процент лучших особей переходящих в следующее поколение без изменений"""
    mutation_rate = 0.06
    """Вероятность мутации"""

    population_size = 10
    """Размер популяции в поколении"""
    number_of_generations = 100
    """Число поколений"""

    departure_vertex = 0
    """Стартовая вершина"""
    destination_vertex = 20
    """Конечная вершина"""

    chromosome_length = 30
    """Длина хромосомы"""
    crossover_strategy: CrossoverStrategy = "best_no_repeat"
    """Стратегия (вариант) скрещивания"""
    mutation_strategy: MutationStrategy = "random"
    """Стратегия (вариант) мутации"""

    @property
    @staticmethod
    def matrix():
        """Матрица, динамически загружаемая из файла"""
        with open("./MATRIX.json", "r") as f:
            res: list[list[int]] = json.loads(f.read())
        return res

    @property
    @staticmethod
    def matrix_length():
        with open("./MATRIX.json", "r") as f:
            return len(json.loads(f.read()))
