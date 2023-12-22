import numpy as np
from zadatak6 import reverse_odd_rows


def reverse_odd_columns(matrix):
    rows, cols = matrix.shape

    # ITERATIVNO
    for col in range(0, cols, 2):
        for row in range(rows // 2):
            matrix[row, col], matrix[cols - row - 1, col] = matrix[cols - row - 1, col], matrix[row, col]

    # ALTERNATIVNO 1
    # for col in range(0, cols, 2):
    #     matrix[:, col] = np.flip(matrix[:, col])

    # ALTERNATIVNO 2
    # for col in range(0, cols, 2):
    #     matrix[:, col] = matrix[cols - 1::-1, col]

    # Alternativno 3 - Ponovno iskorišćavanje koda
    # matrix = reverse_odd_rows(matrix.T).T

    # Vektorski 1
    # matrix[:,::2] = matrix[::-1,::2]


    return matrix


if __name__ == "__main__":
    a = np.array([[0.3, 1, -5], [-1, 4, 0], [1, 5, 2]])

    print(reverse_odd_columns(a))
