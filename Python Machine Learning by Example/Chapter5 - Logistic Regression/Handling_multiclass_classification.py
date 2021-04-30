from sklearn import datasets

digits = datasets.load_digits()

n_samples = len(digits.images)

# As the image data is stored in 8 x 8 matrices, we need to flatten them.
X = digits.images.reshape((n_samples, -1))

Y = digits.target