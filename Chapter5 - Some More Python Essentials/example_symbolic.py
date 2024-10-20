import sympy as sym

x = 2
y = 3
z = x * y

x, y = sym.symbols('x y')

print(2 * x + 3*x - y)               # Algebraic computation
print(sym.diff(x**2, x))             # Differentiate x**2 wrt. x
print(sym.integrate(sym.cos(x), x))  # Integrates cos(x) wrt. x
print(sym.simplify((x ** 2 + x ** 3) / x ** 2))  # Simplifies expression
print(sym.limit(sym.sin(x) / x, x, 0))  # lim of sin(x)/x as x -> 0
print(sym.solve(5 * x - 15, x))         # Solve 5 * x = 15
