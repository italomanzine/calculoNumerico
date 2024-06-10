import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, lambdify, sympify

def input_functions_and_initial_guess():
    """
    Solicita ao usuário as funções do sistema não-linear e a estimativa inicial.
    
    Returns:
        funcs (list): Lista de funções do sistema.
        initial_guess (numpy.ndarray): Vetor de estimativas iniciais.
    """
    try:
        n = int(input("Digite o número de equações (e incógnitas): "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return None, None, None
    
    x = symbols(f'x1:{n+1}')
    funcs = []
    
    for i in range(n):
        func = input(f"Digite a função f{i+1}(x1, x2, ..., xn): ")
        try:
            funcs.append(sympify(func))
        except Exception as e:
            print(f"Erro ao processar a função: {e}")
            return None, None, None
    
    initial_guess = np.zeros(n)
    for i in range(n):
        try:
            initial_guess[i] = float(input(f"Digite a estimativa inicial para x{i+1}: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            return None, None, None
    
    return funcs, initial_guess, x

def display_functions_and_guess(funcs, initial_guess):
    """
    Exibe as funções do sistema não-linear e a estimativa inicial.
    
    Args:
        funcs (list): Lista de funções do sistema.
        initial_guess (numpy.ndarray): Vetor de estimativas iniciais.
    """
    print("Funções do sistema:")
    for i, func in enumerate(funcs):
        print(f"f{i+1}(x1, x2, ..., xn) = {func}")
    print("Estimativa inicial:")
    print(initial_guess)

def jacobian_matrix(funcs, x):
    """
    Calcula a matriz Jacobiana das funções do sistema não-linear.
    
    Args:
        funcs (list): Lista de funções do sistema.
        x (sympy.symbols): Variáveis simbólicas.
        
    Returns:
        jacobian (numpy.ndarray): Matriz Jacobiana.
    """
    n = len(funcs)
    jacobian = np.zeros((n, n), dtype=object)
    
    for i in range(n):
        for j in range(n):
            jacobian[i, j] = diff(funcs[i], x[j])
    
    return jacobian

def newton_method(funcs, initial_guess, x, tol=1e-4, max_iter=100):
    """
    Executa o método de Newton para resolver o sistema de equações não-lineares.
    
    Args:
        funcs (list): Lista de funções do sistema.
        initial_guess (numpy.ndarray): Vetor de estimativas iniciais.
        x (sympy.symbols): Variáveis simbólicas.
        tol (float): Tolerância para a convergência.
        max_iter (int): Número máximo de iterações.
        
    Returns:
        solution (numpy.ndarray): Vetor solução.
        int: Número de iterações realizadas.
        list: Lista de vetores solução em cada iteração.
    """
    n = len(funcs)
    jacobian = jacobian_matrix(funcs, x)
    jacobian_func = lambdify(x, jacobian, modules='numpy')
    funcs_func = lambdify(x, funcs, modules='numpy')
    
    current_guess = initial_guess
    iterations_list = [current_guess.copy()]
    
    for k in range(max_iter):
        F = np.array(funcs_func(*current_guess), dtype=float).flatten()
        J = np.array(jacobian_func(*current_guess), dtype=float)
        
        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            raise ValueError("Matriz Jacobiana é singular.")
        
        current_guess = current_guess + delta
        iterations_list.append(current_guess.copy())
        
        if np.linalg.norm(delta, np.inf) < tol:
            return current_guess, k + 1, iterations_list
    
    return current_guess, max_iter, iterations_list

def plot_solution(iterations_list, x):
    """
    Plota a evolução das soluções ao longo das iterações.
    
    Args:
        iterations_list (list): Lista de vetores solução em cada iteração.
        x (sympy.symbols): Variáveis simbólicas.
    """
    iterations = np.array(iterations_list)
    n = iterations.shape[1]
    
    for i in range(n):
        plt.plot(iterations[:, i], label=f'{x[i]}')
    
    plt.xlabel('Iteração')
    plt.ylabel('Valor')
    plt.title('Convergência das variáveis')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    funcs = initial_guess = x = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados para a nova matriz")
        print("2. Visualizar a matriz e o vetor atuais")
        print("3. Executar o Método de Newton mostrando os passos utilizados")
        print("4. Exibir as soluções")
        print("5. Exibir o gráfico")
        print("6. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            funcs, initial_guess, x = input_functions_and_initial_guess()
            if funcs is None or initial_guess is None or x is None:
                print("Erro na entrada dos dados. Tente novamente.")
        elif choice == '2':
            if funcs is None or initial_guess is None:
                print("Nenhuma função ou estimativa inicial foi inserida ainda.")
            else:
                display_functions_and_guess(funcs, initial_guess)
        elif choice == '3':
            if funcs is None or initial_guess is None:
                print("Nenhuma função ou estimativa inicial foi inserida ainda.")
            else:
                try:
                    solution, iterations, iterations_list = newton_method(funcs, initial_guess, x)
                    print("Soluções encontradas:")
                    for i, val in enumerate(solution):
                        print(f'x{i+1} = {val}')
                    print("Quantidade de iterações:", iterations)
                    print("Passos utilizados nas iterações:")
                    for idx, sol in enumerate(iterations_list):
                        print(f"Iteração {idx + 1}: {sol}")
                except ValueError as e:
                    print(e)
        elif choice == '4':
            if funcs is None or initial_guess is None:
                print("Nenhuma função ou estimativa inicial foi inserida ainda.")
            else:
                try:
                    solution, _, _ = newton_method(funcs, initial_guess, x)
                    print("Soluções encontradas:")
                    for i, val in enumerate(solution):
                        print(f'x{i+1} = {val}')
                except ValueError as e:
                    print(e)
        elif choice == '5':
            if funcs is None or initial_guess is None:
                print("Nenhuma função ou estimativa inicial foi inserida ainda.")
            else:
                try:
                    _, _, iterations_list = newton_method(funcs, initial_guess, x)
                    plot_solution(iterations_list, x)
                except ValueError as e:
                    print(e)
        elif choice == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
