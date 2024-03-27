from function import f
import matplotlib.pyplot as plt
import numpy as np

def plot_function(a, b, root, tol):
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.axhline(0, color='black', lw=2)
    plt.plot(x, y, label='f(x)')
    
    # Marca a bisseção final
    plt.plot(root, f(root), 'ro', label='Raiz aproximada')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
        print("A bisseção requer que f(a) e f(b) tenham sinais opostos.")
        return None, None

    middle = a
    middle_points = []
    while (b - a) / 2.0 > tol:
        middle = (a + b) / 2.0
        middle_points.append(middle)
        if f(middle) == 0:
            return middle, middle_points
        elif f(a) * f(middle) < 0:
            b = middle
        else:
            a = middle

    return (a + b) / 2.0, middle_points
