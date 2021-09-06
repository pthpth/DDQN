import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from gym import Gym
import pyglet
from opengltest import GamerTab


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.n_actions = action_size
        self.lr = 0.005
        self.gamma = 0.99
        self.exploration_proba = 0.8
        self.exploration_proba_decay = 0.005
        self.batch_size = 4
        self.memory_buffer = list()
        self.max_memory_buffer = 2000
        self.model = Sequential([
            Dense(units=24, input_dim=state_size, activation='relu'),
            Dense(units=24, activation='relu'),
            Dense(units=action_size, activation='linear')
        ])
        self.model.compile(loss="mse",
                           optimizer=Adam(lr=self.lr))

    def compute_action(self, current_state):
        if np.random.uniform(0, 1) < self.exploration_proba:
            return np.random.choice(range(self.n_actions))
        q_values = self.model.predict(current_state)
        print("q_values", q_values)
        return np.argmax(q_values[0])

    def update_exploration_probability(self):
        self.exploration_proba = self.exploration_proba * np.exp(-self.exploration_proba_decay)

    def store_episode(self, current_state, action, reward, next_state, done):
        self.memory_buffer.append({
            "current_state": np.asarray(current_state).astype(np.float32),
            "action": action,
            "reward": reward,
            "next_state": np.asarray(next_state).astype(np.float32),
            "done": done
        })
        if len(self.memory_buffer) > self.max_memory_buffer:
            self.memory_buffer.pop(0)

    def train(self):
        np.random.shuffle(self.memory_buffer)
        batch_sample = self.memory_buffer[0:self.batch_size]
        for experience in batch_sample:
            q_current_state = self.model.predict(experience["current_state"])
            q_target = experience["reward"]
            if not experience["done"]:
                print("error", experience["next_state"].shape)
                q_target = q_target + self.gamma * np.max(self.model.predict(experience["next_state"])[0])
            q_current_state[0][experience["action"]] = q_target
            self.model.fit(experience["current_state"], q_current_state, verbose=0)


env = Gym()

state_size = 6
action_size = 4

n_episodes = 10000
runner = 0

agent = DQNAgent(state_size, action_size)

total_steps = 0

for e in range(n_episodes):

    current_state = env.input_generator()
    current_state = np.asarray([current_state]).astype(np.float32)
    total_steps = total_steps + 1
    runner += 1

    action = agent.compute_action(current_state)

    next_state, reward, done = env.step(action)

    next_state = np.array([next_state])

    agent.store_episode(current_state, action, reward, next_state, done)

    if done:
        env = Gym()
        next_state = env.input_generator()
        agent.update_exploration_probability()
    current_state = next_state

    if total_steps >= agent.batch_size:
        total_steps = 0
        agent.train()

    if runner % 100 == 0:
        runner = 0
        tester = GamerTab(agent.model, 400, 400, "hello")
        print("oi")
        pyglet.app.run()
