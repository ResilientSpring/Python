
import gym
import torch


env = gym.make("FrozenLake-v0")

n_state = env.observation_space.n
print(n_state)
n_action = env.action_space.n
print(n_action)


env.reset()

env.render()

new_state, reward, is_done, info = env.step(2)
env.render()
print(new_state)
print(reward)
print(is_done)
print(info)