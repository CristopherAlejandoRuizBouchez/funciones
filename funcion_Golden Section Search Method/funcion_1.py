import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 54/x

x_values = np.linspace(0.1, 10, 100)  
y_values = f(x_values)

def golden_section_search( a, b, precision):
    iterations = []
    gr = (np.sqrt(5) + 1) / 2  # Golden ratio

    while abs(b - a) > precision:
        x1 = b - (b - a) / gr
        x2 = a + (b - a) / gr

        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        iterations.append((a + b) / 2)

    return iterations

precisions = [0.5, 0.1, 0.01, 0.0001]

for precision in precisions:
    plt.figure()
    iterations = golden_section_search(0.1, 10, precision)
    plt.plot(x_values, y_values, label='f(x)')
    plt.scatter(iterations, [f(x) for x in iterations], color='red', label='Puntos visitados')
    plt.title(f'Búsqueda de la Sección Dorada (Precisión: {precision})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()