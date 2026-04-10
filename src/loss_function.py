from src.chromosome import Chromosome


def loss_function(chromosome: Chromosome, matrix: list[list[int]]) -> int:
    path_length = 0
    for index, gene in enumerate(chromosome, start=1):
        if index == len(chromosome):
            break

        path_length += matrix[gene][chromosome[index]]

    return path_length
