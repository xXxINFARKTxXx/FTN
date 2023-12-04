import numpy as np
import matplotlib.pyplot as plt


def diameter(points):
    d = 0
    point_count = points.shape[0]
    for i in range(point_count - 1):
        for j in range(i + 1, point_count):
            point1 = points[i, :]
            point2 = points[j, :]
            distance = np.linalg.norm(point1 - point2)
            if distance > d:
                d = distance

    return d

    # Vektorski - Broadcasting https://numpy.org/doc/stable/user/basics.broadcasting.html#broadcasting
    # rows, cols = points.shape
    # return np.linalg.norm(points.reshape((rows, 1, cols)) - points.reshape((1,rows,cols)), axis=2).max()


if __name__ == "__main__":
    points = np.array([[1.0, 0.0],
                       [4.0, 8.0],
                       [2.1, 1.2],
                       [3.2, 1.9],
                       [5.6, 4.3],
                       [7.9, 2.3],
                       [-1.0, 3.1]])

    d = diameter(points)
    print(d)

    x = points[:, 0]
    y = points[:, 1]

    plt.scatter(x, y)
    plt.show()
