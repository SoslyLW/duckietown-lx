from typing import Tuple

import numpy as np
import math

sideVal = 0.9

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    a = (cols / 2) / (1 - sideVal)
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

    # for i in range(cols):
    #     matrix[:, i] = 1 / (1 + math.exp(0.1 * (i - cols / 2)))

    for i in range(cols):
        if i < cols / 2:
            matrix[:, i] = i / a + sideVal

    for j in range(rows):
        if j < rows / 4:
            matrix[j, :] *= (j / rows)

    for i in range(rows):
        for j in range(cols):
            if j > 150 and i > rows / 4 - 1 and i < rows / 4 + 100:
                matrix[i, j] *= 0.6

    # matrix[:, :] -= 0.2

    for i in range(rows):
        if i > rows / 4:
            matrix[i, :] -= 0.12

    # for i in range(rows):
    #     if i < 100:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.1
    #     elif i < 200:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.8

    # ---
    return matrix.astype("float32")


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    a = (cols / 2) / (1 - sideVal)
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

    # for i in range(cols):
    #     matrix[:, i] = 1 / (1 + math.exp(0.1 * (-(i - cols / 2))))

    for i in range(cols):
        if i > cols / 2:
            matrix[:, i] = -(i - cols) / a + sideVal
    
    for j in range(rows):
        if j < rows / 4:
            matrix[j, :] *= (j / rows)

    for i in range(rows):
        for j in range(cols):
            if j < 640 - 150 and i > rows / 4 - 1 and i < rows / 4 + 100:
                matrix[i, j] *= 0.6
    
    for i in range(rows):
        if i > rows / 4:
            matrix[i, :] -= 0.12
    
    # for i in range(rows):
    #     if i < 100:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.1
    #     elif i < 200:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.8

    return matrix.astype("float32")
