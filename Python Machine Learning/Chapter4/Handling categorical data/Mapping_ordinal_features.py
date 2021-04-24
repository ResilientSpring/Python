import Categorical_data_encoding_with_pandas as dataset
from sklearn.preprocessing import LabelEncoder

size_mapping = {"XL": 3, 'L': 2, 'M': 1}

dataset.df["size"] = dataset.df["size"].map(size_mapping)

print(dataset.df)

inv_size_mapping = {v: k for k, v in size_mapping.items()}

print(dataset.df["size"].map(inv_size_mapping))

class_le = LabelEncoder()

y = class_le.fit_transform(y=dataset.df["class_label"])
print(y)

y_inverse = class_le.inverse_transform(y)
print(y_inverse)