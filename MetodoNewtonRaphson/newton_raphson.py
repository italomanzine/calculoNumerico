import numpy as np
import matplotlib.pyplot as plt

def newton_raphson(f, df, x0, tol, max_iter):
    xi = x0
    x_values = [xi]  # Inicializa a lista de valores de x das iterações.
    iterations_data = []  # Inicializa a lista que armazenará os dados de cada iteração.

    for i in range(max_iter):
        fxi = f(xi)
        dfxi = df(xi)
        
        if abs(dfxi) < np.spacing(1):
            print("Derivada muito próxima de zero. O método falhou.")
            return None, i, x_values, iterations_data
        
        xi_next = xi - fxi / dfxi
        x_values.append(xi_next)
        iterations_data.append({'iteration': i+1, 'x': xi, 'f(x)': fxi, 'f\'(x)': dfxi, 'x_next': xi_next})
        
        if abs(fxi) < tol:
            return xi_next, i, x_values, iterations_data

        xi = xi_next

    return xi, max_iter, x_values, iterations_data

def print_table(iterations_data, tol):
    print("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        'N', 'x_i', 'f(x_i)', 'f\'(x_i)', 'x_i+1', 'E_ideal', 'E'))
    
    for data in iterations_data:
        iteration = data['iteration']
        x_i = data['x']
        f_x_i = data['f(x)']
        df_x_i = data['f\'(x)']
        x_next = data['x_next']
        e_ideal = tol
        e = abs(x_next - x_i)
        
        print("{:<4} {:<12.4f} {:<12.4e} {:<12.4e} {:<12.4f} {:<12.4f} {:<12.4f}".format(
            iteration, x_i, f_x_i, df_x_i, x_next, e_ideal, e))

def plot_tangents(x_values, f, df):
    for xi in x_values[:-1]:  # Ignora o último valor que é a raiz encontrada
        slope = df(xi)
        intercept = f(xi) - slope * xi
        x_tangent = np.linspace(xi - 1, xi + 1, 10)
        y_tangent = slope * (x_tangent - xi) + f(xi)
        plt.plot(x_tangent, y_tangent, 'r--', linewidth=0.7)

def plot_newton_raphson(f, df, x_values):
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
