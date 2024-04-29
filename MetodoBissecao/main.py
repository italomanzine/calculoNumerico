# Importa as funções necessárias do módulo bisection
from bisection import bisection, plot_function, print_table

def main():
    # Interação inicial com o usuário para receber a função matemática e os parâmetros de execução
    print("Método da Bisseção para encontrar a raiz de uma função.")
    func_expr = input("Informe a função matemática, usando 'x' como variável (por exemplo: 'x**2 - 3'): ")
    a = float(input("Informe o valor inicial de a: ").replace(',', '.'))
    b = float(input("Informe o valor inicial de b: ").replace(',', '.'))
    tol = float(input("Informe a tolerância desejada: ").replace(',', '.'))

    # Executa o algoritmo da bisseção com os parâmetros fornecidos e recebe a raiz e os dados das iterações
    root, iterations_data = bisection(a, b, tol, func_expr)

    # Se uma raiz foi encontrada, exibe os resultados e plota o gráfico
    if root is not None:
        print(f"A raiz aproximada é: {root}")
        print_table(iterations_data, tol)
        plot_function(a, b, root, tol, func_expr)
    else:
        print("Não foi possível encontrar a raiz com os valores fornecidos.")

# Verifica se este script está sendo executado como principal e chama a função main
if __name__ == "__main__":
    main()
