import random
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import itertools
from movement import action_space, move


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0
        self.epsilon_decay = 0.9995
        self.learning_rate = 0.001
        self.model = self.build_model()

    def build_model(self):
        """Deep Q Network"""
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        """Save transition into memory."""
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        """Predict action based on greedy-epsilon."""
        # Explore
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        # Exploit
        act_values = self.model.predict(state)
        action = np.argmax(act_values[0])
        # print("Action:", action_space[action])
        # Move
        # move(action_space[action])
        return action  # returns action

    def replay(self, batch_size):
        """Experience replay through random sampling. Decay epsilon."""
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        """Load model."""
        self.model.load_weights(name)

    def save(self, name):
        """Save model."""
        self.model.save_weights(name)

