# Reference: https://docs.python.org/3/tutorial/introduction.html

single_quote = 'spam eggs';
double_quote = "spam eggs";

print(single_quote);
print(double_quote);

Escape = 'doesn\'t';  # Use \' to escape the single quote.
escape = "doesn't";   # or use double quotes instead.

print(Escape);
print(escape);

single_quote2 = '"Yes", they said.';
print(single_quote2);

double_quote2 = "\"Yes\", they said. ";
print(double_quote2);

single_quote3 = '"Isn\'t", they said.';
print(single_quote3);

s = 'First line. \nSecond line';
print(s);

# If you don't want characters prefaced by \ to be interpreted as special characters,
# you can use raw strings by adding an r before the first quote.
print('C:\some\name');   # here \n means newLine!
print("C:\some\name");   # here \n means new Line!

print(r'C:\some\name');
print(r"C:\some\name");

# String literals can span multiple lines.
# One way is using triple-quotes """...""" or '''...'''

print("""
Usage: thingy [OPTIONS]
    -h                           Display this usage message
    -H                           Hostname to connect to 
""")

# End of lines are automatically included in the string, but it's possible to prevent this
# by adding a \ (back-slash) at the end of the line.
print("""\ 
Usage: thingy [OPTIONS]
    -h                           Display this usage message
    -H                           Hostname to connect to 
""");

# print(""\
# Usage: thingy [OPTIONS]
#    -h                           Display this usage message
#    -H                           Hostname to connect to
# "");

my_sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 +\
    19 + 20;

print(my_sum);  # Example on page 36 of Programming for Computations - Python.
print( (1 + 20) * 20 / 2 );

my_sum2 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 \
          + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20;

my_sum3 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 +\
          11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20;

my_sum4 = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + \
          16 + 17 + 18 + 19 + 20;

print(my_sum2 + my_sum3 + my_sum4);
print("my_sum2 = {:d}, my_sum3 = {:d}, my_sum4 = {:d}".format(my_sum2, my_sum3, my_sum4));

# Strings can be concatenated (glue together) with the + operator, and repeated with *
print(3 * "un" + "ium");  # 3 times "un", followed by "ium".

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other
# are automatically concatenated.
print("Py" "thon");