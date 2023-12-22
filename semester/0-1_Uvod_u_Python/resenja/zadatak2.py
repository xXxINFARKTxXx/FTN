import numpy as np


def sum_greater(matrix):
    # ITERATIVNO
    total = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            total += matrix[i, j]

    avg = total / (rows * cols)

    result = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] > avg:
                result += matrix[row, col]

    # VEKTORSKI 1
    # avg = np.average(matrix)
    # mask = matrix > avg
    # greaters = matrix[mask]
    # result = np.sum(greaters)

    # VEKTORSKI 2 - zapis u jednoj liniji
    # result =  matrix[matrix > matrix.mean()].sum()

    return result


if __name__ == "__main__":
    a = np.array([[2, 1, 2, 6, 8, 1, -2],
                  [15, 4, 7, 18, 4, 0, 12],
                  [11, 6, 9, -1, 4, 8, 0],
                  [2, 8, 6, 8, 1, 8, 7]])

    print(sum_greater(a))
