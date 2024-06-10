import numpy as np

def input_interval_and_subintervals():
    """
    Solicita ao usuário o intervalo de integração e o número de subintervalos.
    
    Returns:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos.
    """
    while True:
        try:
            a = float(input("Digite o limite inferior do intervalo (a): "))
            b = float(input("Digite o limite superior do intervalo (b): "))
            if b <= a:
                print("O limite superior deve ser maior que o limite inferior. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    while True:
        try:
            n = int(input("Digite o número de subintervalos (n): "))
            if n <= 0:
                print("O número de subintervalos deve ser maior que zero. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

    return a, b, n

def function_to_integrate(x):
    """
    Define a função que será integrada.
    
    Args:
        x (float): Ponto em que a função será avaliada.
        
    Returns:
        float: Valor da função no ponto x.
    """
    return np.exp(x)  # Exemplo de função: f(x) = e^x

def rectangle_rule(a, b, n):
    """
    Calcula a integral pelo método dos retângulos.
    
    Args:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos.
        
    Returns:
        float: Valor aproximado da integral.
    """
    h = (b - a) / n
    integral = 0
    for i in range(n):
        xi = a + i * h
        integral += function_to_integrate((xi + xi + h) / 2) * h  # Usando ponto médio
    return integral

def trapezoid_rule(a, b, n):
    """
    Calcula a integral pelo método dos trapézios.
    
    Args:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos.
        
    Returns:
        float: Valor aproximado da integral.
    """
    h = (b - a) / n
    integral = (function_to_integrate(a) + function_to_integrate(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        integral += function_to_integrate(xi)
    integral *= h
    return integral

def simpson_rule(a, b, n):
    """
    Calcula a integral pelo método de Simpson.
    
    Args:
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos (deve ser par).
        
    Returns:
        float: Valor aproximado da integral.
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos deve ser par para a regra de Simpson.")
    
    h = (b - a) / n
    integral = function_to_integrate(a) + function_to_integrate(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            integral += 2 * function_to_integrate(xi)
        else:
            integral += 4 * function_to_integrate(xi)
    integral *= h / 3
    return integral

def main():
    """
    Menu principal para interação do usuário com o programa.
    """
    a = b = n = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados do intervalo e o número de subintervalos")
        print("2. Executar a integração pela Regra dos Retângulos")
        print("3. Executar a integração pela Regra dos Trapézios")
        print("4. Executar a integração pela Regra de Simpson")
        print("5. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            a, b, n = input_interval_and_subintervals()
        elif choice == '2':
            if a is None or b is None or n is None:
                print("Por favor, insira os dados do intervalo e o número de subintervalos primeiro.")
            else:
                result = rectangle_rule(a, b, n)
                print(f"Resultado da integração pela Regra dos Retângulos: {result:.4f}")
        elif choice == '3':
            if a is None or b is None or n is None:
                print("Por favor, insira os dados do intervalo e o número de subintervalos primeiro.")
            else:
                result = trapezoid_rule(a, b, n)
                print(f"Resultado da integração pela Regra dos Trapézios: {result:.4f}")
        elif choice == '4':
            if a is None or b is None or n is None:
                print("Por favor, insira os dados do intervalo e o número de subintervalos primeiro.")
            else:
                try:
                    result = simpson_rule(a, b, n)
                    print(f"Resultado da integração pela Regra de Simpson: {result:.4f}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
