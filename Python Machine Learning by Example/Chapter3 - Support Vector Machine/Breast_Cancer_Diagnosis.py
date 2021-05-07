from sklearn.datasets import load_breast_cancer

cancer_data = load_breast_cancer()

X = cancer_data.data
Y = cancer_data.target

print('Input data size: ', X.shape)
print('Output data size: ', Y.shape)
