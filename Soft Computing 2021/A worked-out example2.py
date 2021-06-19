import numpy as np

np.random.seed(1)

# A swarm with two particles
swarm = np.random.uniform(low=-5, high=5, size=[2, 9])

print(swarm)
print(swarm.shape)

# Position matrix X
X = swarm.copy()
print(X[0])

np.random.seed(12)

# Velocity corresponding to a particle
Velocity = np.random.uniform(low=-5, high=5, size=[2, 9])
print(Velocity)

def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


fitness = []
fitness[0] = np.dot(X[0], Velocity[0])
min_fitness0 = min(fitness[0])

fitness[1] = np.dot(X[1], Velocity[1])
min_fitness1 = min(fitness[1])

