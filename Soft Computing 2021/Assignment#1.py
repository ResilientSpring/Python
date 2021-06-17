import Particle_Swarm_Intelligence_Optimization as PSO
import numpy as np

swarm = PSO.NeuralNetwork(layers=[2, 2, 1], activation='sigmoid')

X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([0, 1, 1, 0])

swarm.fit(X=X, y=y, learning_rate=0.2, epochs=100000)

print("weights:", swarm.weights)

X_test = np.array([0.8, 0.7])

y_prediction = swarm.predict(X_test)

print("Prediction:", y_prediction)
