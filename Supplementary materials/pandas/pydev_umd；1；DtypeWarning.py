# The low_memory option is not properly deprecated, but it should be,
# since it does not actually do anything differently.

# The reason you get this low_memory warning is because guessing dtypes for
# each column is very memory demanding.
# Pandas tries to determine what dtype to set by analyzing the data in each column.

# Pandas can only determine what dtype a column should have once the whole file is read.
# This means nothing can really be parsed before the whole file is read
# unless you risk having to change the dtype of that column when you read the last value.

# Specifying dtypes (should always be done) by adding dtype={'user_id': int}
# to the pd.read_csv() call will make pandas know when it starts reading the file,
# that this is only integers. [1][2]

# References
# 1. https://www.google.com/search?q=pydev_umd%3A1%3A+DtypeWarning&oq=pydev_umd%3A1%3A+DtypeWarning&aqs=chrome..69i57.1588j0j7&sourceid=chrome&ie=UTF-8
# 2. https://stackoverflow.com/a/27232309/14900011