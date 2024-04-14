import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3*x**4 - 8*x**3 - 6*x**2 + 12

x_values = np.linspace(-1.5, 3, 1000)
y_values = f(x_values)

def interval_halving(a, b, precision):
    iterations = []
    while abs(b - a) > precision:
        c = (a + b) / 2
        if f(c) < f(b):
            a = c
        else:
            b = c
        iterations.append((a + b) / 2)
    return iterations

precisions = [0.5, 0.1, 0.01, 0.0001]

for precision in precisions:
    iterations = interval_halving( -1.5, 3, precision)
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Puntos visitados')
    plt.title(f'Interval Halving Method (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()