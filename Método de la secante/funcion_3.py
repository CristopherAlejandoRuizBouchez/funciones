import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**2 - 33

def busqueda_secante(func, x0, x1, precision, max_iter=100):
    iterations = []

    for _ in range(max_iter):
        x_next = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        iterations.append(x_next)
        if abs(x_next - x1) < precision:
            break
        x0 = x1
        x1 = x_next

    return iterations

x0 = -2.5
x1 = -2
precisiones = [0.5, 0.1, 0.01, 0.0001]

valores_x = np.linspace(-2.5, 2.5, 100)
valores_y = f(valores_x)

for precision in precisiones:
    plt.figure()
    iterations = busqueda_secante(f, x0, x1, precision)
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Visited Points')
    plt.plot(valores_x, valores_y, label='f(x)')
    plt.title(f'Búsqueda Secante (Precisión: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()