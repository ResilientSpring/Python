# Example on page 87 of the textbook.

# It is possible to have several return statements in a function.

def check_sign(x):
    if x > 0:
        return "x is positive";
    elif x < 0:
        return "x is negative";
    else:
        return "x is zero";

# Remember that only one of the branches is executed for a single call to check_sign(),
# so depending on the number x, the return may take place from
# any of the three return alternatives.