# Importa as funções do arquivo bisection.py
from bisection import bisection, plot_function

def main():
    
    print("Método da Bisseção para encontrar a raiz de uma função.") # Exibe uma mensagem introdutória sobre o programa   
    a = input("Informe o valor inicial de a: ") # Solicita ao usuário o limite inferior do intervalo de busca da raiz    
    b = input("Informe o valor inicial de b: ") # Solicita ao usuário o limite superior do intervalo de busca da raiz    
    tol = input("Informe a tolerância desejada: ") # Solicita ao usuário a tolerância para o critério de parada do método

    # Converte as entradas para números de ponto flutuante, substituindo vírgula por ponto
    a = float(a.replace(',', '.'))
    b = float(b.replace(',', '.'))
    tol = float(tol.replace(',', '.'))

    # Chama a função de bisseção e armazena a raiz encontrada e os pontos médios
    root, middle_points = bisection(a, b, tol)
    if root is not None:  # Se uma raiz foi encontrada        
        print(f"A raiz aproximada é: {root}")# Exibe a raiz aproximada e os pontos médios
        print(f"Pontos médios durante a bisseção: {middle_points}")
        # Plota a função e o ponto de bisseção
        plot_function(a, b, root, tol)
    else:  # Se não foi possível encontrar a raiz
        print("Não foi possível encontrar a raiz com os valores fornecidos.")

# Verifica se este script é o principal e chama a função main
if __name__ == "__main__":
    main()
