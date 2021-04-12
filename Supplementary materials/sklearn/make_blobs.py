from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=10, n_features=2, centers=3, random_state=0, cluster_std=2.00);
print(X.shape);
print(X);
print(y);

# source: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html