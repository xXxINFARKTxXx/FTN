import numpy as np


def min_indices_diagonal(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise Exception("Ulazna matrica nije kvadratna")

    # ITERATIVNO
    min_value = np.inf
    indices = [0, 0]
    for row in range(rows):
        for col in range(rows):
            if row == col:  # element se nalazi na glavnoj dijagonali
                if matrix[row, col] < min_value:
                    min_value = matrix[row, col]
                    indices = [row, col]
            if col == (rows - row - 1):  # element se nalazi na sporednoj dijagonali
                if matrix[row, col] < min_value:
                    min_value = matrix[row, col]
                    indices = [row, col]

    return indices

    # VEKTORSKI 1
    # mask = ~np.maximum(np.eye(rows), np.fliplr(np.eye(rows))).astype(bool)
    # matrix[mask] = np.inf
    # print(np.nonzero(matrix == np.min(matrix)))
    # indices = np.nonzero(matrix == np.min(matrix))
    # return indices[0][0], indices[1][0]

    # VEKTORSKI 2
    # A = matrix.astype(np.float64) # Pretvaranje vrednosti u float da bi se mogla ubaciti inf vrednost (ukoliko su vrednosti u matrici tipa int)
    # mask = np.logical_or(np.flipud(np.eye(matrix.shape[0])), np.eye(matrix.shape[0]))
    # A[~mask] = np.inf
    # return np.unravel_index(A.argmin(), A.shape) # Unravel_index za zadati redni broj indeksa vraća koordinate u tenzoru prosleđenog oblika

    # VEKTORSKI 3
    # mask = np.logical_or(np.flipud(np.eye(rows)), np.eye(rows))
    # matrix = np.where(mask, matrix, np.inf) # Where funkcija čuva dimenzionalnost kada primenjuje masku, a na vrednost van maske postavlja inf
    # return np.unravel_index(matrix.argmin(), matrix.shape)


if __name__ == "__main__":
    A = np.array([[-2., 5., -7.],
                  [-1., -1., -8.],
                  [-3., -5., 1.]])

    b = min_indices_diagonal(A)
    print(b)
