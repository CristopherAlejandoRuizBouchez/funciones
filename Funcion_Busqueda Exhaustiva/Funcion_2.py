import matplotlib.pyplot as plt

def f(x):
    return x**3 + 2*x - 3

def exhaustive_search(precision):
    x_values = []
    y_values = []
    x = 0.1  
    while -5 <= x <= 5:
        x_values.append(x)
        y_values.append(f(x))
        if f(x) > precision:
            x += 1 if precision >= 1 else precision
        else:
            x -= 1 if precision >= 1 else precision

    plt.plot(x_values[-2:], y_values[-2:],'ro', label='Últimos 2 puntos visitados')
    plt.plot(x_values, y_values, label='Función f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfica de la función y los dos últimos puntos visitados para precisión {precision}')
    plt.legend()
    plt.show()


exhaustive_search(0.5)
exhaustive_search(0.1)
exhaustive_search(0.01)
exhaustive_search(0.0001)
print(f(0.5))
