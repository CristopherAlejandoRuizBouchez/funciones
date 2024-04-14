import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**4 + x**2 - 33

def bisection_search(func, lower_bound, upper_bound, precision):
    iterations = []
    a = lower_bound
    b = upper_bound

    while abs(b - a) > precision:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iterations.append(c)

    return iterations


precisiones = [0.5, 0.1, 0.01, 0.0001]

valores_x = np.linspace(-2.5, 2.5, 1000)
valores_y = f(valores_x)
for precision in precisiones:
    plt.figure()
    iterations = bisection_search(f, -2.5, 2.5, precision)
    plt.plot(valores_x, valores_y, label='f(x)')
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Visited Points')
    plt.title(f'bisection_search (Precision: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()
