import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report

url = "https://raw.githubusercontent.com/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/waveform.data"

waveform_data = pd.read_csv(filepath_or_buffer=url, header=None)
print(waveform_data)

waveform_features = waveform_data.iloc[:, 0:21]
print(waveform_features)

waveform_labels = waveform_data.iloc[:, 21]
print(waveform_labels)

X_train, X_test, y_train, y_test = train_test_split(waveform_features, waveform_labels,
                                                    test_size=0.33, random_state=42)

tree_classifier = DecisionTreeClassifier(max_depth=5, random_state=1)
tree_classifier.fit(X=X_train, y=y_train)

y_prediction = tree_classifier.predict(X=X_test)

plt.figure(figsize=(40, 7.2), dpi=200)
tree.plot_tree(decision_tree=tree_classifier, rounded=True, filled=True, fontsize=12)

plt.savefig("Waveform_Decision_Tree")


