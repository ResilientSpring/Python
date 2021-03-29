import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'; # [1]
print("URL:", s);

df = pd.read_csv(filepath_or_buffer=s, header=None, encoding="utf-8");
print(df.tail(5));

y = df.iloc[0:100, 4].values; # Extract the first 100 class labels that correspond to the 50 Iris-versicolor flower.
y = np.where(y == "Iris-setosa", -1, 1); # Convert the class labels into the two integer class labels, 1 (versicolor) and -1 (setosa), that we assign to a vector y, where the values method of a pandas yields the corresponding NumPy representation.

# References:
# 1. https://github.com/rasbt/python-machine-learning-book-3rd-edition/commit/6aa856219c1b85092df28c2a88d2bf85ebbfdfa8