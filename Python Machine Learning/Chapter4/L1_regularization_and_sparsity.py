from sklearn.linear_model import LogisticRegression
import wine_dataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

X, y = wine_dataset.df.iloc[:, 1:], wine_dataset.df.iloc[:, 0]
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0,
                                                    stratify=y)
# Providing the class label array y as an argument to stratify ensures that both training
# and test datasets have the same class proportions as the original dataset.

# Most machine learning and optimization algorithms behave much better if features are on the
# same scale.
mms = MinMaxScaler()

X_train_norm = mms.fit_transform(X=X_train)
X_test_norm = mms.fit_transform(X=X_test)

## Better scalor
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X=X_train)
X_test_std = stdsc.transform(X=X_test)


lr = LogisticRegression(penalty="l1", solver="liblinear", multi_class="ovr", C=1.0)
# Note that C = 1.0 is the default. You can increase or decrease it to make the regularization
# effect stronger or weaker, respectively.

lr.fit(X=X_train_std, y=y_train)
print("Training accuracy: ", lr.score(X=X_train_std, y=y_train))
print("Test accuracy: ", lr.score(X=X_test_std, y=y_test))

# We access the intercept terms via the lr.intercept_
print(lr.intercept_)

# We access the weight array via the lr.coef_ that contains one weight vector for each vector,
# where each weight is multiplied by the respective feature in the feature set to calculate
# the net input.
print(lr.coef_)

# In scikit-learn, the intercept_ corresponds to w0 and coef_ corresponds to Wj