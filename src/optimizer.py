"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026
"""

from random import choice, randint, random

from src.chromosome import Chromosome, Loss
from src.loss_function import loss_function
from src.settings import Settings


class Optimizer:
    """Класс оптимизатора"""

    def __init__(self, settings: Settings):
        self.chromosomes = [
            Chromosome(settings) for _ in range(settings.population_size)
        ]
        self.settings = settings
        # По умолчанию берем лучшей хромосомой случайную.
        # Так как хромосомы генерируются со случайными весами, первая тоже случайна
        self.best_chromosome = self.chromosomes[0]

    def fit(self):
        """
        Метод оптимизации

        Реализует шаг скрещиваний и мутаций по каждому поколению
        """

        for _ in range(self.settings.number_of_generations):
            self.step()

        print("Лучшая хромосома:", self.best_chromosome)

    def step(self):
        """
        Метод шага эволюции

        Реализует скрещивания и мутации по заданным в настройках стратегиям
        """

        losses: list[Loss] = [
            {
                "loss": loss_function(chromosome, self.matrix),
                "chromosome": chromosome,
            }
            for chromosome in self.chromosomes
        ]
        losses.sort(key=lambda x: x["loss"])

        # После сортировки по возрастанию лучшая хромосома будет первой,
        # так как стоит задача минимизации длины пути
        best = losses[0]
        print(f"{best['loss']=}")
        self.best_chromosome = best["chromosome"]

        # Выделаются "элитные" хромосомы. N% лучших результатов,
        # которые не будут участвовать в скрещиваниях и мутациях
        split_index = int(len(losses) * self.settings.elitism_rate)
        elite_losses = losses[:split_index]
        elite_chromosomes = [loss["chromosome"] for loss in elite_losses]

        # Остальные хромосомы выделяем в отдельную переменную.
        # Они будут участвовать в скрещиваниях и мутациях
        rest_chromosomes = losses[split_index:]
        breeded_chromosomes = self.breed(rest_chromosomes)

        # Мутация хромосом
        for chromosome in breeded_chromosomes:
            chance = random()
            if chance < self.settings.mutation_rate:
                chromosome.mutate()

        # Результатов выполнения шага является конкатинация
        # скрещенных и элитных хромосом
        self.chromosomes = [*breeded_chromosomes, *elite_chromosomes]

    def breed(self, sorted_losses: list[Loss]):
        """
        Метод скрещивания

        Реализует шаг скрещивания хромосом из выборки

        Args:
            sorted_losses (list[Loss]): список "лоссов" хромосом из выборки

        Returns:
           chromosomes (list[Chromosome]): Хромосомы, скрещенные по выбранной стратегии
        """

        chromosomes = [loss["chromosome"] for loss in sorted_losses]

        # Для реализации скрещиваний только лучшей половины выделяем их сразу
        # в отдельные переменные
        half = len(chromosomes) // 2
        best_half, other = chromosomes[:half], chromosomes[half:]

        match self.settings.crossover_strategy:
            case "repeat":
                return self._bread_repeat(chromosomes)
            case "no_repeat":
                return self._bread_no_repeat(chromosomes)
            case "best_repeat":
                offspring = self._bread_repeat(best_half)
                return [*offspring, *other]
            case "best_no_repeat":
                offspring = self._bread_no_repeat(best_half)
                return [*offspring, *other]

    @staticmethod
    def _bread_repeat(chromosomes: list[Chromosome]) -> list[Chromosome]:
        """Метод скрещивания с повторением"""

        new_chromosomes = []
        for chromosome in chromosomes:
            other = choice(chromosomes)
            offspring = chromosome ^ other
            # Как результат скрещивания добавляем только одну хромосому,
            # чтобы не появлялось дубликатов
            new_chromosomes.append(offspring[0])

        return new_chromosomes

    @staticmethod
    def _bread_no_repeat(chromosomes: list[Chromosome]) -> list[Chromosome]:
        """Метод скрещивания без повторений"""

        # Список хешей скрещенных хромосом
        breeded_chromosome_hashes = []
        new_chromosomes = []

        for chromosome in chromosomes:
            # Если хромосома есть в этом списке - значит она уже скрестилась ранее
            # и не может еще раз скреститься
            if chromosome.__hash__ in breeded_chromosome_hashes:
                pass

            other_index = randint(0, len(chromosomes) - 1)
            offspring = chromosome ^ chromosomes[other_index]

            breeded_chromosome_hashes.extend(
                [chromosome.__hash__, chromosomes[other_index].__hash__]
            )
            # Как результат скрещивания добавляем только одну хромосому,
            # чтобы не появлялось дубликатов
            new_chromosomes.append(offspring[0])

        return new_chromosomes

    @property
    def matrix(self):
        return self.settings.matrix
