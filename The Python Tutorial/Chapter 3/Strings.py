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
# print(my_sum2 + ", " + my_sum3 + ", " + my_sum4);

# Strings can be concatenated (glue together) with the + operator, and repeated with *
print(3 * "un" + "ium");  # 3 times "un", followed by "ium".

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other
# are automatically concatenated.
print("Py" "thon");

# This feature is particular useful when you want to break long strings.
text = ("Put several strings within parentheses "
        "to have them joined together.");
print(text);

# This only works with two literals though, not with variables or expressions.
prefix = "Py";
# print(prefix 'thon');   cannot concatenate a variable and a string literal.

# If you want to concatenate variables or a variable and literals, use +
print(prefix + "thon");

# Strings can be indexed, with the first character having index 0.
word = "Python";
print(word[0]);  # Character in position 0.
print(word[5]);  # Character in position 5.

# Indices may also be negative numbers, to start counting from the right.
print(word[-1]); # Last character
print(word[-2]); # Second-last character.
print(word[-6]);

# Note that since -0 is the same as 0, negative indices start from -1.
print(word[-0]);
print(word[0]);

# Slicing
print(word[0:2]); # characters from position 0 (included) to 2 (excluded)
print(word[2:5]);

# Slice indices have useful defaults;
# an omitted first index defaults to zero,
# an omitted second index defaults to the size of the string being sliced.
word[:2] ;  # character from the beginning to position 2 (excluded)
word[4:] ;  # characters from position 4 (included) to the end
word[-2:];  # characters from the second-last (included) to the end

# For non-negative indices,
# the length of a slice is the difference of the indices, if both are within bounds.
print(len(word[1:3]));

# Attempting to use an index that is too large will result in an error:
# print( word[42] );  the word only has 6 characters.

# However, out of range slice indexes are handled gracefully when used for slicing.
print(word[4:42]);
print(word[42:]);

# Python strings cannot be changed - they are immutable.
# Thus, assigning to an indexed position in the string results in an error:
# word[0] = 'J';

# If you need a different string, you should create a new one:
new_word = 'J' + word[1:];
print(new_word);