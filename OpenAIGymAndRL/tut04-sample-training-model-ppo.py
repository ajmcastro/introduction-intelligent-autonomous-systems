import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make('LunarLander-v2', render_mode="human")  # continuous: LunarLanderContinuous-v2
env.reset()

model = PPO('MlpPolicy', env, verbose=1)
# model = A2C('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=1000)

episodes = 10

for ep in range(episodes):
    obs, info = env.reset()
    done = False
    while not done:
        # pass observation to model to get predicted action
        action, _states = model.predict(obs)

        # pass action to env and get info back
        obs, rewards, trunc, done, info = env.step(action)

        # show the environment on the screen
        env.render()
        print(ep, rewards, done)
        print("---------------")
