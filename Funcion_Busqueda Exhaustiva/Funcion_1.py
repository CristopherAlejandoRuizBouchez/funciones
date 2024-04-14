import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 + 54/x

def exhaustive_search(precision):
    x_values = []
    y_values = []
    x = 0.1  
    while x <= 10:
        x_values.append(x)
        y_values.append(f(x))
        if f(x) > precision:
            x += 1 if precision >= 1 else precision
        else:
            x -= 1 if precision >= 1 else precision

    plt.plot(x_values[-2:], y_values[-2:], 'ro', label='Últimos 2 puntos visitados')
    plt.plot(x_values, y_values, label ='Función f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfica de la función y los dos últimos puntos visitados para precisión {precision}')
    plt.legend()
    plt.show()

exhaustive_search(0.5)
exhaustive_search(0.1)
exhaustive_search(0.01)
exhaustive_search(0.0001)