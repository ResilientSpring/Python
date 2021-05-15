from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import numpy as np

dataset = load_wine(as_frame=True)

print(dataset)

dataset2 = load_wine(return_X_y=True, as_frame=True)
print(dataset2)

