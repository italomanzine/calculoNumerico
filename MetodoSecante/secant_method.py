import numpy as np
import matplotlib.pyplot as plt
from function import f

def secant_method(f, x0, x1, tol, max_iter):
    # Inicializa a lista de aproximações x
    x_values = [x0, x1]

    # Imprime o cabeçalho da tabela
    print(f"{'N':^3} | {'x_(i-1)':^10} | {'x_(i)':^10} | {'f(x_(i-1))':^10} | {'f(x_(i))':^10} | {'x_(i+1)':^10} | {'E_ideal':^10} | {'E':^10}")
    print("-"*73)

    for i in range(max_iter):
        f_x0, f_x1 = f(x_values[-2]), f(x_values[-1])
        # Evita a divisão por zero
        if f_x1 - f_x0 == 0:
            print("Divisão por zero na iteração da secante.")
            return None, i, x_values

        # Calcula o próximo ponto x
        x_next = x_values[-1] - (f_x1 * (x_values[-1] - x_values[-2])) / (f_x1 - f_x0)
        x_values.append(x_next)

        # Calcula o erro estimado e o erro ideal (se desejado)
        err_estimated = abs(x_values[-1] - x_values[-2])
        err_ideal = tol # Neste exemplo, apenas repetimos a tolerância como erro ideal

        # Imprime os detalhes da iteração atual
        print(f"{i+1:^3} | {x_values[-2]:^10.5f} | {x_values[-1]:^10.5f} | {f_x0:^10.5f} | {f_x1:^10.5f} | {x_next:^10.5f} | {err_ideal:^10.5f} | {err_estimated:^10.5f}")

        if err_estimated < tol:
            return x_next, i + 1, x_values

    return x_next, max_iter, x_values

def plot_secant_method(x_values, f):
    plt.figure(figsize=(10, 6))
    
    # Define os limites do gráfico
    x_min, x_max = min(x_values) - 1, max(x_values) + 1
    x_plot = np.linspace(x_min, x_max, 400)
    y_plot = f(x_plot)
    
    # Plota a função
    plt.plot(x_plot, y_plot, label='y = f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    
    # Plota as secantes
    for i in range(len(x_values) - 1):
        x0, x1 = x_values[i], x_values[i+1]
        y0, y1 = f(x0), f(x1)
        # Encontra os coeficientes da linha secante
        coeficientes = np.polyfit([x0, x1], [y0, y1], 1)
        polinomio = np.poly1d(coeficientes)
        # Estende a secante para cruzar o eixo x
        x_sec = np.linspace(x_min, x_max, 100)
        y_sec = polinomio(x_sec)
        plt.plot(x_sec, y_sec, 'r-', alpha=0.6)  # Reduz a transparência
        
        # Marca os pontos da secante no eixo x
        plt.plot(x1, 0, 'ko')
        plt.text(x1, -0.1, f'$x_{i+1}$', ha='center', va='top', color='blue')
        
        # Plota a linha vertical pontilhada da secante até o eixo x
        if i < len(x_values) - 2:  # Não plota para o último ponto, que é a solução
            plt.axvline(x=x1, color='gray', linestyle=':', linewidth=0.5)
            plt.text(x1, f(x1), f'  f(x{i+1})', verticalalignment='bottom', horizontalalignment='right')

    # Plota a seta indicando a solução
    sol_x = x_values[-1]
    plt.annotate('Solução', xy=(sol_x, 0), xytext=(sol_x, max(y_plot)/2),
                 arrowprops=dict(facecolor='orange', shrink=0.05),
                 ha='center')

    # Configurações finais do gráfico
    plt.title('Método da Secante')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()