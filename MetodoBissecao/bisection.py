# Importação da função que vamos encontrar a raiz e bibliotecas necessárias para a plotagem
from function import f
import matplotlib.pyplot as plt
import numpy as np

# Função para plotar a função e a raiz aproximada
def plot_function(a, b, root, tol):
    
    x = np.linspace(a - 1, b + 1, 400) # Gera uma série de pontos entre a e b para o traçado do gráfico da função    
    y = f(x) # Calcula os valores correspondentes de f(x) para esses pontos    
    plt.axhline(0, color='black', lw=2) # Plota uma linha horizontal no eixo das ordenadas (y=0)    
    plt.plot(x, y, label='f(x)') # Plota o gráfico da função f(x)        
    plt.plot(root, f(root), 'ro', label='Raiz aproximada') # Marca o ponto da raiz aproximada encontrada no gráfico
    
    # Define as etiquetas dos eixos e o título do gráfico
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de f(x)')
    
    plt.legend() # Adiciona uma legenda ao gráfico    
    plt.grid(True) # Adiciona uma grade ao gráfico para facilitar a leitura    
    plt.show() # Exibe o gráfico

# Função que implementa o método da bisseção
def bisection(a, b, tol):
    # Verifica se os valores iniciais satisfazem a condição do teorema do valor intermediário
    if f(a) * f(b) >= 0:
        # Se não satisfazem, imprime uma mensagem de erro e retorna valores nulos
        print("A bisseção requer que f(a) e f(b) tenham sinais opostos.")
        return None, None

    
    middle = a # Inicializa a variável para armazenar o ponto médio do intervalo    
    middle_points = [] # Lista para armazenar todos os pontos médios calculados durante o método

    # Enquanto a diferença entre b e a for maior que a tolerância especificada, continua o método
    while (b - a) / 2.0 > tol:
        
        middle = (a + b) / 2.0 # Atualiza o ponto médio        
        middle_points.append(middle) # Adiciona o ponto médio atual à lista de pontos médios
        
        # Verifica se encontramos a raiz exata ou se devemos ajustar os limites do intervalo
        if f(middle) == 0:  # Se f(middle) é zero, encontramos a raiz exata
            return middle, middle_points
        elif f(a) * f(middle) < 0:  # Se f(a) e f(middle) têm sinais opostos, a raiz está entre a e middle
            b = middle
        else:  # Se f(middle) e f(b) têm sinais opostos, a raiz está entre middle e b
            a = middle

    # Retorna o ponto médio final como a raiz aproximada e a lista de todos os pontos médios calculados
    return (a + b) / 2.0, middle_points
