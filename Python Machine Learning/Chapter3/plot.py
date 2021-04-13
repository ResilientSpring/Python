import Decision_boundary_visualization
import numpy as np
import Perceptron_with_scikit
import matplotlib.pyplot as plt

X_combined_std = np.vstack((Perceptron_with_scikit.X_train_std,
                            Perceptron_with_scikit.X_test_std));

y_combined = np.hstack((Perceptron_with_scikit.y_train, Perceptron_with_scikit.y_test));

Decision_boundary_visualization.plot_decision_regions(X=X_combined_std, y=y_combined,
                                                      classifier=Perceptron_with_scikit.ppn,
                                                      test_idx=range(105, 150));

plt.xlabel("petal length [standardized]");
plt.ylabel("petal width [standardized]");
plt.legend(loc="upper left");
plt.tight_layout();
plt.show();