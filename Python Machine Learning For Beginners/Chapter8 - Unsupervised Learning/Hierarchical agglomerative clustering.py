import numpy as np
import pandas as pd
from sklearn.datasets._samples_generator import make_blobs
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# generating dummy data of 10 records with 2 clusters.
features, labels = make_blobs(n_samples=10, centers=2, cluster_std=2.00, n_features=2,
                              random_state=1, return_centers=False);
print(labels);
print(features);

# plotting the dummy data
plt.scatter(x=features[:, 0], y=features[:, 1], c="r");

# adding numbers to data points
annots = range(1, 11);
zipper = zip(annots, features[:, 0], features[:, 1]);
print(tuple(zipper));

for label, x, y in zipper:
    plt.annotate(label, xy=(x, y), xytext=(-3, 3), textcoords="offset points", ha="right",
                 va="bottom");

plt.savefig("cluster.jpg");

plt.show();

dendos = linkage(y=features, method="single");

annots = range(1, 11);
dendrogram(Z=dendos, orientation="top", labels=annots, distance_sort="descending", show_leaf_counts=True);

plt.savefig("dendrograms.jpg");

plt.show();