import sympy as sym

x = 2
y = 3
z = x * y

print(z)

x, y = sym.symbols('x y') # define x and y as a mathematical symbols.
z = x * y
print(z)
