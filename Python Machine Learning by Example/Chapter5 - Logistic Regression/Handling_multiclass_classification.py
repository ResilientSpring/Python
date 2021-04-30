from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)

# As the image data is stored in 8 x 8 matrices, we need to flatten them.
X = digits.images.reshape((n_samples, -1))

Y = digits.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)