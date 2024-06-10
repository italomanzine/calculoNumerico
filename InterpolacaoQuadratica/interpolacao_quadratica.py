import numpy as np

def input_points():
    """
    Solicita ao usuário o número de pontos e as coordenadas desses pontos.
    
    Returns:
        points (list of tuples): Lista de pontos (x, y).
    """
    try:
        n = int(input("Digite o número de pontos (mínimo 3): "))
        if n < 3:
            raise ValueError("O número mínimo de pontos é 3.")
    except ValueError as e:
        print(e)
        return []
    
    points = []
    for i in range(n):
        try:
            x = float(input(f"Digite a coordenada x do ponto {i+1}: "))
            y = float(input(f"Digite a coordenada y do ponto {i+1}: "))
            points.append((x, y))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
            return []
    
    return points

def display_points(points):
    """
    Exibe os pontos atuais inseridos pelo usuário.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
    """
    if not points:
        print("Nenhum ponto foi inserido ainda.")
        return
    
    print("Pontos atuais:")
    for i, (x, y) in enumerate(points):
        print(f"Ponto {i+1}: x = {x}, y = {y}")

def quadratic_interpolation(p1, p2, p3):
    """
    Calcula o polinômio interpolador de segundo grau entre três pontos.
    
    Args:
        p1 (tuple): Primeiro ponto (x1, y1).
        p2 (tuple): Segundo ponto (x2, y2).
        p3 (tuple): Terceiro ponto (x3, y3).
        
    Returns:
        (float, float, float): Coeficientes a2, a1 e a0 do polinômio interpolador P2(x) = a2*x^2 + a1*x + a0.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])
    B = np.array([y1, y2, y3])
    
    try:
        a2, a1, a0 = np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        raise ValueError("Os pontos fornecidos não permitem uma solução única.")
    
    return a2, a1, a0

def calculate_interpolated_value(a2, a1, a0, x):
    """
    Calcula o valor interpolado para um valor específico de x.
    
    Args:
        a2 (float): Coeficiente a2 do polinômio interpolador.
        a1 (float): Coeficiente a1 do polinômio interpolador.
        a0 (float): Coeficiente a0 do polinômio interpolador.
        x (float): Valor de x para o qual se deseja calcular o valor interpolado.
        
    Returns:
        float: Valor interpolado.
    """
    return a2 * x**2 + a1 * x + a0

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    points = []
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados para os pontos")
        print("2. Visualizar os pontos atuais")
        print("3. Executar a interpolação quadrática")
        print("4. Exibir a função interpoladora")
        print("5. Calcular e exibir o valor interpolado para um valor específico de x")
        print("6. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            points = input_points()
        elif choice == '2':
            display_points(points)
        elif choice == '3':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    p3 = points[2]
                    a2, a1, a0 = quadratic_interpolation(p1, p2, p3)
                    print(f"Coeficientes do polinômio interpolador: a2 = {a2}, a1 = {a1}, a0 = {a0}")
                except ValueError as e:
                    print(e)
        elif choice == '4':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    p3 = points[2]
                    a2, a1, a0 = quadratic_interpolation(p1, p2, p3)
                    print(f"Polinômio interpolador: P2(x) = {a2}*x^2 + {a1}*x + {a0}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    p3 = points[2]
                    a2, a1, a0 = quadratic_interpolation(p1, p2, p3)
                    x = float(input("Digite o valor de x: "))
                    y = calculate_interpolated_value(a2, a1, a0, x)
                    print(f"O valor interpolado em x = {x} é y = {y}")
                except ValueError as e:
                    print(e)
        elif choice == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
