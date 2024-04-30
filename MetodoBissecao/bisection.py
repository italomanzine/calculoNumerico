import numpy as np
import matplotlib.pyplot as plt

def safe_eval(expr, **kwargs):
    # Avalia expressões matemáticas de forma segura, utilizando uma lista de nomes permitidos
    allowed_names = {'x': kwargs.get('x', 0), 'np': np}
    code = compile(expr, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Uso de nome não permitido: {name}")
    return eval(code, {"__builtins__": {}}, allowed_names)

def plot_function(a, b, root, tol, expr):
    # Gera pontos para o gráfico da função e plota a linha y=0
    x = np.linspace(a - 1, b + 1, 400)
    y = [safe_eval(expr, x=xi) for xi in x]
    plt.axhline(0, color='black', lw=2)
    plt.plot(x, y, label='f(x)')
    
    # Plota e anota a raiz no gráfico
    root_value = safe_eval(expr, x=root)
    plt.plot(root, root_value, 'ro', label=f'Root at x={root:.4f}')
    plt.annotate(f'({root:.4f}, {root_value:.4f})', xy=(root, root_value), xytext=(-20, 20),
                 textcoords='offset points', arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5'))

    # Configurações adicionais e exibição do gráfico
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

 # Imprime uma tabela com os dados das iterações do método da bisseção
def print_table(iterations_data, tol):
    headers = ["N", "A", "B", "x_ns", "f(x_ns)", "f(A)", "f(B)", "f(A)*f(x_ns)", "[A, x_ns]", "[x_ns, B]", "e_ideal", "e"]
    print("{:<4} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*headers))
    for i, data in enumerate(iterations_data):
        a, b, x, f_x, f_a, f_b = data['a'], data['b'], data['x'], data['f(x)'], data['f(a)'], data['f(b)']
        e_ideal = tol
        e = abs(b - a) / 2
        f_a_x = f_a * f_x if f_a is not None and f_x is not None else None
        interval_a_x = f"[{a:.4f}, {x:.4f}]" if a is not None and x is not None else ''
        interval_x_b = f"[{x:.4f}, {b:.4f}]" if x is not None and b is not None else ''
        print(f"{i+1:<4} {a:<12.4f} {b:<12.4f} {x:<12.4f} {f_x:<12.4e} {f_a:<12.4e} {f_b:<12.4e} {f_a_x:<12.4e} {interval_a_x:<12} {interval_x_b:<12} {e_ideal:<12.4f} {e:<12.4f}")

def bisection(a, b, tol, expr):
    # Implementa o método da bisseção para encontrar a raiz de uma função em um intervalo [a, b]
    # Verifica inicialmente se a função muda de sinal entre a e b
    if safe_eval(expr, x=a) * safe_eval(expr, x=b) > 0:
        print("A função deve ter sinais opostos em a e b para o método funcionar.")
        return None, []

    iterations_data = []
    while (b - a) / 2.0 > tol:
        # Encontra o ponto médio e avalia a função nesse ponto
        x_ns = (a + b) / 2.0
        f_x_ns = safe_eval(expr, x=x_ns)
        f_a = safe_eval(expr, x=a)
        f_b = safe_eval(expr, x=b)

        # Registra os dados da iteração
        iterations_data.append({'a': a, 'b': b, 'x': x_ns, 'f(x)': f_x_ns, 'f(a)': f_a, 'f(b)': f_b})

        # Determina o novo intervalo para a próxima iteração
        if f_a * f_x_ns < 0:
            b = x_ns
        elif f_x_ns * f_b < 0:
            a = x_ns
        else:
            # Se a função é suficientemente próxima de zero, para o loop
            if abs(f_x_ns) < tol:
                break
            else:
                raise ValueError("O método da bisseção falhou.")

    # Retorna a raiz encontrada e os dados das iterações
    return (a + b) / 2.0, iterations_data