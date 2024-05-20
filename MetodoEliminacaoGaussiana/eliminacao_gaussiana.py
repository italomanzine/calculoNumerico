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

def gaussian_elimination(A, B):
    """
    Executa a eliminação Gaussiana para transformar a matriz A em uma matriz triangular superior.
    
    Args:
        A (numpy.ndarray): Matriz dos coeficientes.
        B (numpy.ndarray): Vetor dos termos independentes.
        
    Returns:
        U (numpy.ndarray): Matriz triangular superior.
        C (numpy.ndarray): Vetor modificado dos termos independentes.
    """
    n = len(B)
    U = A.copy()
    C = B.copy()
    
    for k in range(n-1):
        for i in range(k+1, n):
            if U[k, k] == 0:
                raise ZeroDivisionError("Divisão por zero detectada!")
            m = U[i, k] / U[k, k]
            U[i, k:] -= m * U[k, k:]
            C[i] -= m * C[k]
    
    return U, C

def back_substitution(U, C):
    """
    Executa a retro-substituição para resolver o sistema triangular superior.
    
    Args:
        U (numpy.ndarray): Matriz triangular superior.
        C (numpy.ndarray): Vetor modificado dos termos independentes.
        
    Returns:
        X (numpy.ndarray): Vetor solução.
    """
    n = len(C)
    X = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        if U[i, i] == 0:
            raise ZeroDivisionError("Divisão por zero detectada!")
        X[i] = (C[i] - np.dot(U[i, i+1:], X[i+1:])) / U[i, i]
    
    return X

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    A = B = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir uma nova matriz e vetor")
        print("2. Visualizar a matriz e o vetor atuais")
        print("3. Executar a eliminação Gaussiana")
        print("4. Verificar as soluções")
        print("5. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            A, B = input_matrix_and_vector()
        elif choice == '2':
            if A is None or B is None:
                print("Nenhuma matriz ou vetor foi inserido ainda.")
            else:
                display_matrix_and_vector(A, B)
        elif choice == '3':
            if A is None or B is None:
                print("Nenhuma matriz ou vetor foi inserido ainda.")
            else:
                try:
                    U, C = gaussian_elimination(A, B)
                    print("Matriz triangular superior (U):")
                    print(U)
                    print("Vetor modificado dos termos independentes (C):")
                    print(C)
                except ZeroDivisionError as e:
                    print(e)
        elif choice == '4':
            if A is None or B is None:
                print("Nenhuma matriz ou vetor foi inserido ainda.")
            elif 'U' not in locals() or 'C' not in locals():
                print("Você precisa executar a eliminação Gaussiana primeiro.")
            else:
                try:
                    X = back_substitution(U, C)
                    print("Vetor solução (X):")
                    print(X)
                except ZeroDivisionError as e:
                    print(e)
        elif choice == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
