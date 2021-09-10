import numpy as np

import gym
import highway_env
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.regularizers import l1, l2


class DDQNAgent:
    def __init__(self, state_size, action_size):
        self.n_actions = action_size
        self.lr = 0.005
        self.gamma = 0.75
        self.exp_proba = 0.8
        self.exp_proba_decay = 0.000
        self.memory_buffer = list()
        self.max_memory_buffer = 2000
        self.q_model = self.build_model(state_size, action_size)
        self.q_target_model = self.build_model(state_size, action_size)

    def build_model(self, state_size, action_size):
        model = Sequential([
            Dense(units=100, input_dim=state_size, activation='relu'),
            Dense(units=50, activation='relu', bias_regularizer=l2(0.01), kernel_regularizer=l2(0.01)),
            Dense(units=24, activation='relu'),
            Dense(units=action_size, activation='linear')
        ])
        # model=keras.models.load_model('model')
        model.compile(loss="mse", optimizer=Adam(lr=self.lr))
        return model

    def compute_action(self, current_state):
        if np.random.uniform(0, 1) < self.exp_proba:
            return np.random.choice(range(self.n_actions))
        q_values = self.q_model.predict(current_state)[0]
        return np.argmax(q_values)

    def store_episode(self, current_state, action, reward, next_state, done):
        self.memory_buffer.append({
            "current_state": current_state,
            "action": action,
            "reward": reward,
            "next_state": next_state,
            "done": done
        })
        if len(self.memory_buffer) > self.max_memory_buffer:
            self.memory_buffer.pop(0)

    def update_exploration_probability(self):
        self.exp_proba = self.exp_proba * np.exp(-self.exp_proba_decay)
        print(self.exp_proba)

    def train(self, batch_size):
        np.random.shuffle(self.memory_buffer)
        batch_sample = self.memory_buffer[0:batch_size]

        for experience in batch_sample:
            q_current_state = self.q_model.predict(experience["current_state"])
            q_target = experience["reward"]
            if not experience["done"]:
                q_target = q_target + self.gamma * np.max(self.q_target_model.predict(experience["next_state"])[0])
            q_current_state[0][experience["action"]] = q_target
            self.q_model.fit(experience["current_state"], q_current_state, verbose=0)

    def update_q_target_network(self):
        self.q_target_model.set_weights(self.q_model.get_weights())


config = {
    "observation": {
        "type": "Kinematics",
        "vehicles_count": 50,
        "features": ["presence", "x", "y", "vx", "vy", "cos_h", "sin_h"],
        "features_range": {
            "x": [-200, 200],
            "y": [-200, 200],
            "vx": [-10, 10],
            "vy": [-10, 10]
        },
        "normalize": True,
        "absolute": False,
        "order": "sorted"
    }
}
env = gym.make('highway-v0')
env.configure(config)

state_size = 350
action_size = 5
n_episodes = 500
max_iteration_ep = 1000
batch_size = 8
q_target_update_freq = 5
agent = DDQNAgent(state_size, action_size)
total_steps = 0
n_training = 0
for e in range(n_episodes):
    current_state = env.reset()
    current_state = np.reshape(current_state, (1, 350))
    rewards = 0
    if e > 350:
        agent.exploration_proba = 0
    for step in range(max_iteration_ep):
        env.render()
        total_steps = total_steps + 1
        action = agent.compute_action(current_state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, (1, 350))
        rewards = rewards + reward
        agent.store_episode(current_state, action, reward, next_state, done)

        if done:
            # agent.update_exploration_probability()
            print(agent.exp_proba)
            break
        current_state = next_state
    if e % 100 == 0:
        agent.q_model.save("model1")
    print("episode ", e + 1, " rewards: ", rewards)
    if total_steps >= batch_size:
        agent.train(batch_size=batch_size)
        n_training = n_training + 1
        if n_training % q_target_update_freq:
            agent.update_q_target_network()
agent.q_model.save("model1")
