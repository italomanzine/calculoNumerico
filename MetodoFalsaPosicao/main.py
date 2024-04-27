import sympy as sp
from false_position_method import find_roots, print_table, plot_roots

def main():
    """Solicita a função e parâmetros do usuário, executa o método da falsa posição e exibe os resultados."""
    x = sp.symbols('x')  # Define a variável simbólica para x

    function_input = input("Digite a função que deseja encontrar a raiz, usando 'x' como variável: ")
    f_expr = sp.sympify(function_input)  # Converte a entrada em uma expressão sympy
    f = sp.lambdify(x, f_expr, 'numpy')  # Converte para uma função numérica

    a = float(input("Digite o valor inicial de a: "))  # Início do intervalo
    b = float(input("Digite o valor inicial de b: "))  # Final do intervalo
    tol = float(input("Digite a tolerância desejada: "))  # Tolerância de erro
    max_iter = int(input("Digite o número máximo de iterações: "))  # Máximo de iterações

    roots, iterations_data = find_roots(f, a, b, tol, max_iter)  # Encontra as raízes

    if roots:
        print(f"As raízes aproximadas são: {roots}.")
        print_table(iterations_data, tol)  # Exibe a tabela de iterações
        plot_roots(f, roots, a, b)  # Exibe o gráfico
    else:
        print("Não foram encontradas raízes no intervalo dado.")

if __name__ == "__main__":
    main()
