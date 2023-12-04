import numpy as np


def reverse_odd_rows(matrix):
    rows, cols = matrix.shape

    # ITERATIVNO
    for row in range(0, rows, 2):
        for col in range(cols // 2):
            matrix[row, col], matrix[row, cols - col - 1] = matrix[row, cols - col - 1], matrix[row, col]

    # ALTERNATIVNO 1
    # for row in range(0, rows, 2):
    #     matrix[row, :] = np.flip(matrix[row])

    # ALTERNATIVNO 2
    # for row in range(0, rows, 2):
    #     matrix[row, :] = matrix[row, cols - 1::-1]

    # VEKTORSKI
    # matrix[0::2, :] = matrix[0::2,::-1]

    return matrix


if __name__ == "__main__":
    a = np.array([[0.3, 1, -5], [-1, 4, 0], [1, 5, 2]])

    print(reverse_odd_rows(a))
