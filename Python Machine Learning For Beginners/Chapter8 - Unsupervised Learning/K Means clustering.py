import numpy as np
import pandas as pd
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

# generating dummy data of 500 records with 4 clusters
features, labels = make_blobs(n_samples=500, centers=4, cluster_std=2.00);

# plotting the dummy data
plt.scatter(x=features[:, 0], y=features[ : , 1]);

plt.savefig("to_be_clustered.jpg");

plt.show();

# Performing k-means clustering using KMeans class
km_model = KMeans(n_clusters=4);
km_model.fit(X=features);

## printing cluster centers
print(km_model.cluster_centers_);

## printing predicted labels
print(km_model.labels_);

## ploting the data points
plt.scatter(x=features[:, 0], y=features[:, 1], c=km_model.labels_, cmap="rainbow");

## ploting the centroids
plt.scatter(x=km_model.cluster_centers_[: , 0], y=km_model.cluster_centers_[:, 1],
            s=100, c="black");

plt.show();