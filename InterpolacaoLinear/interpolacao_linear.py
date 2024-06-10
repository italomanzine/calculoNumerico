import numpy as np

def input_points():
    """
    Solicita ao usuário o número de pontos e as coordenadas desses pontos.
    
    Returns:
        points (list of tuples): Lista de pontos (x, y).
    """
    try:
        n = int(input("Digite o número de pontos: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
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

def linear_interpolation(p1, p2):
    """
    Calcula o polinômio interpolador de primeiro grau entre dois pontos.
    
    Args:
        p1 (tuple): Primeiro ponto (x1, y1).
        p2 (tuple): Segundo ponto (x2, y2).
        
    Returns:
        (float, float): Coeficientes a1 e a0 do polinômio interpolador P1(x) = a1*x + a0.
    """
    x1, y1 = p1
    x2, y2 = p2
    
    if x1 == x2:
        raise ValueError("Os pontos devem ter coordenadas x diferentes.")
    
    a1 = (y2 - y1) / (x2 - x1)
    a0 = y1 - a1 * x1
    
    return a1, a0

def calculate_interpolated_value(a1, a0, x):
    """
    Calcula o valor interpolado para um valor específico de x.
    
    Args:
        a1 (float): Coeficiente a1 do polinômio interpolador.
        a0 (float): Coeficiente a0 do polinômio interpolador.
        x (float): Valor de x para o qual se deseja calcular o valor interpolado.
        
    Returns:
        float: Valor interpolado.
    """
    return a1 * x + a0

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    points = []
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados para os pontos")
        print("2. Visualizar os pontos atuais")
        print("3. Executar a interpolação linear")
        print("4. Exibir a função interpoladora")
        print("5. Calcular e exibir o valor interpolado para um valor específico de x")
        print("6. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            points = input_points()
        elif choice == '2':
            display_points(points)
        elif choice == '3':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    a1, a0 = linear_interpolation(p1, p2)
                    print(f"Coeficientes do polinômio interpolador: a1 = {a1}, a0 = {a0}")
                except ValueError as e:
                    print(e)
        elif choice == '4':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    a1, a0 = linear_interpolation(p1, p2)
                    print(f"Polinômio interpolador: P1(x) = {a1}*x + {a0}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar a interpolação.")
            else:
                try:
                    p1 = points[0]
                    p2 = points[1]
                    a1, a0 = linear_interpolation(p1, p2)
                    x = float(input("Digite o valor de x: "))
                    y = calculate_interpolated_value(a1, a0, x)
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
