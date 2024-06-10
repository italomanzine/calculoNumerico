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
    Exibe os pontos atuais inseridos pelo usuário em formato de tabela.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
    """
    if not points:
        print("Nenhum ponto foi inserido ainda.")
        return
    
    print("Pontos atuais:")
    print("| i | xi  | f(xi) |")
    print("|---|-----|-------|")
    for i, (x, y) in enumerate(points):
        print(f"| {i+1} | {x:.4f} | {y:.4f} |")

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
    
    sum_x = np.sum(X)
    sum_x2 = np.sum(X**2)
    sum_y = np.sum(Y)
    sum_xy = np.sum(X * Y)
    
    a2 = (m * sum_xy - sum_x * sum_y) / (m * sum_x2 - sum_x**2)
    a1 = (sum_y - a2 * sum_x) / m
    
    return a1, a2, sum_x, sum_x2, sum_y, sum_xy

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

def calculate_residuals(points, a, degree):
    """
    Calcula os resíduos e a soma dos quadrados dos resíduos.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
        a (tuple): Coeficientes da função ajustada.
        degree (int): Grau do polinômio ajustado (1 para linear, 2 para quadrático).
        
    Returns:
        tuple: Lista de resíduos e soma dos quadrados dos resíduos.
    """
    residuals = []
    sum_squared_residuals = 0.0
    
    for x, y in points:
        if degree == 1:
            y_adjusted = a[0] + a[1] * x
        elif degree == 2:
            y_adjusted = a[0] + a[1] * x + a[2] * x**2
        
        residual = y - y_adjusted
        residuals.append((x, y, y_adjusted, residual, residual**2))
        sum_squared_residuals += residual**2
    
    return residuals, sum_squared_residuals

def generate_latex_report(points, linear_results, quadratic_results):
    """
    Gera um relatório em formato LaTeX com os resultados dos ajustes.
    
    Args:
        points (list of tuples): Lista de pontos (x, y).
        linear_results (tuple): Resultados do ajuste linear.
        quadratic_results (tuple): Resultados do ajuste quadrático.
    """
    with open("relatorio_minimos_quadrados.tex", "w") as f:
        f.write(r"\documentclass{article}" + "\n")
        f.write(r"\usepackage{amsmath}" + "\n")
        f.write(r"\begin{document}" + "\n")
        f.write(r"\title{Relatório de Ajuste pelo Método dos Mínimos Quadrados}" + "\n")
        f.write(r"\maketitle" + "\n")
        
        f.write(r"\section*{Pontos Tabelados}" + "\n")
        f.write(r"\begin{tabular}{|c|c|c|}\hline" + "\n")
        f.write(r"i & $x_i$ & $f(x_i)$ \\\hline" + "\n")
        for i, (x, y) in enumerate(points):
            f.write(f"{i+1} & {x:.4f} & {y:.4f} \\\hline\n")
        f.write(r"\end{tabular}" + "\n")
        
        f.write(r"\section*{Ajuste Linear}" + "\n")
        a1, a2, sum_x, sum_x2, sum_y, sum_xy = linear_results
        f.write(r"\subsection*{Cálculo dos Somatórios}" + "\n")
        f.write(r"\begin{align*}" + "\n")
        f.write(r"\sum x_i &= " + f"{sum_x:.4f} \\\\\n")
        f.write(r"\sum x_i^2 &= " + f"{sum_x2:.4f} \\\\\n")
        f.write(r"\sum f(x_i) &= " + f"{sum_y:.4f} \\\\\n")
        f.write(r"\sum x_i f(x_i) &= " + f"{sum_xy:.4f} \n")
        f.write(r"\end{align*}" + "\n")
        
        f.write(r"\subsection*{Resolução do Sistema}" + "\n")
        f.write(r"\begin{align*}" + "\n")
        f.write(r"a_2 &= " + f"{a2:.4f} \\\\\n")
        f.write(r"a_1 &= " + f"{a1:.4f} \n")
        f.write(r"\end{align*}" + "\n")
        
        residuals, sum_squared_residuals = calculate_residuals(points, (a1, a2), 1)
        f.write(r"\subsection*{Cálculo dos Resíduos}" + "\n")
        f.write(r"\begin{tabular}{|c|c|c|c|c|c|}\hline" + "\n")
        f.write(r"i & $x_i$ & $f(x_i)$ & $\phi(x_i)$ & $r(x_i)$ & $r^2(x_i)$ \\\hline" + "\n")
        for i, (x, y, y_adjusted, residual, residual_squared) in enumerate(residuals):
            f.write(f"{i+1} & {x:.4f} & {y:.4f} & {y_adjusted:.4f} & {residual:.4f} & {residual_squared:.4f} \\\hline\n")
        f.write(r"\end{tabular}" + "\n")
        f.write(r"\subsection*{Soma dos Quadrados dos Resíduos}" + "\n")
        f.write(r"\begin{equation*}" + "\n")
        f.write(r"\sum r^2(x_i) = " + f"{sum_squared_residuals:.4f}" + "\n")
        f.write(r"\end{equation*}" + "\n")
        
        f.write(r"\section*{Ajuste Quadrático}" + "\n")
        a0, a1, a2 = quadratic_results
        f.write(r"\subsection*{Cálculo dos Somatórios}" + "\n")
        f.write(r"\begin{align*}" + "\n")
        f.write(r"a_0 &= " + f"{a0:.4f} \\\\\n")
        f.write(r"a_1 &= " + f"{a1:.4f} \\\\\n")
        f.write(r"a_2 &= " + f"{a2:.4f} \n")
        f.write(r"\end{align*}" + "\n")
        
        residuals, sum_squared_residuals = calculate_residuals(points, (a0, a1, a2), 2)
        f.write(r"\subsection*{Cálculo dos Resíduos}" + "\n")
        f.write(r"\begin{tabular}{|c|c|c|c|c|c|}\hline" + "\n")
        f.write(r"i & $x_i$ & $f(x_i)$ & $\phi(x_i)$ & $r(x_i)$ & $r^2(x_i)$ \\\hline" + "\n")
        for i, (x, y, y_adjusted, residual, residual_squared) in enumerate(residuals):
            f.write(f"{i+1} & {x:.4f} & {y:.4f} & {y_adjusted:.4f} & {residual:.4f} & {residual_squared:.4f} \\\hline\n")
        f.write(r"\end{tabular}" + "\n")
        f.write(r"\subsection*{Soma dos Quadrados dos Resíduos}" + "\n")
        f.write(r"\begin{equation*}" + "\n")
        f.write(r"\sum r^2(x_i) = " + f"{sum_squared_residuals:.4f}" + "\n")
        f.write(r"\end{equation*}" + "\n")
        
        f.write(r"\end{document}" + "\n")

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
        print("5. Gerar relatório em LaTeX")
        print("6. Sair do programa")
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
                    a1, a2, sum_x, sum_x2, sum_y, sum_xy = linear_least_squares(points)
                    residuals, sum_squared_residuals = calculate_residuals(points, (a1, a2), 1)
                    print("\na) Cálculo dos somatórios:")
                    print(f"Σxi = {sum_x:.4f}")
                    print(f"Σxi^2 = {sum_x2:.4f}")
                    print(f"Σf(xi) = {sum_y:.4f}")
                    print(f"Σxi*f(xi) = {sum_xy:.4f}")
                    print("\nb) Resolução do sistema:")
                    print(f"a1 = {a1:.4f}")
                    print(f"a2 = {a2:.4f}")
                    print("\nc) Cálculo do quadrado dos resíduos:")
                    for i, (x, y, y_adjusted, residual, residual_squared) in enumerate(residuals):
                        print(f"Iteração {i+1}: x = {x:.4f}, f(x) = {y:.4f}, φ(x) = {y_adjusted:.4f}, r(x) = {residual:.4f}, r^2(x) = {residual_squared:.4f}")
                    print(f"Soma dos quadrados dos resíduos: {sum_squared_residuals:.4f}")
                except ValueError as e:
                    print(e)
        elif choice == '4':
            if len(points) < 3:
                print("É necessário pelo menos três pontos para realizar o ajuste quadrático.")
            else:
                try:
                    a0, a1, a2 = quadratic_least_squares(points)
                    residuals, sum_squared_residuals = calculate_residuals(points, (a0, a1, a2), 2)
                    print("\na) Cálculo dos somatórios:")
                    print(f"a0 = {a0:.4f}")
                    print(f"a1 = {a1:.4f}")
                    print(f"a2 = {a2:.4f}")
                    print("\nb) Resolução do sistema:")
                    print(f"a0 = {a0:.4f}")
                    print(f"a1 = {a1:.4f}")
                    print(f"a2 = {a2:.4f}")
                    print("\nc) Cálculo do quadrado dos resíduos:")
                    for i, (x, y, y_adjusted, residual, residual_squared) in enumerate(residuals):
                        print(f"Iteração {i+1}: x = {x:.4f}, f(x) = {y:.4f}, φ(x) = {y_adjusted:.4f}, r(x) = {residual:.4f}, r^2(x) = {residual_squared:.4f}")
                    print(f"Soma dos quadrados dos resíduos: {sum_squared_residuals:.4f}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            if len(points) < 2:
                print("É necessário pelo menos dois pontos para gerar o relatório.")
            else:
                linear_results = linear_least_squares(points)
                quadratic_results = quadratic_least_squares(points)
                generate_latex_report(points, linear_results, quadratic_results)
                print("Relatório gerado em 'relatorio_minimos_quadrados.tex'.")
        elif choice == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
