import numpy as np
import sympy as sp

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

def input_function():
    """
    Solicita ao usuário a função que deve ser integrada.
    
    Returns:
        func (function): Função que será integrada.
    """
    x = sp.symbols('x')
    while True:
        try:
            func_str = input("Digite a função a ser integrada em termos de x (por exemplo, exp(x)): ")
            func_sympy = sp.sympify(func_str)
            func = sp.lambdify(x, func_sympy, modules='numpy')
            break
        except (sp.SympifyError, ValueError):
            print("Entrada inválida. Por favor, insira uma função válida em termos de x.")
    return func

def rectangle_rule(f, a, b, n):
    """
    Calcula a integral pelo método dos retângulos.
    
    Args:
        f (function): Função a ser integrada.
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
        integral += f((xi + xi + h) / 2) * h  # Usando ponto médio
    return integral

def trapezoid_rule(f, a, b, n):
    """
    Calcula a integral pelo método dos trapézios.
    
    Args:
        f (function): Função a ser integrada.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos.
        
    Returns:
        float: Valor aproximado da integral.
    """
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        xi = a + i * h
        integral += f(xi)
    integral *= h
    return integral

def simpson_rule(f, a, b, n):
    """
    Calcula a integral pelo método de Simpson.
    
    Args:
        f (function): Função a ser integrada.
        a (float): Limite inferior do intervalo.
        b (float): Limite superior do intervalo.
        n (int): Número de subintervalos (deve ser par).
        
    Returns:
        float: Valor aproximado da integral.
    """
    if n % 2 != 0:
        raise ValueError("O número de subintervalos deve ser par para a regra de Simpson.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        if i % 2 == 0:
            integral += 2 * f(xi)
        else:
            integral += 4 * f(xi)
    integral *= h / 3
    return integral

def main():
    """
    Menu principal para interação do usuário com o programa.
    """
    a = b = n = None
    f = None
    
    while True:
        print("\nMenu:")
        print("1. Inserir os dados do intervalo e o número de subintervalos")
        print("2. Inserir a função a ser integrada")
        print("3. Executar a integração pela Regra dos Retângulos")
        print("4. Executar a integração pela Regra dos Trapézios")
        print("5. Executar a integração pela Regra de Simpson")
        print("6. Sair do programa")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            a, b, n = input_interval_and_subintervals()
        elif choice == '2':
            f = input_function()
        elif choice == '3':
            if a is None or b is None or n is None or f is None:
                print("Por favor, insira os dados do intervalo, o número de subintervalos e a função primeiro.")
            else:
                result = rectangle_rule(f, a, b, n)
                print(f"Resultado da integração pela Regra dos Retângulos: {result:.4f}")
        elif choice == '4':
            if a is None or b is None or n is None or f is None:
                print("Por favor, insira os dados do intervalo, o número de subintervalos e a função primeiro.")
            else:
                result = trapezoid_rule(f, a, b, n)
                print(f"Resultado da integração pela Regra dos Trapézios: {result:.4f}")
        elif choice == '5':
            if a is None or b is None or n is None or f is None:
                print("Por favor, insira os dados do intervalo, o número de subintervalos e a função primeiro.")
            else:
                try:
                    result = simpson_rule(f, a, b, n)
                    print(f"Resultado da integração pela Regra de Simpson: {result:.4f}")
                except ValueError as e:
                    print(e)
        elif choice == '6':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
