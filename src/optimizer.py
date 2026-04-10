from random import choice, randint, random

from src.chromosome import Chromosome, Loss
from src.loss_function import loss_function
from src.settings import Settings


class Optimizer:
    def __init__(self, settings: Settings):
        self.chromosomes = [
            Chromosome(settings) for _ in range(settings.population_size)
        ]
        self.settings = settings
        self.best_chromosome = self.chromosomes[0]

    def fit(self):
        for _ in range(self.settings.number_of_generations):
            self.step()

        print("Лучшая хромосома:", self.best_chromosome)

    def step(self):
        losses: list[Loss] = [
            {
                "loss": loss_function(chromosome, self.matrix),
                "chromosome": chromosome,
            }
            for chromosome in self.chromosomes
        ]
        losses.sort(key=lambda x: x["loss"])

        best = losses[0]
        print(f"{best['loss']=}")
        self.best_chromosome = best["chromosome"]

        split_index = int(len(losses) * self.settings.elitism_rate)
        elite_losses = losses[:split_index]
        elite_chromosomes = [loss["chromosome"] for loss in elite_losses]
        rest_chromosomes = losses[split_index:]
        breeded_chromosomes = self.breed(rest_chromosomes)

        for chromosome in breeded_chromosomes:
            chance = random()
            if chance < self.settings.mutation_rate:
                chromosome.mutate()

        self.chromosomes = [*breeded_chromosomes, *elite_chromosomes]

    def breed(self, sorted_losses: list[Loss]):
        chromosomes = [loss["chromosome"] for loss in sorted_losses]

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
        new_chromosomes = []

        for chromosome in chromosomes:
            other = choice(chromosomes)
            offspring = chromosome ^ other
            new_chromosomes.append(offspring[0])

        return new_chromosomes

    @staticmethod
    def _bread_no_repeat(chromosomes: list[Chromosome]) -> list[Chromosome]:
        breeded_chromosome_hashes = []
        new_chromosomes = []

        for chromosome in chromosomes:
            if chromosome.__hash__ in breeded_chromosome_hashes:
                pass

            other_index = randint(0, len(chromosomes) - 1)
            offspring = chromosome ^ chromosomes[other_index]

            breeded_chromosome_hashes.extend(
                [chromosome.__hash__, chromosomes[other_index].__hash__]
            )

            new_chromosomes.append(offspring[0])

        return new_chromosomes

    @property
    def matrix(self):
        return self.settings.matrix
