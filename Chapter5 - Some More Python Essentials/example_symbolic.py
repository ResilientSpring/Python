import sympy as sym

x = 2
y = 3
z = x * y

x, y = sym.symbols('x y')

print(2 * x + 3*x - y)               # Algebraic computation
print(sym.diff(x**2, x))             # Differentiate x**2 wrt. x
print(sym.integrate(sym.cos(x), x))  # Integrates cos(x) wrt. x
print(sym.simplify((x ** 2 + x ** 3) / x ** 2))  # Simplifies expression

