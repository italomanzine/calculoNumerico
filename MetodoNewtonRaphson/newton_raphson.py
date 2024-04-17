import numpy as np
import matplotlib.pyplot as plt
from function import f, df

def newton_raphson(x0, tol, max_iter):
    xi = x0
    x_values = [xi]  # Inicializa a lista de valores de x das iterações
    for i in range(max_iter):
        fxi = f(xi)
        dfxi = df(xi)
        if dfxi == 0:
            print("Derivada nula. O método falhou.")
            return None, i, x_values
        xi_next = xi - fxi / dfxi
        x_values.append(xi_next)  # Armazena o valor de xi nas iterações
        if abs(fxi) < tol:
            return xi_next, i, x_values  # Retorna o valor atual de xi se estiver abaixo da tolerância
        xi = xi_next
    return xi, max_iter, x_values  # Retorna o último valor e o número máximo de iterações se não alcançar a tolerância

def plot_tangents(x_values, f, df):
    for xi in x_values[:-1]:  # Desenha as tangentes para cada ponto de iteração
        slope = df(xi)
        intercept = f(xi) - slope * xi
        x_tangent = np.linspace(xi - 1, xi + 1, 10)
        y_tangent = slope * (x_tangent - xi) + f(xi)
        plt.plot(x_tangent, y_tangent, 'r--', linewidth=0.7)

def plot_newton_raphson(x_values, f, df):
    plt.figure(figsize=(10, 6))
    x_min, x_max = min(x_values) - 1, max(x_values) + 1
    x_plot = np.linspace(x_min, x_max, 400)
    y_plot = f(x_plot)
    plt.plot(x_plot, y_plot, label='f(x)')

    # Plota as iterações no eixo x e as rotula
    for i, xi in enumerate(x_values[:-1]):
        # Calcula onde a tangente intercepta o eixo x
        x_intercept = xi - f(xi) / df(xi)
        tangent_x = np.linspace(xi, x_intercept, 100)
        tangent_y = df(xi) * (tangent_x - xi) + f(xi)
        plt.plot(tangent_x, tangent_y, 'r--', linewidth=1)
        plt.axvline(xi, color='gray', linestyle=':', linewidth=1)

        # Rotula o ponto de iteração xi
        plt.text(xi, -0.5, f'x{i+1}', ha='center', va='center', color='blue')

    # Desenha uma seta apontando para a solução final
    plt.annotate('Solução', xy=(x_values[-1], 0), xytext=(x_values[-1], f(x_values[-1]) + 3),
                 arrowprops=dict(facecolor='green', shrink=0.05),
                 ha='center')

    # Configurações adicionais do gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(x_values[-1], color='green', linestyle='--')
    plt.plot(x_values[-1], f(x_values[-1]), 'go')
    plt.title('Método de Newton-Raphson')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
