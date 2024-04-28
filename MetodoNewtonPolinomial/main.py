import sympy as sp
from newton_method_polynomial import find_roots, print_table, plot_roots

def main():
    """ Solicita a função e parâmetros do usuário, executa o Método de Newton e exibe os resultados. """
    x = sp.symbols('x')  # Define a variável simbólica para x

    function_input = input("Digite a função que deseja encontrar a raiz, usando 'x' como variável: ")
    f_expr = sp.sympify(function_input)  # Converte a entrada em uma expressão sympy
    f = sp.lambdify(x, f_expr, 'numpy')  # Converte para uma função numérica

    df_expr = sp.diff(f_expr, x)  # Calcula a derivada da função
    df = sp.lambdify(x, df_expr, 'numpy')  # Converte a derivada para uma função numérica

    x0 = float(input("Digite o valor inicial (chute inicial): "))  # Valor inicial
    tol = float(input("Digite a tolerância desejada: "))  # Tolerância de erro
    max_iter = int(input("Digite o número máximo de iterações: "))  # Máximo de iterações

    root, iterations_data = find_roots(f, df, x0, tol, max_iter)  # Encontra as raízes

    if root is not None:
        print(f"A raiz aproximada é: {root}.")
        print_table(iterations_data)  # Exibe a tabela de iterações
        plot_roots(f, root, x0)  # Exibe o gráfico
    else:
        print("Não foi possível encontrar uma raiz no intervalo dado ou o método não convergiu.")

if __name__ == "__main__":
    main()
