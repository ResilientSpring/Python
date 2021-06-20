import numpy as np

np.random.seed(1)

# Layer1
w1 = np.random.rand(2, 2)
print(w1)

flat_w1 = np.reshape(w1, np.prod(w1.shape))
print(flat_w1)

print(30*'=')

bias1 = np.random.rand(1, 2)
print(bias1)

flat_b1 = np.reshape(bias1, np.prod(bias1.shape))
print(flat_b1)

# Layer2
w2 = np.random.rand(2, 1)
flat_w2 = np.reshape(w2, np.prod(w2.shape))
print(flat_w2)

bias2 = np.random.rand(1, 1)
flat_b2 = np.reshape(bias2, np.prod(bias2.shape))
print(flat_b2)

# Forming particle
particle_position = np.hstack([flat_w1, flat_b1, flat_w2, flat_b2])
print(particle_position)
