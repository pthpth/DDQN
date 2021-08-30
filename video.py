from abc import ABC

import pyglet
from stack import track_maker, reward_lines
from pyglet import shapes, window,clock
from gym import Gym
import numpy as np
import math


# # Function to check the progress of the trained neural network at certain intervals, n_episodes is number of trials
# and agent is the trained neural network
class GamerTab(pyglet.window.Window):
    def __init__(self, env, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.env = Gym()
        self.batch = pyglet.graphics.Batch()
        self.cars = pyglet.graphics.Batch()
        self.lines = track_maker("test.png")[1]
        self.reward = reward_lines("test.png")[1]
        self.car = shapes.Rectangle(0, 600, height=10, width=10, batch=self.cars)
        self.d_lines = [
            shapes.Line(x[0][0], 629 - x[0][1], x[1][0], 629 - x[1][1], 2, color=(50, 225, 30), batch=self.batch)
            for
            x in
            self.lines]
        self.r_lines = [
            shapes.Line(x[0][0], 629 - x[0][1], x[1][0], 629 - x[1][1], 2, color=(255, 225, 30), batch=self.batch) for
            x
            in
            self.reward]


    def on_draw(self):
        # clear the window
        window.clear()
        # draw the label
        self.batch.draw()
        self.cars.draw()

    def update(self, pos, rot):
        self.car.rotation = rot
        self.car.position = pos

    def bren(self, agent):
        self.update((0,10),45)
        # current_state = self.env.input_generator()
        # current_state = np.asarray([current_state]).astype(np.float32)
        # action = agent.compute_action(current_state)
        # next_state, reward, done = self.env.step(action)
        # next_state = np.array([next_state])
        # current_state = next_state
        # self.update((self.env.X, self.env.Y), self.env.MAIN_DIR)

