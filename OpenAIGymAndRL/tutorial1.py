import gymnasium as gym

env = gym.make('LunarLander-v2', render_mode="human")  # continuous: LunarLanderContinuous-v2
env.reset()

for step in range(200):
    env.render()
    # take random action
    env.step(env.action_space.sample())

env.close()
