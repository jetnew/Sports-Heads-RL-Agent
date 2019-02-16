from dqn import DQNAgent
from get_window import get_frame
from movement import action_space, move
import time
from env import FootballHeadEnv
import itertools
from graph import EpisodeStats, plot_episode_stats
import numpy as np
import random
time.sleep(2)

# Define consts
STATE_SIZE = 200 * 200  # dims
ACTION_SIZE = 4
EPISODES = 10
BATCH_SIZE = 32

# Define agent
agent = DQNAgent(STATE_SIZE, ACTION_SIZE)
done = False

# For graphing
stats = EpisodeStats(
    episode_lengths=np.zeros(EPISODES),
    episode_rewards=np.zeros(EPISODES))

# Start environment
env = FootballHeadEnv()
# # Random agent
# while True:
#     move(action_space[random.randint(0,3)])

# state = env.reset()

for e in range(EPISODES):
    # Restart game
    state = env.reset()
    total_reward = 0

    for t in itertools.count():
        # Play game
        print("Agent act")
        action = agent.act(state)
        move(action_space[action])
        print("Env step")
        next_state, reward, done, _ = env.step(state)

        print("Agent remember")
        agent.remember(state, action, reward, next_state, done)
        state = next_state

        print("Agent replay")
        if len(agent.memory) > BATCH_SIZE:
            agent.replay(BATCH_SIZE)

        # For graphing
        stats.episode_rewards[e] += reward
        stats.episode_lengths[e] = t

        if done:
            print("Episode:", e,
                  "Total reward:", total_reward,
                  "Time taken:", t)
            break

plot_episode_stats(stats)
