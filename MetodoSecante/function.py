import sympy as sp

# Define a variável simbólica x
x = sp.symbols('x')

# Substitua esta expressão pela função específica do Exercício 1 do PDF
# Exemplo: Para uma função f(x) = x^2 + x - 6
f_expr = x**2 + x - 6

# Converte a expressão simbólica em uma função numérica para cálculo
f = sp.lambdify(x, f_expr, 'numpy')
