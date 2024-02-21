from typing import Tuple

import numpy as np
import math


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    offset = -0
    matrix = np.zeros(shape=shape, dtype="float32")
    # for i in range(rows):
    #     for j in range(cols):
    #         if j < cols / 2:
    #             #matrix[i, j] = pow((1 * (i/rows)), 3) * pow((0.5 * (j / (cols / 2))), 1)
    #             matrix[i, j] = pow((0.5 * (j / (cols / 2))), 1)
    #         else:
    #             #matrix[i, j] = -1 * pow((offset + 1 * (i/rows)), 3) * pow((offset + 0.5 * (1-((j- (cols / 2)) / (cols / 2)))), 2)
    #             matrix[i, j] = -1 * pow((offset + 0.5 * (1-((j- (cols / 2)) / (cols / 2)))), 2)

    for i in range(cols):
        matrix[:, i] = 1 / (1 + math.exp(0.1 * (i - cols / 2)))

    for i in range(rows):
        if i < 100:
            for j in range(cols):
                matrix[i, j] *= 0.1
        elif i < 200:
            for j in range(cols):
                matrix[i, j] *= 0.8

    # ---
    return matrix.astype("float32")


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    offset = -0
    matrix = np.zeros(shape=shape, dtype="float32")
    # for i in range(rows):
    #     for j in range(cols):
    #         if j < cols / 2:
    #             #matrix[i, j] = -1 * pow((offset + 1 * (i/rows)), 3) * pow((offset + 0.5 * (j / (cols / 2))), 2)
    #             matrix[i, j] = -1 * pow((offset + 0.5 * (j / (cols / 2))), 2)
    #         else:
    #             #matrix[i, j] = pow((1 * (i/rows)), 3) * pow((0.5 * (1-((j- (cols / 2)) / (cols / 2)))), 1)
    #             matrix[i, j] = pow((0.5 * (1-((j- (cols / 2)) / (cols / 2)))), 1)

    for i in range(cols):
        matrix[:, i] = 1 / (1 + math.exp(0.1 * (-(i - cols / 2))))

    for i in range(rows):
        if i < 100:
            for j in range(cols):
                matrix[i, j] *= 0.1
        elif i < 200:
            for j in range(cols):
                matrix[i, j] *= 0.8

    return matrix.astype("float32")
