# .loc, .iloc, and also [] indexing can accept a callable as indexer.

# Getting values from an object with multi-axes selection uses the following notation
# (using .loc as an example, but the following applies to .iloc as well).

# Any of the axes accessors may be the null slice :.
# Axes left out of the specification are assumed to be :,
# e.g. p.loc['a'] is equivalent to p.loc['a', :, :].

# Reference:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#different-choices-for-indexing