import pandas as pd
import seaborn as sns

print(sns.get_dataset_names());

# To read a particular dataset into the Pandas dataframe,
# pass the dataset name to the load_dataset() method of the Seaborn library.
diamond_df = sns.load_dataset("diamonds");

print(diamond_df.head());