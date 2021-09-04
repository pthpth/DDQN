# importing pyglet module
import math
import gym
import pyglet
from pyglet import shapes
import data
import numpy as np
from stack import *


class GamerTab(pyglet.window.Window):
    def __init__(self, bren, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bren = bren
        pyglet.clock.schedule_interval(self.update, 1 / 24.0)
        self.env = gym.Gym()
        self.set_vsync(True)
        self.current_state = self.env.input_generator()
        self.current_state = np.asarray([self.current_state]).astype('float32')
        self.batch = pyglet.graphics.Batch()
        self.cars = pyglet.graphics.Batch()
        self.lines = list(zip(data.points1, data.points2))
        self.reward = list(zip(data.rpoints1, data.rpoints2))
        self.car = shapes.Rectangle(50, 50, height=10, width=20, batch=self.cars)
        self.d_lines = [
            shapes.Line(x[0][0], x[0][1], x[1][0], x[1][1], 2, color=(50, 225, 30), batch=self.batch)
            for
            x in
            self.lines]
        self.r_lines = [
            shapes.Line(x[0][0], x[0][1], x[1][0], x[1][1], 2, color=(255, 225, 30), batch=self.batch) for
            x
            in
            self.reward]

    def on_draw(self):
        # clear the window
        self.clear()
        # draw the label
        self.batch.draw()
        self.cars.draw()

    def update(self, dt):
        q_values = self.bren.predict(self.current_state)[0]
        action = np.argmax(q_values)
        print("TABstate", self.current_state)
        print("TABq", q_values)
        self.current_state, reward, done = self.env.step(action)
        if done:
            print("DONE")
            # print(self.env.X,self.env.Y,self.env.MAIN_DIR)
            self.close()
        self.current_state = np.asarray([self.current_state]).astype('float32')
        self.car.rotation = self.env.MAIN_DIR * 180 / math.pi
        self.car.position = (self.env.X, self.env.Y)
