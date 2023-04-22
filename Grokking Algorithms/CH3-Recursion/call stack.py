def greet(name):
    print("hello, " + name + "!")

    greet2(name)
    print("getting ready to say bye...")

    bye()


def greet2(name):
    print("how are you, " + name + "?")


def bye():
    print("ok, bye!")


# Suppose you call greet("maggie")
# First, your computer allocates a box of memory for that function call.
greet("maggie")
