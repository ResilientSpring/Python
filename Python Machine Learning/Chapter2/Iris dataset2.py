import numpy as np
import pandas as pd

url = \
    "https://raw.githubusercontent.com/rasbt/python-machine-learning-book-3rd-edition/master/ch02/iris.data";

#  if no names are passed the behavior is identical to header=0 and
#  column names are inferred from the first line of the file.[1]
df = pd.read_csv(filepath_or_buffer=url, header=None);
print(df);

# select setosa and versicolor
y = df.iloc[0:100, 4];
print(y);

y2 = df.iloc[0:100, 4].to_numpy();
print(y2);

# Convert the class labels into the two integer class labels,
# 1 (versicolor) and -1 (setosa).
y3 = np.where(y == "Iris-setosa", -1, 1);

# extract the first feature column (sepal length) and
# the third feature column (petal length) of those 100 training examples and assign them
# to a feature matrix, X.
X = df.iloc[0:100, [0, 2]].to_numpy();

# References:
# 1. https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#column-and-index-locations-and-names