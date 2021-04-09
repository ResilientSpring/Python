import Decision_boundary_visualization as dbv
import Iris_dataset2 as training_set
import Train
import matplotlib.pyplot as plt

dbv.plot_decision_regions(X=training_set.X, y=training_set.y3, classifier=Train.ppn);
plt.xlabel("sepal length [cm]");
plt.ylabel("petal length [cm]");
plt.legend(loc="upper left");

plt.savefig("boundary.jpg");

plt.show();