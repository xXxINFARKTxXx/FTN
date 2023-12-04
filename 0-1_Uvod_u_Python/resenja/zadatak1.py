import numpy as np


def sum_d(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Ulazna matrica nije kvadratna")

    # ITERATIVNO
    total = 0
    for i in range(rows):
        total += matrix[i, i]

    # VEKTORSKI 1
    # total = np.sum(np.diagonal(matrix))

    # VEKTORSKI 2
    # mask = np.eye(rows)
    # masked = matrix * mask
    # total = np.sum(masked)

    # VEKTORSKI 3
    # mask = np.eye(rows).astype(bool)
    # masked = matrix[mask]
    # total = np.sum(masked)

    # VEKTORSKI 4 - Ulančani poziv funkcija
    # total = matrix.diagonal().sum()
    
    # VEKTORSKI 5 - Postojeća metoda za računanje sume elemenata na glavnoj dijagonali matrice
    # total = np.trace(matrix)

    # VEKTORSKI 6 - Integer array indexing
    # total = matrix[np.arange(rows), np.arange(rows)].sum()

    return total


if __name__ == "__main__":
    a = np.array([[2, 1, 6, 1],
                  [1, 3, 8, 2],
                  [5, 9, 4, 3],
                  [1, 1, 8, 5]])
    print(sum_d(a))
