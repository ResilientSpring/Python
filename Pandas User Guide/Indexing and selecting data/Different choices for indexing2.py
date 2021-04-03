# .iloc is primarily integer position based (from 0 to length-1 of the axis),
# but may also be used with a boolean array.
# .iloc will raise IndexError if a requested indexer is out-of-bounds,
# except slice indexers which allow out-of-bounds indexing.

#    Allowed inputs are:

#        An integer e.g. 5.

#        A list or array of integers [4, 3, 0].

#        A slice object with ints 1:7.

#        A boolean array (any NA values will be treated as False).

#        A callable function with one argument (the calling Series or DataFrame) and
#        that returns valid output for indexing (one of the above).

# Source:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#different-choices-for-indexing