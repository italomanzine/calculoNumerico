import numpy as np
import matplotlib.pyplot as plt

def false_position(f, a, b, tol, max_iter):
    """Executa o método da falsa posição."""
    iterations_data = []
    for i in range(max_iter):
        fa = f(a)
        fb = f(b)
        # Verifica se os valores de fa e fb são iguais para evitar divisão por zero
        if fb == fa:
            return None, iterations_data
        x_ns = (a * fb - b * fa) / (fb - fa)
        f_x_ns = f(x_ns)
        iterations_data.append({'iteration': i + 1, 'a': a, 'b': b, 'fa': fa, 'fb': fb, 'x_ns': x_ns, 'f_x_ns': f_x_ns})
        if abs(f_x_ns) < tol:
            return x_ns, iterations_data
        if fa * f_x_ns < 0:
            b = x_ns
        else:
            a = x_ns
    return None, iterations_data

def find_roots(f, start, end, tol, max_iter):
    """Encontra todas as raízes da função f no intervalo [start, end]."""
    roots = []
    iterations_data = []
    step = (end - start) / 10  # Ajusta para que o intervalo seja progressivamente testado
    a = start

    # Loop para testar cada subintervalo dentro de [start, end]
    while a < end:
        b = a + step
        fa = f(a)
        fb = f(b)
        if fa * fb < 0:
            # Se há uma mudança de sinal entre a e b, chama o método da falsa posição
            root, data = false_position(f, a, b, tol, max_iter)
            if root is not None:
                roots.append(root)
            iterations_data.extend(data)
        else:
            # Ainda registra a tentativa, mesmo quando não há raiz neste subintervalo
            iterations_data.append({
                'iteration': len(iterations_data) + 1,
                'a': a, 'b': b, 'fa': fa, 'fb': fb,
                'x_ns': None, 'f_x_ns': None
            })

        a += step  # Garante que o próximo subintervalo seja testado

    return roots, iterations_data

def print_table(iterations_data, tol):
    """Imprime uma tabela formatada com os dados das iterações, lidando com None values."""
    headers = ["N", "A", "B", "f(A)", "f(B)", "x_ns", "f(x_ns)", "f(A)*f(x_ns)", "f(x_ns)*f(B)", "E_ideal", "E"]
    print("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*headers))
    
    for data in iterations_data:
        # Extraindo dados para evitar repetição de código
        iteration = data.get('iteration', '')
        a, b, fa, fb = data.get('a'), data.get('b'), data.get('fa'), data.get('fb')
        x_ns, f_x_ns = data.get('x_ns'), data.get('f_x_ns')
        # Preparação dos dados para impressão
        formatted_values = [
            iteration,
            "{:.6f}".format(a) if a is not None else '',
            "{:.6f}".format(b) if b is not None else '',
            "{:.6f}".format(fa) if fa is not None else '',
            "{:.6f}".format(fb) if fb is not None else '',
            "{:.6f}".format(x_ns) if x_ns is not None else '',
            "{:.6f}".format(f_x_ns) if f_x_ns is not None else '',
            "{:.6f}".format(fa * f_x_ns) if None not in [fa, f_x_ns] else '',
            "{:.6f}".format(f_x_ns * fb) if None not in [f_x_ns, fb] else '',
            "{:.6f}".format(tol),
            "{:.6f}".format(abs(f_x_ns)) if f_x_ns is not None else ''
        ]
        
        print("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*formatted_values))

def format_iteration_data(a, b, fa, fb, x_ns, f_x_ns, tol):
    """Formata os dados de uma iteração para serem impressos na tabela."""
    # Cria uma lista de valores formatados, lidando com possíveis valores None
    formatted_values = []
    for value in [a, b, fa, fb, x_ns, f_x_ns]:
        if value is None:
            formatted_values.append('')
        else:
            formatted_values.append("{:.6f}".format(value))
    # Calcula o erro se x_ns e f_x_ns são números
    error = "{:.6f}".format(abs(f_x_ns)) if f_x_ns is not None else ''
    # Adiciona os valores de E_ideal e E
    formatted_values.append("{:.6f}".format(tol))
    formatted_values.append(error)
    return formatted_values

def plot_roots(f, roots, start, end):
    """Plota a função f e as raízes encontradas em um gráfico."""
    # Gera os valores de x e y para plotar a função
    x_vals = np.linspace(start, end, 1000)
    y_vals = f(x_vals)
    plt.plot(x_vals, y_vals, label='f(x)')
    # Plota as raízes encontradas
    for root in roots:
        plt.plot(root, f(root), 'ro', label=f'Root at x={root:.4f}')
        plt.annotate(f'({root:.4f}, {f(root):.4f})', xy=(root, f(root)), xytext=(-20, 20),
                     textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5'))
    # Configurações do gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método da Falsa Posição')
    plt.show()
