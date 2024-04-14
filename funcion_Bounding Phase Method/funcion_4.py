import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**4 - 8*x**3 - 6*x**2 + 12

def bounding_phase_method(a, b, n):
    points_visited = []
    for i in range(n):
        c = (a + b) / 2 - 0.01
        d = (a + b) / 2 + 0.01
        if f(c) < f(d):
            b = d
        else:
            a = c
        points_visited.append((a + b) / 2)
    return points_visited

n_values = [int(4.5/precision) for precision in [0.5, 0.1, 0.01, 0.0001]]

for n in n_values:
    points_visited = bounding_phase_method(-1.5, 3, n)
    x_values = np.linspace(-1.5, 3, num=100)
    y_values = f(x_values)

    plt.figure()
    plt.plot(x_values, y_values, label='f(x) = 3x^4 - 8x^3 - 6x^2 + 12')
    plt.scatter(points_visited, [f(p) for p in points_visited], color='red', label='Puntos Visitados')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Bounding Phase Method - Precision: {1/n}')
    plt.legend()
    plt.grid()
    plt.show()