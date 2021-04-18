import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

url = "https://github.com/PacktPublishing/Machine-Learning-for-Finance/blob/master/1%20Excel%20Exercise.xlsx?raw=true";
df = pd.read_excel(io=url, sheet_name=0, header=1, index_col=None, usecols="A:N", nrows=180);
print(df);

print(df.columns);

# Feature set
X = df.drop(columns="Cultivar");
print(X);

# Class label
y = df.iloc[:, 0];
print(y);

# Divide dataset into two sets, i.e., a training set and a test set.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0,
                                                    stratify=y);

# Data Scaling/Normalization

## Initialize the Scaler
sc = StandardScaler();

## Scailing the training set
X_train = sc.fit_transform(X_train);

## Scailing the test set.
X_test = sc.transform(X_test);

sgd_lr = SGDClassifier(loss="log", penalty='l1', alpha=0.0001, fit_intercept=True,
                       max_iter=100, learning_rate='constant', eta0=0.01);

sgd_lr.fit(X=X_train, y=y_train);