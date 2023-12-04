import numpy as np


def min_indices_rows(matrix):
    # ITERATIVNO
    rows, cols = matrix.shape
    vector = np.zeros(cols)
    for col in range(cols):
        min_value = matrix[0, col]
        min_index = 0
        for row in range(1, rows):
            if matrix[row, col] < min_value:
                min_value = matrix[row, col]
                min_index = row
        vector[col] = min_index

    # VEKTORSKI 1 - Ovako bi se zadatak radio pomoću argmin funkcije
    # vector = matrix.argmin(axis=0)

    return vector


if __name__ == "__main__":
    A = np.array([[-2, 5, -3],
                  [-1, -1, 0],
                  [-3, -5, 1]])

    b = min_indices_rows(A)
    print(b)

