import numpy as np

def input_points():
    """
    Solicita ao usuário o número de pontos e as coordenadas desses pontos.
    
    Returns:
        points (list of tuples): Lista de pontos (x, y).
    """
    try:
        m = int(input("Digite o número de pontos: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
        return []
    
    points = []
    for i in range(m):
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

def linear_least_squares(points):
    """
    Calcula os coeficientes da reta de melhor ajuste pelo método dos mínimos quadrados.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
        
    Returns:
        (float, float): Coeficientes a1 e a2 da reta ajustada y = a1 + a2*x.
    """
    m = len(points)
    X = np.array([x for x, y in points])
    Y = np.array([y for y in points])
    
    A = np.vstack([np.ones(m), X]).T
    a1, a2 = np.linalg.lstsq(A, Y, rcond=None)[0]
    
    return a1, a2

def quadratic_least_squares(points):
    """
    Calcula os coeficientes do polinômio quadrático de melhor ajuste pelo método dos mínimos quadrados.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
        
    Returns:
        (float, float, float): Coeficientes a0, a1 e a2 do polinômio ajustado y = a0 + a1*x + a2*x^2.
    """
    m = len(points)
    X = np.array([x for x, y in points])
    Y = np.array([y for y in points])
    
    A = np.vstack([np.ones(m), X, X**2]).T
    a0, a1, a2 = np.linalg.lstsq(A, Y, rcond=None)[0]
    
    return a0, a1, a2

def calculate_adjusted_value(a, x, degree):
    """
    Calcula o valor ajustado para um valor específico de x.
    
    Args:
        a (tuple): Coeficientes da função ajustada.
        x (float): Valor de x para o qual se deseja calcular o valor ajustado.
        degree (int): Grau do polinômio ajustado (1 para linear, 2 para quadrático).
        
    Returns:
        float: Valor ajustado.
    """
    if degree == 1:
        a1, a2 = a
        return a1 + a2 * x
    elif degree == 2:
        a0, a1, a2 = a
        return a0 + a1 * x + a2 * x**2
    else:
        raise ValueError("Grau do polinômio não suportado.")

def calculate_residual_sum_of_squares(points, a, degree):
    """
    Calcula a soma dos quadrados dos resíduos.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
        a (tuple): Coeficientes da função ajustada.
        degree (int): Grau do polinômio ajustado (1 para linear, 2 para quadrático).
        
    Returns:
        float: Soma dos quadrados dos resíduos.
    """
    residuals = 0.0
    for x, y in points:
        y_adjusted = calculate_adjusted_value(a, x, degree)
        residuals += (y - y_adjusted) ** 2
    
    return residuals

def main():
    """
    Função principal que gerencia o menu interativo e as operações do programa.
    """
    points = []
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados para os pontos")
        print("2. Visualizar os pontos atuais")
        print("3. Executar o ajuste linear pelo método dos mínimos quadrados")
        print("4. Executar o ajuste polinomial (quadrático) pelo método dos mínimos quadrados")
        print("5. Exibir as funções ajustadas")
        print("6. Calcular e exibir o valor ajustado para um valor específico de x")
        print("7. Calcular e exibir a soma dos quadrados dos resíduos")
        print("8. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            points = input_points()
        elif choice == '2':
            display_points(points)
        elif choice == '3':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar o ajuste linear.")
            else:
                try:
                    a1, a2 = linear_least_squares(points)
                    print(f"Coeficientes da reta ajustada: a1 = {a1}, a2 = {a2}")
                except ValueError as e:
                    print(e)
        elif choice == '4':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar o ajuste quadrático.")
            else:
                try:
                    a0, a1, a2 = quadratic_least_squares(points)
                    print(f"Coeficientes do polinômio ajustado: a0 = {a0}, a1 = {a1}, a2 = {a2}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            if len(points) < 2:
                print("É necessário realizar um ajuste primeiro.")
            else:
                if len(points) >= 2:
                    a1, a2 = linear_least_squares(points)
                    print(f"Função linear ajustada: y = {a1} + {a2}*x")
                if len(points) >= 3:
                    a0, a1, a2 = quadratic_least_squares(points)
                    print(f"Função quadrática ajustada: y = {a0} + {a1}*x + {a2}*x^2")
        elif choice == '6':
            if len(points) < 2:
                print("É necessário realizar um ajuste primeiro.")
            else:
                try:
                    x = float(input("Digite o valor de x: "))
                    if len(points) >= 2:
                        a1, a2 = linear_least_squares(points)
                        y_linear = calculate_adjusted_value((a1, a2), x, 1)
                        print(f"O valor ajustado pela função linear em x = {x} é y = {y_linear}")
                    if len(points) >= 3:
                        a0, a1, a2 = quadratic_least_squares(points)
                        y_quadratic = calculate_adjusted_value((a0, a1, a2), x, 2)
                        print(f"O valor ajustado pela função quadrática em x = {x} é y = {y_quadratic}")
                except ValueError as e:
                    print(e)
        elif choice == '7':
            if len(points) < 2:
                print("É necessário realizar um ajuste primeiro.")
            else:
                if len(points) >= 2:
                    a1, a2 = linear_least_squares(points)
                    rss_linear = calculate_residual_sum_of_squares(points, (a1, a2), 1)
                    print(f"Soma dos quadrados dos resíduos (linear): {rss_linear}")
                if len(points) >= 3:
                    a0, a1, a2 = quadratic_least_squares(points)
                    rss_quadratic = calculate_residual_sum_of_squares(points, (a0, a1, a2), 2)
                    print(f"Soma dos quadrados dos resíduos (quadrático): {rss_quadratic}")
        elif choice == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
