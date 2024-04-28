import numpy as np
import matplotlib.pyplot as plt

def newton_method(f, df, x0, tol, max_iter):
    """Executa o Método de Newton para encontrar raízes de polinômios."""
    iterations_data = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:  # Evita divisão por zero ou derivada muito pequena
            return None, iterations_data
        x_new = x - fx / dfx
        iterations_data.append({'iteration': i + 1, 'x': x, 'f(x)': fx, 'df(x)': dfx, 'x_new': x_new, 'error': abs(x_new - x)})
        if abs(x_new - x) < tol:
            return x_new, iterations_data
        x = x_new
    return None, iterations_data

def find_roots(f, df, x0, tol, max_iter):
    """Wrapper para o Método de Newton que orquestra a busca pela raiz."""
    return newton_method(f, df, x0, tol, max_iter)

def print_table(iterations_data):
    """Imprime uma tabela formatada com os dados das iterações."""
    print("Iter      x          f(x)       df(x)       x_new      Error")
    for data in iterations_data:
        print(f"{data['iteration']:4} {data['x']:10.6f} {data['f(x)']:10.6e} {data['df(x)']:10.6e} {data['x_new']:10.6f} {data['error']:10.6e}")

def plot_roots(f, root, x0):
    """Plota a função e a raiz encontrada em um gráfico."""
    x_vals = np.linspace(x0 - 1, x0 + 1, 400)  # Gerando pontos ao redor do chute inicial
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(root, f(root), 'ro', label=f'Root at x={root:.6f}')
    plt.title("Equações Polinomiais")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

