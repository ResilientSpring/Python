# To refer to items from a module within your program's namespace, you can use the
# from... import statement.

# When you import modules this way, you can refer to the functions by name
# rather than through dot notation.

# On page 208.


# importing one specific function, randint(), from the random module
from random import randint

for i in range(10):

    # When we implement this function within our program, we will no longer write
    # the function in dot notation as "random.randint()" but instead will just write "randint()"
    c = randint(a=1, b=25)

    print(c)