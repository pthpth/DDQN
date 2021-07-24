from collison import *
from stack import *


def minDist(arr):
    mins = None
    for x in arr:
        if (mins is None) or (x is not None and mins > x):
            mins = x
    return mins


NAME_TRACK = "test.png"


# gym class to make the gym environment for Q-learning
class Gym:
    def __init__(self, dirt, x, y):
        self.MAIN_DIR = dirt
        self.X = x
        self.tracks = track_maker(NAME_TRACK)
        self.rewards = reward_lines(NAME_TRACK)
        self.width = 10
        self.height = 10
        self.Y = y
        self.track_points = [[Point(x[0], x[1]), Point(x[2], x[3])] for x in self.tracks]

    def input_generator(self):
        inputs = []
        origin = Point(self.X, self.Y)
        tracks = self.track_points
        dirs = [math.pi / 4, -math.pi / 4, math.pi, 0, math.pi / 2]
        dirs = [Point(math.cos(x + self.MAIN_DIR), math.sin(x + self.MAIN_DIR)) for x in dirs]
        for dir in dirs:
            dist = [pointOfIntersection(origin, dir, track[0], track[1]) for track in tracks]
            inputs.append(minDist(dist))
        return inputs

    def done(self):
        DIR = self.MAIN_DIR
        x0 = self.X
        y0 = self.Y
        wid = self.width
        hgt = self.height
        ROT_MAT = np.array([
            [math.cos(DIR), -math.sin(DIR)],
            [math.sin(DIR), math.cos(DIR)]
        ])
        top_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 + hgt / 2]])
        bottom_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 - hgt / 2]])
        top_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 + hgt / 2]])
        bottom_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 - hgt / 2]])
        dir1 = bottom_right - top_right
        dir2 = bottom_left - bottom_right
        dir3 = top_left - bottom_left
        dir4 = top_right - top_left
        print(dir1,dir2,dir3,dir4)
        pass

    def step(self, step_number):
        if step_number == 0:
            self.X += 0.005
        elif step_number == 1:
            self.Y += 0.005
        elif step_number == 2:
            self.X -= 0.005
        elif step_number == 3:
            self.Y -= 0.005
        elif step_number == 4:
            self.MAIN_DIR += 0.0001
        elif step_number == 5:
            self.MAIN_DIR -= 0.0001
        # return self.input_generator(), reward(), self.done()
