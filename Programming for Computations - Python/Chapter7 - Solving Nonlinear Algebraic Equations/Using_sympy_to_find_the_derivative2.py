import sympy as sym

x = sym.symbols('x')
f_expression = x**2 - 9   # symbolic expression for f(x)
dfdx_expression = sym.diff(f_expression, x)  # compute f'(x) symbolically

# turn f_expression and dfdx_expression into plan Python functions
f = sym.lambdify(x, f_expression)
dfdx = sym.lambdify(x, dfdx_expression)

print(f(3), dfdx(3))
