import numpy as np
import matplotlib.pyplot as plt

def newton_method(f, df, x0, tol, max_iter):
    """Executa o Método de Newton para encontrar uma raiz de polinômios."""
    iterations_data = []
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-12:
            break
        x_new = x - fx / dfx
        iterations_data.append({
            'iteration': i + 1,
            'x': x,
            'f(x)': fx,
            'df(x)': dfx,
            'x_new': x_new,
            'error': abs(x_new - x)
        })
        if abs(x_new - x) < tol:
            break
        x = x_new
    return x, iterations_data

def find_roots(f, df, x_start, x_end, tol, max_iter):
    roots = []
    iterations_data_all = []

    # Tenta encontrar raízes, usando pontos uniformemente espaçados como chutes iniciais
    test_points = np.linspace(x_start, x_end, 100)
    for x0 in test_points:
        root, iterations_data = newton_method(f, df, x0, tol, max_iter)
        if root is not None:
            # Verifica se a raiz é única dentro de uma tolerância
            if not any(np.isclose(root, r, atol=tol) for r in roots):
                roots.append(root)
        iterations_data_all.extend(iterations_data)  # Agrega todas as iterações

    # Remove raízes complexas e duplicadas
    roots = [r for r in roots if np.isreal(r)]
    roots = list(set(np.real(roots)))

    # Retorna as raízes únicas reais e os dados de iteração
    return roots, iterations_data_all

def print_table(iterations_data):
    """Imprime uma tabela formatada com os dados das iterações."""
    print("Iter      x          f(x)       df(x)       x_new      Error")
    for data in iterations_data:
        print(f"{data['iteration']:4} {data['x']:10.6f} {data['f(x)']:10.6e} {data['df(x)']:10.6e} {data['x_new']:10.6f} {data['error']:10.6e}")

def plot_roots(f, roots, x_start, x_end):
    x_vals = np.linspace(x_start, x_end, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(12, 6))
    plt.plot(x_vals, y_vals, label='f(x)')

    # Para evitar sobreposição das anotações, determina uma posição de offset dinâmica
    for i, root in enumerate(roots):
        plt.plot(root, f(root), 'ro', label=f'Root at x={root:.4f}')
        offset = (20 if i % 2 == 0 else -20)
        plt.annotate(f'({root:.4f}, {f(root):.4f})', xy=(root, f(root)), xytext=(offset, 20),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5'))

    plt.title("Equações Polinomiais e Raízes Encontradas")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.show()
