from sklearn.datasets import load_wine

wine_data = load_wine()
X = wine_data.data
y = wine_data.target
print("Input size: ", X.shape)
