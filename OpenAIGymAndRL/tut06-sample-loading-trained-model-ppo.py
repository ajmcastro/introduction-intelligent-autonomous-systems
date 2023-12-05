import gymnasium as gym
from stable_baselines3 import PPO

models_dir = "models/PPO"

env = gym.make('LunarLander-v2', render_mode="human")  # continuous: LunarLanderContinuous-v2
env.reset()

model_path = f"{models_dir}/10000.zip"
model = PPO.load(model_path, env=env)

episodes = 5

for ep in range(episodes):
    obs, info = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, rewards, trunc, done, info = env.step(action)
        env.render()
        print(ep, rewards, done)
        print("---------------")
