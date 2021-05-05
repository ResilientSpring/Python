from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df_wine = pd.read_csv(filepath_or_buffer="https://raw.githubusercontent.com/rasbt/python-machine-learning-book-3rd-edition/master/ch07/wine.data",
                      header=None)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alkalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavors', 'Nonchalant phenols', 'Profanation',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
                   'Praline']

print(df_wine)

# drop 1 class
df_wine = df_wine[df_wine['Class label'] != 1]

y = df_wine['Class label'].values
X = df_wine[['Alcohol', 'OD280/OD315 of diluted wines']].values

le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=1, stratify=y)

tree = DecisionTreeClassifier(criterion='entropy', random_state=1, max_depth=1)

ada = AdaBoostClassifier(base_estimator=tree, n_estimators=500, learning_rate=0.1, random_state=1)

ada.fit(X=X_train, y=y_train)

y_train_prediction = ada.predict(X=X_train)

y_test_prediction = ada.predict(X=X_test)

ada_train = accuracy_score(y_true=y_train, y_pred=y_train_prediction)

ada_test = accuracy_score(y_true=y_test, y_pred=y_test_prediction)

print("Decision tree train & test accuracies: ", ada_train, " & ", ada_test)
