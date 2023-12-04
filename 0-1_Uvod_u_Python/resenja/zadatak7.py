import numpy as np
from zadatak3 import min_indices_rows


def max_indices_cols(matrix):
    # ITERATIVNO
    rows, cols = matrix.shape
    vector = np.zeros(rows)
    for row in range(rows):
        max_value = matrix[row, 0]
        max_index = 0
        for col in range(1, rows):
            if matrix[row, col] > max_value:
                max_value = matrix[row, col]
                max_index = col
        vector[row] = max_index

    return vector

    # VEKTORSKI 1 - Ovako bi se zadatak radio pomoću argmax funkcije
    # return matrix.argmax(axis=1)

    # ALTERNATIVNO - Ponovno korišćenje postojeće funkcije iz zadatka 3
    # return min_indices_rows(-matrix.T)


if __name__ == "__main__":
    A = np.array([[-2, 5, 3],
                  [-1, -1, 0],
                  [-1, -5, -3]])

    b = max_indices_cols(A)
    print(b)

