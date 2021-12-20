import gym

environment = gym.make("CartPole-v1")

observation = environment.reset()

print(observation)

environment.render()

print(environment.action_space)
