import numpy as np

np.random.seed(1)

# A swarm with two particles
swarm = np.random.uniform(low=-5, high=5, size=[5, 2])

print(swarm)
print(swarm.shape)

# Time step
t = 0

c1 = c2 = 2

# Position matrix X
position = swarm.copy()
print(position[0])

pbest = position

np.random.seed(12)

# Velocity corresponding to a particle
v = np.random.uniform(low=-5, high=5, size=[5, 2])
print(v)

def objective_function(x):

    fitness = []
    gbest = [1, 2]

    for i in range(0, len(x), 1):
        y = (x[i][0] ** 2) + (x[i][1] ** 2)
        fitness.append(y)

    for j in range(0, len(fitness), 1):
        if min(fitness) == fitness[j]:
            gbest = [x[j, 0], x[j, 1]]

    return fitness, gbest


fitness, gbest = objective_function(x=position)

# Velocity update
v[t+1] = v[t] + c1 * np.random.uniform() * (pbest[t] - position[t]) + c2 * np.random.uniform() * \
         (gbest[t] - position[t])

# Position update
position[t+1] = position[t] + v[t]

