import numpy as np
import K_Hong as k

X = np.array([ [1, 1], [1, 0], [0, 1], [0, 0] ])
y = np.array([0, 1, 1, 0])

X_test = np.array([[0, 1], [1, 1], [0, 0], [1, 0]])

swarm = k.NeuralNetwork(layers=[2, 2, 1], activation="sigmoid")

swarm.fit(X=X, y=y)

y_prediction = swarm.predict(x=X_test)
print(y_prediction)
