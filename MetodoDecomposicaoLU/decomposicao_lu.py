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

def lu_decomposition(A):
    """
    Executa a decomposição LU na matriz A.
    
    Args:
        A (numpy.ndarray): Matriz dos coeficientes.
        
    Returns:
        L (numpy.ndarray): Matriz triangular inferior.
        U (numpy.ndarray): Matriz triangular superior.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    
    for k in range(n):
        for i in range(k+1, n):
            if U[k, k] == 0:
                raise ZeroDivisionError("Divisão por zero detectada!")
            L[i, k] = U[i, k] / U[k, k]
            U[i, k:] -= L[i, k] * U[k, k:]
    
    return L, U

def forward_substitution(L, B):
    """
    Resolve o sistema triangular inferior Ly = B.
    
    Args:
        L (numpy.ndarray): Matriz triangular inferior.
        B (numpy.ndarray): Vetor dos termos independentes.
        
    Returns:
        y (numpy.ndarray): Vetor intermediário.
    """
    n = B.size
    y = np.zeros(n)
    
    for i in range(n):
        y[i] = (B[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    
    return y

def backward_substitution(U, y):
    """
    Resolve o sistema triangular superior Ux = y.
    
    Args:
        U (numpy.ndarray): Matriz triangular superior.
        y (numpy.ndarray): Vetor intermediário.
        
    Returns:
        x (numpy.ndarray): Vetor solução.
    """
    n = y.size
    x = np.zeros(n)
    
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    
    return x

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    A = B = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir uma nova matriz e vetor")
        print("2. Visualizar a matriz e o vetor atuais")
        print("3. Executar a decomposição LU")
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
                    L, U = lu_decomposition(A)
                    print("Matriz triangular inferior (L):")
                    print(L)
                    print("Matriz triangular superior (U):")
                    print(U)
                except ZeroDivisionError as e:
                    print(e)
        elif choice == '4':
            if A is None or B is None:
                print("Nenhuma matriz ou vetor foi inserido ainda.")
            elif 'L' not in locals() or 'U' not in locals():
                print("Você precisa executar a decomposição LU primeiro.")
            else:
                try:
                    y = forward_substitution(L, B)
                    x = backward_substitution(U, y)
                    print("Vetor solução (X):")
                    print(x)
                except ZeroDivisionError as e:
                    print(e)
        elif choice == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
