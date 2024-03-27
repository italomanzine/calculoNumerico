from bisection import bisection, plot_function

def main():
    print("Método da Bisseção para encontrar a raiz de uma função.")
    a = input("Informe o valor inicial de a: ")
    b = input("Informe o valor inicial de b: ")
    tol = input("Informe a tolerância desejada: ")

    # Convertendo strings com vírgula para float
    a = float(a.replace(',', '.'))
    b = float(b.replace(',', '.'))
    tol = float(tol.replace(',', '.'))

    root, middle_points = bisection(a, b, tol)
    if root is not None:
        print(f"A raiz aproximada é: {root}")
        print(f"Pontos médios durante a bisseção: {middle_points}")
        plot_function(a, b, root, tol)
    else:
        print("Não foi possível encontrar a raiz com os valores fornecidos.")

if __name__ == "__main__":
    main()
