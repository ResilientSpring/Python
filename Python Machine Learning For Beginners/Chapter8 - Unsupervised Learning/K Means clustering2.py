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
km_model = KMeans(n_clusters=4);
km_model.fit(X=features_numpy);

## printing the predicted labels
print(km_model.labels_);

## printing the data points
plt.scatter(x=features_numpy[:, 0], y=features_numpy[:, 1], c=km_model.labels_,
            cmap="rainbow");

## print the centroids
plt.scatter(x=km_model.cluster_centers_[:, 0], y=km_model.cluster_centers_[:, 1], s=100,
            c="black");

plt.show();