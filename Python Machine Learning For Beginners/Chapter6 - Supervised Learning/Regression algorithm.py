import pandas as pd
import numpy as np
import seaborn as sns

print(sns.get_dataset_names());

tips_df = sns.load_dataset("tips");
print(tips_df.head());