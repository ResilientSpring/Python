import numpy as np
import pandas as pd
from sklearn.datasets._samples_generator import make_blobs
from matplotlib import pyplot as plt

# generating dummy data of 10 records with 2 clusters.
features, labels = make_blobs(n_samples=10, centers=2, cluster_std=2.00)

# plotting the dummy data
plt.scatter(x=features[:, 0], y=features[:, 1], color='r')

# adding numbers to data points
annots = range(1, 11)

for label, x, y in zip(annots, features[:, 0], features[:, 1]):
    plt.annotate(text=label, xy=(x, y), xytext=(-3, 3), textcoords='offset points', ha='right', va='bottom')


plt.show()
