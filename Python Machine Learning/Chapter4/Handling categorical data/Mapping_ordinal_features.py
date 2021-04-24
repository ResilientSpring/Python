import Categorical_data_encoding_with_pandas as dataset

size_mapping = {"XL": 3, 'L': 2, 'M': 1}

dataset.df["size"] = dataset.df["size"].map(size_mapping)

print(dataset.df)

inv_size_mapping = {v: k for k, v in size_mapping.items()}

print(dataset.df["size"].map(inv_size_mapping))