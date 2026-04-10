import json

from src.chromosome import Chromosome
from src.constants import Settings
from src.loss_function import loss_function


class Optimizer:
    def __init__(self, settings: Settings):
        self.chromosomes = [
            Chromosome(settings) for _ in range(settings.population_size)
        ]
        self.settings = settings

    def step(self):
        losses = [
            {
                "loss": loss_function(chromosome, self.matrix),
                "chromosome": chromosome,
            }
            for chromosome in self.chromosomes
        ]
        sorted_losses = sorted(losses, key=lambda x: x["loss"], reverse=True)
        elite_chromosomes = sorted_losses[
            : int(len(sorted_losses) * self.settings.elitism_rate)
        ]

    @property
    def matrix(self):
        return self.settings.matrix
