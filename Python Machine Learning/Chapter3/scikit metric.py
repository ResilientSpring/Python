from sklearn.metrics import accuracy_score
import Perceptron_with_scikit

print("Accuracy: %.3f" % accuracy_score(y_true=Perceptron_with_scikit.y_test,
                                        y_pred=Perceptron_with_scikit.y_prediction));