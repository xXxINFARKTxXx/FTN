import numpy as np


def sort_by_first_column(matrix):
    rows = matrix.shape[0]
    for i in range(rows - 1):
        for j in range(i + 1, rows):
            if matrix[j, 0] > matrix[i, 0]:
                temp = matrix[i, :].copy()
                matrix[i, :] = matrix[j, :]
                matrix[j, :] = temp
    return matrix
    
# Aleternativno - Pancake sort
    # rows, cols = matrix.shape
    # A = matrix.copy() # Vraća se nova sortirana matrica
    # for row in range(rows - 1):
    #     highest_idx = np.argmax(A[row:,0])
    #     A[row + highest_idx : , :] = np.flipud(A[row + highest_idx:,:])
    #     A[row:,:] = np.flipud(A[row:,:])
    # return A

# Vektorski - Jednolinijsko rešenje
    # return matrix[(-matrix[:,0]).argsort()]


if __name__ == "__main__":
    stocks = np.array([[66, 1],
                       [100, 2],
                       [133, 3],
                       [200, 4],
                       [33, 5],
                       [66, 6],
                       [133, 7],
                       [266, 8]])
    sorted = sort_by_first_column(stocks)
    print(sorted)
