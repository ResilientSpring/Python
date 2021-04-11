from sklearn.cluster import KMeans
import dataset as data
import matplotlib.pyplot as plt

# training KMeans with 3 clusters
km_model = KMeans(n_clusters=3);
km_model.fit(X=data.features_numpy);

# printing the data points with the predicted labels
plt.scatter(x=data.features_numpy[:, 0], y=data.features_numpy[:, 1],
            c=km_model.labels_, cmap="rainbow");

# printing the predicted centroids
plt.scatter(x=km_model.cluster_centers_[:, 0], y=km_model.cluster_centers_[:, 1],
            s=100, c="black");

plt.savefig("inertia.jpg");

plt.show();