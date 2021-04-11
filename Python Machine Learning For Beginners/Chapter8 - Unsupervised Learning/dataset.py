import seaborn as sns
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris_df = sns.load_dataset("iris")
print(iris_df.head());

# drop the class labels.
features = iris_df.drop(labels=["species"], axis=1);
labels = iris_df.filter(items=["species"], axis=1);
print(features.head());

# performs K Means clustering on the Iris dataset.
features_numpy = features.to_numpy();