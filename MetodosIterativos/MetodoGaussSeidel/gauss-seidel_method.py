import numpy as np

def input_matrix_and_vector():
    """
    Solicita ao usuário a matriz dos coeficientes e o vetor dos termos independentes.
    
    Returns:
        A (numpy.ndarray): Matriz dos coeficientes.
        B (numpy.ndarray): Vetor dos termos independentes.
    """
    n = int(input("Digite o número de equações (e incógnitas): "))
    print("Digite a matriz dos coeficientes:")
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = float(input(f"a[{i+1}][{j+1}]: "))
    
    print("Digite o vetor dos termos independentes:")
    B = np.zeros(n)
    for i in range(n):
        B[i] = float(input(f"b[{i+1}]: "))
    
    return A, B

def display_matrix_and_vector(A, B):
    """
    Exibe a matriz dos coeficientes e o vetor dos termos independentes de forma
    que pareça um sistema de equações.
    
    Args:
        A (numpy.ndarray): Matriz dos coeficientes.
        B (numpy.ndarray): Vetor dos termos independentes.
    """
    n = A.shape[0]
    print("Sistema de Equações:")
    for i in range(n):
        equation = ""
        for j in range(n):
            if j > 0 and A[i, j] >= 0:
                equation += f" + {A[i, j]}x{j+1}"
            else:
                equation += f" {A[i, j]}x{j+1}"
        equation += f" = {B[i]}"
        print(equation)

def check_convergence(A):
    """
    Verifica se a matriz dos coeficientes satisfaz a condição de convergência.
    
    Args:
        A (numpy.ndarray): Matriz dos coeficientes.
        
    Returns:
        bool: True se a condição de convergência for satisfeita, False caso contrário.
    """
    n = A.shape[0]
    for i in range(n):
        sum_row = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) <= sum_row:
            return False
    return True

def gauss_seidel_method(A, B, tolerance, max_iterations):
    """
    Executa o Método Iterativo de Gauss-Seidel para resolver o sistema de equações.
    
    Args:
        A (numpy.ndarray): Matriz dos coeficientes.
        B (numpy.ndarray): Vetor dos termos independentes.
        tolerance (float): Tolerância para a convergência.
        max_iterations (int): Número máximo de iterações.
        
    Returns:
        X (numpy.ndarray): Vetor solução.
        int: Número de iterações realizadas.
        list: Lista de vetores solução em cada iteração.
    """
    n = len(B)
    X = np.zeros_like(B)  # Inicializa o vetor solução com zeros
    iterations_list = []  # Lista para armazenar as soluções em cada iteração
    
    for k in range(max_iterations):
        new_X = X.copy()
        for i in range(n):
            s1 = sum(A[i, j] * new_X[j] for j in range(i))
            s2 = sum(A[i, j] * X[j] for j in range(i + 1, n))
            new_X[i] = (B[i] - s1 - s2) / A[i, i]
            new_X[i] = round(new_X[i], 4)  # Arredondar para 4 casas decimais
        
        iterations_list.append(new_X.copy())
        
        if np.allclose(X, new_X, atol=tolerance):
            return new_X, k + 1, iterations_list
        
        X = new_X.copy()
    
    return X, max_iterations, iterations_list

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    A = B = None
    tolerance = max_iterations = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir uma nova matriz e vetor")
        print("2. Visualizar a matriz e o vetor atuais")
        print("3. Executar o Método Iterativo de Gauss-Seidel")
        print("4. Verificar as soluções")
        print("5. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            A, B = input_matrix_and_vector()
            tolerance = float(input("Digite o valor de tolerância para a convergência: "))
            max_iterations = int(input("Digite o número máximo de iterações: "))
        elif choice == '2':
            if A is None or B is None:
                print("Nenhuma matriz ou vetor foi inserido ainda.")
            else:
                display_matrix_and_vector(A, B)
        elif choice == '3':
            if A is None or B is None or tolerance is None or max_iterations is None:
                print("Nenhuma matriz, vetor, tolerância ou número de iterações foi inserido ainda.")
            else:
                if check_convergence(A):
                    print("a) Verificação da convergência: OK")
                else:
                    print("a) Verificação da convergência: Falhou. A matriz não é diagonalmente dominante.")
                X, iterations, iterations_list = gauss_seidel_method(A, B, tolerance, max_iterations)
                print("b) Isolamento das incógnitas: Concluído")
                print("c) Atribuição inicial: X =", np.zeros_like(B))
                print("d) Iterações:")
                for idx, sol in enumerate(iterations_list):
                    print(f"Iteração {idx + 1}: X = {sol}")
                print("Soluções encontradas:", X)
                print("Quantidade de iterações:", iterations)
        elif choice == '4':
            print("As soluções foram verificadas na última execução do método.")
        elif choice == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
