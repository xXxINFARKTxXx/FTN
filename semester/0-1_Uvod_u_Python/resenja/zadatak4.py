import numpy as np


def sum_rows(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Ulazna matrica nije kvadratna")
    n = rows

    # ITERATIVNO 1
    result = np.zeros(n)
    for i in range(n):
        row_total = 0
        for j in range(n):
            if i == n - j - 1:
                continue
            row_total += matrix[i, j]
        result[i] = row_total

    # VEKTORSKI 1
    # mask = np.fliplr(np.logical_not(np.eye(n)))
    # masked = matrix * mask
    # result = np.sum(masked, axis=1)

    # VEKTORSKI 2
    # result = matrix.sum(axis=1) - np.fliplr(matrix).diagonal()

    return result


if __name__ == "__main__":
    a = np.array([[-0.5, 10, 2], [-1, 1, 0], [1, -6, -3]])

    print(sum_rows(a))
