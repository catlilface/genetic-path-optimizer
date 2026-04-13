"""
Теоретические основы искуственного интеллекта
Лабораторная работа №1

URL: https://online.mospolytech.ru/local/crw/course.php?id=14927

Автор: Климов Александр Олегович
Email: aleklim98@gmail.com

2026
"""

from src.chromosome import Chromosome


def loss_function(chromosome: Chromosome, matrix: list[list[int]]) -> int:
    """
    Функция потерь

    Returns:
        path_length (int): общая длина пути по нодам из хромосомы в матрице
    """

    path_length = 0
    for index, gene in enumerate(chromosome, start=1):
        if index == len(chromosome):
            break

        path_length += matrix[gene][chromosome[index]]

    return path_length
