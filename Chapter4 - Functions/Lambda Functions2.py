# Example on page 86 of the textbook.

g = lambda x: x ** 2;

#...which is equivalent to:
def g(x):
    return x ** 2;

def f(x):
    return x;

def sum_function_values(f, start, stop):
    """Sum up function values for integer arguments as
    f(start) + f(start + 1) + f(start + 2) + ... + f(stop) """
    S = 0;
    for i in range(start, stop + 1, 1):
        S = S + f(i);

    return S;

print(sum_function_values(lambda x: x, 1, 3));
print(sum_function_values(lambda x: x ** 2, 1, 3));

print("Sum with f becomes {:g}".format(sum_function_values(f, 1, 3)));
print("Sum with g becomes {:g}".format(sum_function_values(g, 1, 3)));