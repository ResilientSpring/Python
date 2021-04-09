import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
print(y3)

# extract the first feature column (sepal length) and
# the third feature column (petal length) of those 100 training examples and assign them
# to a feature matrix, X.
X1 = df.iloc[0:100, [0, 2]].to_numpy();
print(X1);

X = df.iloc[0:100, [0, 2]].to_numpy();
print(X);

# plot data
plt.scatter(x=X[:50, 0], y=X[:50, 1], c="red", marker='o', label="setosa");
plt.scatter(x=X[50:100, 0], y=X[50:100, 1], c="blue", marker='x', label="versicolor");

plt.xlabel("sepal length [cm]");
plt.ylabel("petal length [cm]");
plt.legend(loc="upper left");

plt.savefig('iris_dataset.jpg');

plt.show();

# References:
# 1. https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#column-and-index-locations-and-names