import load_mnist as loader

X_train, y_train = loader.load_mnist('', kind="train")
print("Rows: {:d}, columns: {:d}".format(X_train.shape[0], X_train.shape[1]))