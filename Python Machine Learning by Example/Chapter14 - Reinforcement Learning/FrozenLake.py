import gym

environment = gym.make("FrozenLake-v1")

number_of_state = environment.observation_space.n

print(number_of_state)

number_of_action = environment.action_space.n
print(number_of_action)

environment.reset()

environment.render()

# Take a right action
new_state, reward, is_done, info = environment.step(2)
environment.render()

print(new_state)
print(reward)
print(is_done)
print(info)

def run_episode(environment, policy):
    state = environment.reset()
    total_reward = 0
    is_done = False

    while not is_done:
        action = policy[state].item()
        state, reward, is_done, info = environment.step(action)
        total_reward += reward
        if is_done:
            break
    return total_reward
