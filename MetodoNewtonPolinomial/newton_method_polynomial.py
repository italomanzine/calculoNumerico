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

def find_roots(f, df, x_start, x_end, tol, max_iter):
    """Orquestra a busca pela raiz usando um valor inicial inteligente dentro do intervalo."""
    x0 = (x_start + x_end) / 2  # Escolhe o ponto médio como chute inicial
    return newton_method(f, df, x0, tol, max_iter)

def print_table(iterations_data):
    """Imprime uma tabela formatada com os dados das iterações."""
    print("Iter      x          f(x)       df(x)       x_new      Error")
    for data in iterations_data:
        print(f"{data['iteration']:4} {data['x']:10.6f} {data['f(x)']:10.6e} {data['df(x)']:10.6e} {data['x_new']:10.6f} {data['error']:10.6e}")

def plot_roots(f, root, x_start, x_end):
    """Plota a função e a raiz encontrada em um gráfico, com uma vista ampla do intervalo fornecido."""
    x_vals = np.linspace(x_start - 1, x_end + 1, 400)  # Gera pontos para um intervalo mais amplo
    y_vals = f(x_vals)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label='f(x)')
    plt.plot(root, f(root), 'ro', label=f'Root at x={root:.6f}')
    plt.annotate(f'({root:.4f}, {f(root):.4f})', xy=(root, f(root)), xytext=(-20, 20),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5'))
    plt.title("Equações Polinomiais e Raízes Encontradas")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()

