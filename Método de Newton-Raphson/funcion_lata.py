import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 * np.pi * x ** 2 + (500 / x)

def derivada_f(x):
    return 4 * np.pi * x - 500 / x**2

def busqueda_newton_raphson( suposicion_inicial, precision, max_iter=100):
    iteraciones = []
    x = suposicion_inicial

    for i in range(max_iter):
        x_siguiente = x - f(x) / derivada_f(x)
        iteraciones.append(x_siguiente)
        if abs(x_siguiente - x) < precision:
            break
        x = x_siguiente

    return iteraciones

precisiones = [0.5, 0.1, 0.01, 0.0001]

valores_x = np.linspace(0.1, 10, 1000)
valores_y = f(valores_x)
for precision in precisiones:
    plt.figure()
    iterations = busqueda_newton_raphson(0.1, precision)
    plt.plot(valores_x, valores_y, label='f(x)')
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Visited Points')
    plt.title(f'busqueda_newton_raphson (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()