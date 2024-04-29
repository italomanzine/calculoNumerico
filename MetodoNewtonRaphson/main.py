import sympy as sp
from newton_raphson import newton_raphson, plot_newton_raphson, print_table

def main():
    x = sp.symbols('x')  # Cria uma variável simbólica 'x'
    print("Método de Newton-Raphson para encontrar a raiz de uma função.")

    func_expr = input("Informe a função matemática, usando 'x' como variável (por exemplo: 'x**2 - 3'): ")
    f = sp.lambdify(x, sp.sympify(func_expr), 'numpy')
    df = sp.lambdify(x, sp.diff(sp.sympify(func_expr), x), 'numpy')

    x0 = float(input("Digite o valor inicial (x0): "))
    tol = float(input("Digite a tolerância desejada (e.g., 0.001): "))
    max_iter = int(input("Digite o número máximo de iterações: "))

    root, iterations, x_values, iterations_data = newton_raphson(f, df, x0, tol, max_iter)
    if root is not None:
        print(f"A raiz aproximada é: {root} encontrada em {iterations} iterações.")
        print_table(iterations_data, tol)  # Exibe a tabela de iterações
        plot_newton_raphson(f, df, x_values)  # Esta função agora é chamada corretamente
    else:
        print("O método não convergiu após o número máximo de iterações.")

if __name__ == "__main__":
    main()
