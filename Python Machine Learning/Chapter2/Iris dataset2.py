import numpy as np
import pandas as pd

url = \
    "https://raw.githubusercontent.com/rasbt/python-machine-learning-book-3rd-edition/master/ch02/iris.data";

df = pd.read_csv(filepath_or_buffer=url, header=None);
print(df);

# select setosa and versicolor