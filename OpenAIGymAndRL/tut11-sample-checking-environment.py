from stable_baselines3.common.env_checker import check_env
from tut10-sample-snake-env-converted-gym-env import SnekEnv


env = SnekEnv()
# It will check your custom environment and output additional warnings if needed
check_env(env)