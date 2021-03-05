# Program for computing the height of a ball in vertical motion.

v0 = 5;  # initial velocity
g = 9.81;  # Acceleration of gravity
t = 0.6;  # Time

# y = v0 * t - 0.5 * g * t ** 2;

y = v0*t;

# print(y);
print( y);

# Comments on how well Python's response corresponds to the actual error.

# a) NameError: name 'hello' is not defined, which I think truly
# corresponds to the actual error.

# b)     v0 = 5;   initial velocity
#                              ^
# SyntaxError: invalid syntax
# This error message was too vague to know what the specific error was.

# c)     v0  5;  # initial velocity
#         ^
# SyntaxError: invalid syntax
# This error message was too vague to know the specific error was.

# d)     pint(y);
# NameError: name 'pint' is not defined
# This error message did not correspond to the actual error.

# e) No error.

# f) No error.

