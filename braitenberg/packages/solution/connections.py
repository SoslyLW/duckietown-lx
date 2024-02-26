from typing import Tuple

import numpy as np
import math

sideVal = 0.9
b = 10

def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    # a = (cols / 2) / (1 - sideVal)
    a = (240 - b) / 320
    # offset = -0
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

    for col in range(320):
        for row in range(480):
            if (rows - row) < a * col + b:
                matrix[row, col] = 1

    # for i in range(cols):
    #     if i < cols / 2:
    #         matrix[:, i] = i / a + sideVal

    # for i in range(rows):
    #     for j in range(cols):
    #         if j > 150 and i > rows / 4 - 1 and i < rows / 4 + 100:
    #             matrix[i, j] *= 0.6

    # # matrix[:, :] -= 0.2

    # for i in range(rows):
    #     for j in range(cols):
    #         if i > rows / 4:
    #             matrix[i, j] -= 0.12
    #             # if j < 3 * cols / 4 and j > cols / 2:
    #             #     matrix[i, j] -= 0.1
    #             #     if i > 225 and j > cols / 4:
    #             #         matrix[i, j] -= 0.2
    #             # if i > 325 and j > 3 * cols / 4:
    #             #     matrix[i, j] -= 0.2
    
    # for j in range(rows):
    #     if j < rows / 4:
    #         # matrix[j, :] *= (j / rows)
    #         matrix[j, :] = 0
    #     elif j < 200:
    #         matrix[j, :320] = 0.32
    #         matrix[j, 320:] = 0.4

    # for i in range(rows):
    #     if i < 200:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.45
    #     # elif i < 250:
    #     #     matrix[i, :] *= 0.65
    # #     elif i < 200:
    # #         for j in range(cols):
    #             matrix[i, j] *= 0.8

    # ---
    return matrix.astype("float32")


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one

    rows, cols = shape
    # a = (cols / 2) / (1 - sideVal)
    matrix = np.zeros(shape=shape, dtype="float32")
    a = (240 - b) / 320

    for col in range(320):
        for row in range(480):
            if (rows - row) < -a * (col - 320) + b:
                matrix[row, col+ 320] = 1


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

    # for i in range(cols):
    #     if i > cols / 2:
    #         matrix[:, i] = -(i - cols) / a + sideVal

    # for i in range(rows):
    #     for j in range(cols):
    #         if j < 640 - 150 and i > rows / 4 - 1 and i < rows / 4 + 100:
    #             matrix[i, j] *= 0.6
    
    # for i in range(rows):
    #     for j in range(cols):
    #         if i > rows / 4:
    #             matrix[i, j] -= 0.12
    #             # if j > cols / 4 and j < cols / 2:
    #             #     matrix[i, j] -= 0.1
    #             #     if i > 225 and j > cols / 4:
    #             #         matrix[i, j] -= 0.2
    #             # if i > 325 and j < cols / 4:
    #             #     matrix[i, j] -= 0.2

    
    # for j in range(rows):
    #     if j < rows / 4:
    #         # matrix[j, :] *= (j / rows)
    #         matrix[j, :] = 0
    #     elif j < 200:
    #         matrix[j, :320] = 0.4
    #         matrix[j, 320:] = 0.32
    
    # for i in range(rows):
    #     if i < 200:
    #         for j in range(cols):
    #             matrix[i, j] *= 0.45
    #     # elif i < 250:
    #     #     matrix[i, :] *= 0.65
    # #     elif i < 200:
    # #         for j in range(cols):
    # #             matrix[i, j] *= 0.8

    return matrix.astype("float32")
