from sklearn.metrics import accuracy_score
import Perceptron_with_scikit

print("Accuracy: %.3f" % accuracy_score(y_true=Perceptron_with_scikit.y_test,
                                        y_pred=Perceptron_with_scikit.y_prediction));

# Alternatively, each classifier in scikit-learn has a score method, which computes
# a classifier's prediction accuracy by combining the predict call with accuracy_score
# by combining the predict call with accuracy_score.
print("Accuracy: %.3f" % Perceptron_with_scikit.ppn.score(X=Perceptron_with_scikit.X_test_std,
                                                          y=Perceptron_with_scikit.y_test));