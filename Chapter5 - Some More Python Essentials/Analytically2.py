import sympy as sym

x = sym.symbols('x')

f_expr = 5*x**3 + 2*x**2 - 1    # Symbolic expression for f(x)

dfdx_expr = sym.diff(f_expr, x)   # Compute f'(x) symbolically

print(f_expr)
print(dfdx_expr)

# turn symbolic expressions into functions for numerical calculations.
f = sym.lambdify([x], f_expr)  # f = lambda x: 5*x**3 + 2*x**2 - 1
dfdx = sym.lambdify([x], dfdx_expr)   # dfdx = lambda x: 15*x**2 4*x

print(f(1), dfdx(1))   # Call and print, x = 1
