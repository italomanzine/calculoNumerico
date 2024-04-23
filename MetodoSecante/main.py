from function import f
from secant_method import secant_method, plot_secant_method

def main():
    print("Método da Secante para encontrar a raiz de uma função.")
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
