import math
import matplotlib.pyplot as plt

def linspace(start, stop, num):
    return [start + i*(stop-start)/(num-1) for i in range(num)]

def plot(funcion, a, b, n_arreglo):
    x_valores = linspace(a, b, 100)
    y_valores = [funcion(x) for x in x_valores]

    plt.plot(x_valores, y_valores, label='Función')

    for n in n_arreglo:
        rango_minimo = fibonacci_search(funcion, a, b, n)
        if rango_minimo:
            min_x, max_x = rango_minimo
            plt.scatter([min_x, max_x], [funcion(min_x), funcion(max_x)], label=f'Rango mínimo ({n})')

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Gráfica de la función y puntos mínimos para distintas precisiones')
    plt.grid(True)
    plt.show()


def fibonacci(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 2):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n + 1]


def fibonacci_search(funcion, a, b, n):
    L = b - a
    k = 2
    
    while k <= n:
        Lk_asterisco = (fibonacci(n - k + 1) / fibonacci(n + 1)) * L
        x1 = a + Lk_asterisco
        x2 = b - Lk_asterisco
        
        fx1 = funcion(x1)
        fx2 = funcion(x2)
        
        if fx1 > fx2:
            a = x1
        elif fx1 < fx2:
            b = x2
        else:
            a = x1
            b = x2
        
        k += 1
    print(a, b)
    return (a, b)

def f(x):
    r = (x**4) + (x**2) - 33
    return r

plot(f, -2.5, 2.5, [5, 10, 15, 20])