import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x - 3

x_values = np.linspace(0, 5, 1000)
y_values = f(x_values)

def bounding_phase( a, b, precision):
    iterations = []
    delta = precision / 2
    while abs(b - a) > precision:
        x1 = a + delta
        x2 = b - delta
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        iterations.append((a + b) / 2)
    return iterations
precisions = [0.5, 0.1, 0.01, 0.0001]

for precision in precisions:
    iterations = bounding_phase(0, 5, precision)
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Puntos visitados')
    plt.title(f'Bounding Phase Method (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()