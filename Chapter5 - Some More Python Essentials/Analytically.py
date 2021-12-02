import sympy as sym

x = sym.symbols('x')

f_expr = 5*x**3 + 2*x**2 - 1    # Symbolic expression for f(x)

dfdx_expr = sym.diff(f_expr, x)   # Compute f'(x) symbolically

# turn symbolic expressions into functions
f = sym.lambdify([x])
