# Object selection has had a number of user-requested additions in order to support
# more explicit location based indexing.
# pandas now supports three types of multi-axis indexing.

# .loc is primarily label based, but may also be used with a boolean array.
# .loc will raise KeyError when the items are not found. Allowed inputs are:
#
#    A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index.
#    This use is not an integer position along the index.).
#
#    A list or array of labels ['a', 'b', 'c'].
#
#    A slice object with labels 'a':'f' (Note that contrary to usual Python slices,
#    both the start and the stop are included, when present in the index!
#    See Slicing with labels and Endpoints are inclusive.)
#
#    A boolean array (any NA values will be treated as False).
#
#    A callable function with one argument (the calling Series or DataFrame)
#    and that returns valid output for indexing (one of the above).

# Source:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#different-choices-for-indexing