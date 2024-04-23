import sympy as sp
from secant_method import secant_method, plot_secant_method

# Defina a variável simbólica
x = sp.symbols('x')

def main():
    # Entrada do usuário para a função
    # Exemplo: Para uma função f(x) = x^2 + x - 6
    # O usuário deve digitar 'x**2 + x - 6'
    function_input = input("Digite a função que deseja encontrar a raiz, usando 'x' como variável: ")
    f_expr = sp.sympify(function_input)  # Converte a entrada do usuário em uma expressão sympy
    f = sp.lambdify(x, f_expr, 'numpy')  # Converte a expressão sympy para uma função numpy

    # Continuação do código para ler os outros parâmetros e executar o método da secante
    x0 = float(input("Digite o primeiro valor inicial x0: "))
    x1 = float(input("Digite o segundo valor inicial x1: "))
    tol = float(input("Digite a tolerância desejada: "))
    max_iter = int(input("Digite o número máximo de iterações: "))

    # Executa o método da secante
    root, iterations, x_values = secant_method(f, x0, x1, tol, max_iter)

    if root is not None:
        print(f"A raiz aproximada é: {root}, encontrada em {iterations} iterações.")
        plot_secant_method(x_values, f)
    else:
        print("O método da secante não convergiu.")

if __name__ == "__main__":
    main()
