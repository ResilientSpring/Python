from sklearn.cluster import KMeans
from sklearn import preprocessing
import dataset as data
import matplotlib.pyplot as plt

le = preprocessing.LabelEncoder();
labels = le.fit_transform(y=data.labels);

# printing the data points with original labels
plt.scatter(x=data.features_numpy[:, 0], y=data.features_numpy[:, 1], c=labels,
            cmap="rainbow");

plt.savefig("inertia2.jpg");

plt.show();