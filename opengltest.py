# importing pyglet module
import math

import pyglet
from pyglet import shapes
from stack import *


class GamerTab(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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


width = 1350

# height of window
height = 629

# caption i.e title of the window
title = "Geeks for geeks"

# creating a window
window = GamerTab(width, height, title)

# text
text = "Welcome to Geeks for Geeks"

# on draw event
# start running the application
pyglet.app.run()
window.update((0,600),45)