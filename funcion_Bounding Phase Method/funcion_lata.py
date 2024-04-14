import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * np.pi * x ** 2 + 500/x


def bounding_phase_method(a, b, n):
    points_visited = []
    for i in range(n):
        c = (a + b) / 2 - 0.1
        d = (a + b) / 2 + 0.1
        if f(c) < f(d):
            b = d
        else:
            a = c
        points_visited.append((a + b) / 2)
    return points_visited

n_values = [int(10/precision) for precision in [0.5, 0.1, 0.01, 0.0001]]

for n in n_values:
    points_visited = bounding_phase_method(0.1, 10, n)
    x_values = np.linspace(0.1, 10, num=100)
    y_values = f(x_values)

    plt.figure()
    plt.plot(x_values, y_values, label='f(x) = x^2 + 54/x')
    plt.scatter(points_visited, [f(p) for p in points_visited], color='red', label='Puntos Visitados')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Bounding Phase Method - Precision: {1/n}')
    plt.legend()
    plt.grid()
    plt.show()