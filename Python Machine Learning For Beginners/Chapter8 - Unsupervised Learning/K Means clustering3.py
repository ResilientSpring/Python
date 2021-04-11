import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import dataset as data

# training KMeans on K values from 1 to 10
loss = [];

for i in range(1, 11):
    km = KMeans(n_clusters=i).fit(X=data.features_numpy);

    loss.append(km.inertia_);

# printing the loss against the number of clusters.
plt.plot(range(1, 11), loss);
plt.title("Finding Optimal Clusters via Elbow Method");
plt.xlabel("Number of Clusters");
plt.ylabel("loss");

plt.savefig("inertia.jpg");

plt.savefig()

plt.show();
