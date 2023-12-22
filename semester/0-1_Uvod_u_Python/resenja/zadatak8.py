import numpy as np


def reverse_diags(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Ulazna matrica nije kvadratna")

    # ITERATIVNO
    for i in range(rows):
        matrix[i, i], matrix[i, rows - i - 1] = matrix[i, rows - i - 1], matrix[i, i]

    # VEKTORSKI
    # mask = np.maximum(np.eye(rows), np.fliplr(np.eye(rows)))
    # matrix = np.fliplr(matrix * mask) + matrix * np.logical_not(mask)

    return matrix


if __name__ == "__main__":
    a = np.array([[-0.5, 10, 2],
                  [-1, 1, 0],
                  [1, -6, -3]])

    print(reverse_diags(a))
