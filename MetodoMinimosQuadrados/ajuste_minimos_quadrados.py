import numpy as np
from scipy.stats import linregress

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
    print("| i | xi     | f(xi)   |")
    for i, (x, y) in enumerate(points):
        print(f"| {i+1} | {x:.4f} | {y:.4f} |")

def linear_least_squares(points):
    """
    Separa os valores de x e y dos pontos e calcula os coeficientes da reta de melhor ajuste usando o método dos mínimos quadrados.
    """
    X = np.array([x for x, y in points])
    Y = np.array([y for x, y in points])  # Corrigido para garantir que Y é unidimensional
    try:
        slope, intercept, r_value, p_value, std_err = linregress(X, Y)
        return intercept, slope
    except Exception as e:
        print(f"Erro ao executar o ajuste linear: {e}")
        print(f"X: {X}")
        print(f"Y: {Y}")
        return None, None

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
        print("4. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            points = input_points()
        elif choice == '2':
            display_points(points)
        elif choice == '3':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para realizar o ajuste linear.")
            else:
                intercept, slope = linear_least_squares(points)
                if intercept is not None and slope is not None:
                    print(f"A equação da reta ajustada é y = {intercept:.4f} + {slope:.4f}x")
                else:
                    print("Não foi possível calcular o ajuste linear.")
        elif choice == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
