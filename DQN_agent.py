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
        # we define some parameters and hyperparameters:
        # "lr" : learning rate
        # "gamma": discounted factor
        # "exploration_proba_decay": decay of the exploration probability
        # "batch_size": size of experiences we sample to train the DNN
        self.lr = 0.001
        self.gamma = 0.99
        self.exploration_proba = 1.0
        self.exploration_proba_decay = 0.005
        self.batch_size = 2

        # We define our memory buffer where we will store our experiences
        # We stores only the 2000 last time steps
        self.memory_buffer = list()
        self.max_memory_buffer = 2000

        # We create our model having to hidden layers of 24 units (neurones)
        # The first layer has the same size as a state size
        # The last layer has the size of actions space
        self.model = Sequential([
            Dense(units=24, input_dim=state_size, activation='relu'),
            Dense(units=24, activation='relu'),
            Dense(units=action_size, activation='linear')
        ])
        self.model.compile(loss="mse",
                           optimizer=Adam(lr=self.lr))

    # The agent computes the action to perform given a state 
    def compute_action(self, current_state):
        # We sample a variable uniformly over [0,1]
        # if the variable is less than the exploration probability
        #     we choose an action randomly
        # else
        #     we forward the state through the DNN and choose the action 
        #     with the highest Q-value.
        if np.random.uniform(0, 1) < self.exploration_proba:
            # print("random")
            return np.random.choice(range(self.n_actions))
        q_values = self.model.predict(current_state)
        # print("highest")
        return np.argmax(q_values[0])

    # when an episode is finished, we update the exploration probability using 
    # epsilon greedy algorithm
    def update_exploration_probability(self):
        self.exploration_proba = self.exploration_proba * np.exp(-self.exploration_proba_decay)

    # At each time step, we store the corresponding experience
    def store_episode(self, current_state, action, reward, next_state, done):
        # We use a dictionary to store them
        self.memory_buffer.append({
            "current_state": np.asarray(current_state).astype(np.float32),
            "action": action,
            "reward": reward,
            "next_state": np.asarray(next_state).astype(np.float32),
            "done": done
        })
        # If the size of memory buffer exceeds its maximum, we remove the oldest experience
        if len(self.memory_buffer) > self.max_memory_buffer:
            self.memory_buffer.pop(0)

    # At the end of each episode, we train our model
    def train(self):
        # We shuffle the memory buffer and select a batch size of experiences
        np.random.shuffle(self.memory_buffer)
        batch_sample = self.memory_buffer[0:self.batch_size]

        # We iterate over the selected experiences
        for experience in batch_sample:
            # We compute the Q-values of S_t
            q_current_state = self.model.predict(experience["current_state"])
            # print("q",experience["current_state"])
            # We compute the Q-target using Bellman optimality equation
            q_target = experience["reward"]
            if not experience["done"]:
                q_target = q_target + self.gamma * np.max(self.model.predict(experience["next_state"])[0])
            q_current_state[0][experience["action"]] = q_target
            # train the model
            self.model.fit(experience["current_state"], q_current_state, verbose=0)


# We create our gym environment
env = Gym()
# We get the shape of a state and the actions space size
state_size = 5
action_size = 6
# Number of episodes to run
n_episodes = 1000
# We define our agent
agent = DQNAgent(state_size, action_size)
total_steps = 0

# We iterate over episodes
for e in range(n_episodes):
    # We initialize the first state and reshape it to fit
    #  with the input layer of the DNN
    env = Gym()
    current_state = env.input_generator()
    current_state = np.asarray([current_state]).astype(np.float32)
    total_steps = total_steps + 1
    # the agent computes the action to perform
    action = agent.compute_action(current_state)
    # print(action)
    # the environment runs the action and returns
    # the next state, a reward and whether the agent is done
    next_state, reward, done = env.step(action)
    next_state = np.array([next_state])

    # We store each experience in the memory buffer
    agent.store_episode(current_state, action, reward, next_state, done)

    # if the episode is ended, we leave the loop after
    # updating the exploration probability
    if done:
        agent.update_exploration_probability()
    current_state = next_state
    # if the have at least batch_size experiences in the memory buffer
    # than we train our model
    if total_steps >= agent.batch_size:
        total_steps = 0
        agent.train()
        print(e)
        tester = GamerTab(agent.model,1350,629,"hello")
        pyglet.app.run()
