import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# importing the dataset
iris_df = sns.load_dataset("iris");

print(iris_df.head())

# Creating feature set
X = iris_df.drop(["species"], axis=1)

# Creating label set
y = iris_df["species"]

# Converting labels to numbers
