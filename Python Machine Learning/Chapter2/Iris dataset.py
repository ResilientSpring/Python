import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'; # [1]
print("URL:", s);

df = pd.read_csv(filepath_or_buffer=s, header=None, encoding="utf-8");
print(df.tail(5));

y = df.iloc[0:100, 4].values;
y = np.where(y == "Iris-setosa", -1, 1);

# References:
# 1. https://github.com/rasbt/python-machine-learning-book-3rd-edition/commit/6aa856219c1b85092df28c2a88d2bf85ebbfdfa8