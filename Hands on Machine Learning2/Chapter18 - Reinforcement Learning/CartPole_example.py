import gym

environment = gym.make('CartPole-v1')

environment.seed(42)

observation = environment.reset()

print(observation)
