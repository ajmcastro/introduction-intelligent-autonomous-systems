import gymnasium as gym

# Create the environment
env = gym.make('LunarLander-v2')  # continuous: LunarLanderContinuous-v2

# required before you can step the environment
env.reset()

# sample action:
print("sample action:", env.action_space.sample())

# observation space shape:
print("observation space shape:", env.observation_space.shape)

# sample observation:
print("sample observation:", env.observation_space.sample())

env.close()
