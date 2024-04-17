# Arquivo principal para interação do usuário e execução do método de Newton-Raphson.

from newton_raphson import newton_raphson, plot_newton_raphson
from function import f, df

def main():
    print("Método de Newton-Raphson para encontrar a raiz da função.")
    x0 = float(input("Digite o valor inicial (x0): "))
    tol = float(input("Digite a tolerância desejada (e.g., 0.001): "))
    max_iter = int(input("Digite o número máximo de iterações: "))
    
    # Chama o método de Newton-Raphson e obtém a raiz e os valores de x das iterações
    root, iterations, x_values = newton_raphson(x0, tol, max_iter)
    if iterations < max_iter:
        print(f"A raiz aproximada é: {root} encontrada em {iterations} iterações.")
        # Plota a função e as tangentes das iterações
        plot_newton_raphson(x_values, f, df)
    else:
        print("O método não convergiu após o número máximo de iterações.")

if __name__ == "__main__":
    main()
