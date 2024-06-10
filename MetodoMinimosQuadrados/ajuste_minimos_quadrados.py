import numpy as np

def input_points():
    """
    Solicita ao usuário o número de pontos e as coordenadas desses pontos.
    Assegura que os dados inseridos sejam convertidos para os tipos corretos e armazenados como uma lista de tuplas (x, y).
    """
    while True:
        try:
            m = int(input("Digite o número de pontos: "))
            if m < 2:
                print("É necessário pelo menos dois pontos para realizar o ajuste linear.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    points = []
    for i in range(m):
        while True:
            try:
                x = float(input(f"Digite a coordenada x do ponto {i+1}: "))
                y = float(input(f"Digite a coordenada y do ponto {i+1}: "))
                points.append((x, y))
                break
            except ValueError:
                print("Por favor, digite um número válido para as coordenadas.")

    return points

def display_points(points):
    """
    Exibe os pontos atuais inseridos pelo usuário em formato de tabela.
    Útil para verificar visualmente os dados antes de realizar cálculos.
    """
    print("Pontos atuais:")
    print("| i | xi     | f(xi)  |")
    for i, (x, y) in enumerate(points):
        print(f"| {i+1} | {x:.4f} | {y:.4f} |")

def calculate_linear_regression_details(points):
    """
    Calcula os detalhes da regressão linear incluindo somatórios, sistema e resíduos.
    """
    X = np.array([x for x, y in points])
    Y = np.array([y for x, y in points])

    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_x2 = np.sum(X**2)
    sum_xy = np.sum(X * Y)

    # Resolução do sistema linear para encontrar coeficientes
    A = np.array([[n, sum_x], [sum_x, sum_x2]])
    b = np.array([sum_y, sum_xy])
    coefficients = np.linalg.solve(A, b)
    a0, a1 = coefficients

    # Cálculo dos resíduos
    Y_pred = a0 + a1 * X
    residuals = Y - Y_pred
    sum_squared_residuals = np.sum(residuals**2)

    # Exibir detalhes
    print("a) Cálculo dos somatórios:")
    print(f"Somatória xi = {sum_x}, Somatória xi^2 = {sum_x2}, Somatória yi = {sum_y}, Somatória xi*yi = {sum_xy}")
    print("b) Resolução do sistema:")
    print("Sistema linear:")
    print(f"| {n:.4f} {sum_x:.4f} | | a0 |   = | {sum_y:.4f}  |")
    print(f"| {sum_x:.4f} {sum_x2:.4f} | | a1 |   = | {sum_xy:.4f} |")
    print(f"Coeficientes: a0 = {a0:.4f}, a1 = {a1:.4f}")
    print("c) Cálculo dos quadrados dos resíduos:")
    print(f"Resíduos quadrados: {sum_squared_residuals:.4f}")

    return a0, a1

def calculate_quadratic_regression_details(points):
    """
    Calcula os detalhes da regressão quadrática incluindo somatórios, sistema e resíduos.
    """
    X = np.array([x for x, y in points])
    Y = np.array([y for x, y in points])

    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(Y)
    sum_x2 = np.sum(X**2)
    sum_x3 = np.sum(X**3)
    sum_x4 = np.sum(X**4)
    sum_xy = np.sum(X * Y)
    sum_x2y = np.sum(X**2 * Y)

    # Resolução do sistema quadrático para encontrar coeficientes
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    b = np.array([sum_y, sum_xy, sum_x2y])
    coefficients = np.linalg.solve(A, b)
    a0, a1, a2 = coefficients

    # Cálculo dos resíduos
    Y_pred = a0 + a1 * X + a2 * X**2
    residuals = Y - Y_pred
    sum_squared_residuals = np.sum(residuals**2)

    # Exibir detalhes
    print("a) Cálculo dos somatórios:")
    print(f"Somatória xi = {sum_x}, Somatória xi^2 = {sum_x2}, Somatória xi^3 = {sum_x3}, Somatória xi^4 = {sum_x4}, Somatória f(xi) = {sum_y}")
    print(f"Somatória xi*yi = {sum_xy}, Somatória xi^2*yi = {sum_x2y}")
    print("b) Resolução do sistema:")
    print("Sistema quadrático:")
    print(f"| {n:.4f} {sum_x:.4f} {sum_x2:.4f} | | a0 |   = | {sum_y:.4f}  |")
    print(f"| {sum_x:.4f} {sum_x2:.4f} {sum_x3:.4f} | | a1 |   = | {sum_xy:.4f} |")
    print(f"| {sum_x2:.4f} {sum_x3:.4f} {sum_x4:.4f} | | a2 |   = | {sum_x2y:.4f} |")
    print(f"Coeficientes: a0 = {a0:.4f}, a1 = {a1:.4f}, a2 = {a2:.4f}")
    print("c) Cálculo dos quadrados dos resíduos:")
    print(f"Resíduos quadrados: {sum_squared_residuals:.4f}")

    return a0, a1, a2

def main():
    """
    Menu principal para interação do usuário com o programa.
    """
    points = []
    while True:
        print("\nMenu:")
        print("1. Inserir os dados para os pontos")
        print("2. Visualizar os pontos atuais")
        print("3. Executar o ajuste linear pelo método dos mínimos quadrados")
        print("4. Executar o ajuste polinomial (quadrático) pelo método dos mínimos quadrados")
        print("5. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            points = input_points()
        elif choice == '2':
            display_points(points)
        elif choice == '3':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar o ajuste linear.")
            else:
                a0, a1 = calculate_linear_regression_details(points)
                print(f"A equação da reta ajustada é y = {a0:.4f} + {a1:.4f}x")
        elif choice == '4':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar o ajuste quadrático.")
            else:
                a0, a1, a2 = calculate_quadratic_regression_details(points)
                print(f"A equação do polinômio ajustado é y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x^2")
        elif choice == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
