import sympy as sp

# Define a variável simbólica x para usar nas funções
x = sp.symbols('x')

# Definição da função e sua derivada
f_expr = 2 * x - sp.sin(x) - 4  # Função dada no exercício
df_expr = sp.diff(f_expr, x)  # Derivada da função

# Converte as expressões simbólicas em funções numéricas
f = sp.lambdify(x, f_expr, 'numpy')
df = sp.lambdify(x, df_expr, 'numpy')
