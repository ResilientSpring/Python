import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

url = "https://raw.githubusercontent.com/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/waveform.data"

# Load dataset
waveform_data = pd.read_csv(filepath_or_buffer=url, header=None)
print(waveform_data)

# Feature set
waveform_feature = waveform_data.iloc[:, 0:21]
print(waveform_feature)

# Label set
waveform_label = waveform_data.iloc[:, 21]
print(waveform_label)

X_train, X_test, y_train, y_test = train_test_split(waveform_feature, waveform_label,
                                                    test_size=0.33, random_state=42)

support_vector_machine = SVC(C=5.0)
support_vector_machine.fit(X=X_train, y=y_train)

y_prediction = support_vector_machine.predict(X=X_test)

print(classification_report(y_true=y_test, y_pred=y_prediction))
