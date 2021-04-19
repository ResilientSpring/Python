import pandas as pd
import numpy as np
import seaborn as sns

print(sns.get_dataset_names());

diamond_df = sns.load_dataset("diamonds");
print(diamond_df);

# Train a regression algorithm of your choice, which predicts the price of the diamond.
# Perform all the preprocessing steps.

# Dividing Data into Features and Labels

## label set
label = diamond_df["price"];
print(label);

## feature set