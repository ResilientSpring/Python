import numpy as np
from sklearn.metrics import classification_report
import April19

target_name = ["setosa", "versicolor", "virginica"];

y_prediction = April19.model.predict(x=April19.X_test);
y_prediction_bool = np.argmax(y_prediction, axis=1);

print(classification_report(y_true=April19.y_test, y_pred=y_prediction_bool, target_names=target_name));
