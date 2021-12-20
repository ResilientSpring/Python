import gym

environment = gym.make("FrozenLake-v1")

number_of_state = environment.observation_space.n

print(number_of_state)

number_of_action = environment.action_space.n
print(number_of_action)

environment.render()

# Take a right action
new_state, reward, is_done, info = environment.step(2)
print(new_state)
