# Reference: https://docs.python.org/3/tutorial/introduction.html

# Python knows a number of "compound" data type, used to group together other values.
# The most versatile is the list, which might contain items of different types,
# but usually the items all have the same type.

squares = [1, 4, 9, 16, 25];
print(squares);

# Like strings (and all other built-in sequence types), lists can be indexed and sliced.
print(squares[0]);
print(squares[-1]);
print(squares[-3:]); # Slicing returns a new list.
