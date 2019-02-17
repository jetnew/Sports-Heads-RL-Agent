from dqn import DQNAgent
from get_window import get_frame
from movement import action_space, move
import time
from env import FootballHeadEnv
import itertools
from graph import EpisodeStats, plot_episode_stats
import numpy as np
import threading
import random
time.sleep(2)

# Define consts
STATE_SIZE = 200 * 200  # dims
ACTION_SIZE = 4
EPISODES = 1000
BATCH_SIZE = 32

# Define agent
agent1 = DQNAgent(STATE_SIZE, ACTION_SIZE)  # right
agent2 = DQNAgent(STATE_SIZE, ACTION_SIZE)  # left
agent1.load("spheads-dqn1.h5")
agent2.load("spheads-dqn2.h5")
done = False

# For graphing
stats = EpisodeStats(
    episode_lengths=np.zeros(EPISODES),
    episode_rewards=np.zeros(EPISODES))

# Start environment
env = FootballHeadEnv()
# Random agent
# while True:
#     move(action_space[random.randint(0,7)])

# Play
def play():
    state = env.reset()
    for t in itertools.count():
        action1 = agent1.act(state)
        # action1 = random.randint(0,3)  # random
        move(action_space[action1])

        action2 = agent2.act(state)
        action2 += 4
        move(action_space[action2])

        next_state, p1_reward, p2_reward, done, _ = env.step(state)
        state = next_state
# Train
def train():
    for e in range(EPISODES):
        print("Episode:", e)
        # Restart game
        state = env.reset()
        p1_total_reward = 0
        p2_total_reward = 0

        for t in itertools.count():
            # Play game
            # print("Agent act")
            action1 = agent1.act(state)
            move(action_space[action1])
            action2 = agent2.act(state) + 4
            # action2 = random.randint(4, 7)
            move(action_space[action2])

            # print("Env step")
            next_state, p1_reward, p2_reward, done, _ = env.step(state)
            p1_total_reward += p1_reward
            p2_total_reward += p2_reward

            # print("Agent remember")
            agent1.remember(state, action1, p1_reward, next_state, done)
            # agent2.remember(state, action2, p2_reward, next_state, done)
            state = next_state

            # print("Agent replay")
            # print("Timestep:", t)
            if len(agent1.memory) > BATCH_SIZE and t % 5 == 0:
                agent1.replay(BATCH_SIZE)
                # agent2.replay(BATCH_SIZE)

            # For graphing
            stats.episode_rewards[e] += p1_reward
            stats.episode_lengths[e] = t

            if done:
                print("Episode:", e,
                      "P1 total reward:", p1_total_reward,
                      "P2 total reward:", p2_total_reward,
                      "Time taken:", t,
                      "Agent 1's epsilon:", agent1.epsilon,
                      "Agent 2's epsilon:", agent2.epsilon)
                break

            if e % 10 == 0:
                agent1.save("spheads-dqn1.h5")
                agent2.save("spheads-dqn2.h5")

    plot_episode_stats(stats)

# play()
train()
