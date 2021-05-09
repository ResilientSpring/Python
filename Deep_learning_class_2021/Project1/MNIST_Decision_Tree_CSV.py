import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

url = "https://media.githubusercontent.com/media/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/mnist_train.csv"

MNIST_data = pd.read_csv(filepath_or_buffer=url, header=None)
print(MNIST_data.head(n=100))

# Feature set
features = MNIST_data.iloc[1:, 1:]
print(features)

# Label set
labels = MNIST_data.iloc[1:, 0]
print(labels)

