from dqn import DQNAgent
from get_window import get_frame
from movement import action_space, move
import time
time.sleep(2)

# Define consts
state_size = 200*200  # dims
action_size = 4

# Define agent
agent = DQNAgent(state_size, action_size)
done = False

# Start environment

state = get_frame()
action = agent.act(state)

move(action_space[action])
