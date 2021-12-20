import gym

env = gym.make("FrozenLake-v1")

n_state = env.observation_space.n
print(n_state)
n_action = env.action_space.n
print(n_action)


env.reset()

env.render()

# Source: https://github.com/PacktPublishing/Python-Machine-Learning-By-Example-Third-Edition/blob/master/chapter14/simulate_frozenlake.py

new_state, reward, is_done, info = env.step(2)
env.render()
print(new_state)
print(reward)
print(is_done)
print(info)