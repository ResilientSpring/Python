# Reference: https://docs.python.org/3/tutorial/introduction.html

print(2+2);
print(50 - 5 * 6);
print((50 - 5 * 6 ) / 4);
print(8 / 5);  # division / always returns a floating point number.
print(17 / 3);

# To do floor division and get an integer result (disregarding any fractional result),
# you can use the // operator.
print(17 // 3);

# To calculate the remainder, you can use %:
print(17 % 3);

# With Python, it is possible to use the ** operator to calculate powers:
print(5 ** 2); # 5 squared.
print(2 ** 7); # 2 to the power of 7.

# if a variable is not "defined" (assign a value), trying to use it will give you an error:
# print(n);

# There is full support for floating point;
# operators with mixed type operands convert the integer operand to floating point:
print(4 * 3.75 - 1);

# In interactive mode, the last printed expression is remembered by Python and assigned to
# the variable _.
# This means that when you are using Python as a calculator,
# it is somewhat easier to continue calculations from the last session.
tax = 12.5 / 100;
price = 100.50;
print(price * tax);
# print(price + _);
# print(round(_, 2));