import gym
import matplotlib.pyplot as plt

environment = gym.make('CartPole-v1')

environment.seed(42)

observation = environment.reset()

print(observation) # cart's horizontal position, its velocity, the angle of the pole (0 = vertical), and the angular velocity.

image = environment.render(mode="rgb_array")
print(image.shape)

def plot_environment(environment, figsize=(5, 4)):
    plt.figure(figsize=figsize)
    image = environment.render(mode="rgb_array")
    plt.imshow(image)
    plt.axis("off")

    return image


plot_environment(environment)

plt.show()

print(environment.action_space)

print(observation[2])

action = 1 # accelerate right
observation, reward, done, info = environment.step(action)

print(observation, '\n', reward, '\n', done, '\n', info)

def basic_policy(observation):
    angle = observation[2]

    return 0 if angle < 0 else 1


totals = []

for episode in range(500):
    episode_rewards = 0
    observation = environment.reset()

    for step in range(200):
        action = basic_policy(observation)
        observation, reward, done, info = environment.step(action)
        episode_rewards += reward
