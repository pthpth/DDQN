from collison import *
from stack import *


def minDist(arr):
    mins = None
    for x in arr:
        if (mins is None) or (x is not None and mins > x):
            mins = x
    return mins


NAME_TRACK = "test.png"


def unitVector(x):
    return x / np.linalg.norm(x)


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
        top_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 + hgt / 2]]).ravel()
        bottom_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 - hgt / 2]]).ravel()
        top_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 + hgt / 2]]).ravel()
        bottom_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 - hgt / 2]]).ravel()
        dir1 = unitVector(bottom_right - top_right)
        dir1 = Point(dir1[0], dir1[1])
        dir2 = unitVector(bottom_left - bottom_right)
        dir2 = Point(dir2[0], dir2[1])
        dir3 = unitVector(top_left - bottom_left)
        dir3 = Point(dir3[0], dir3[1])
        dir4 = unitVector(top_right - top_left)
        dir4 = Point(dir4[0], dir4[1])
        top_right = Point(top_right[0], top_right[1])
        bottom_left = Point(bottom_left[0], bottom_left[1])
        bottom_right = Point(bottom_right[0], bottom_right[1])
        top_left = Point(top_left[0], top_left[1])
        tracks = self.tracks
        for x in tracks:
            if (pointOfIntersection(top_right, dir1, x[0], x[1]) < hgt or
                    pointOfIntersection(bottom_right, dir2, x[0], x[1]) < wid or
                    pointOfIntersection(bottom_left, dir3, x[0], x[1]) < hgt or
                    pointOfIntersection(top_left, dir4, x[0], x[1]) < wid):
                return True
            else:
                return False

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

    def reward(self):
        DIR = self.MAIN_DIR
        x0 = self.X
        y0 = self.Y
        wid = self.width
        hgt = self.height
        ROT_MAT = np.array([
            [math.cos(DIR), -math.sin(DIR)],
            [math.sin(DIR), math.cos(DIR)]
        ])
        top_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 + hgt / 2]]).ravel()
        bottom_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 - hgt / 2]]).ravel()
        top_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 + hgt / 2]]).ravel()
        bottom_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 - hgt / 2]]).ravel()
        dir1 = unitVector(bottom_right - top_right)
        dir1 = Point(dir1[0], dir1[1])
        dir2 = unitVector(bottom_left - bottom_right)
        dir2 = Point(dir2[0], dir2[1])
        dir3 = unitVector(top_left - bottom_left)
        dir3 = Point(dir3[0], dir3[1])
        dir4 = unitVector(top_right - top_left)
        dir4 = Point(dir4[0], dir4[1])
        top_right = Point(top_right[0], top_right[1])
        bottom_left = Point(bottom_left[0], bottom_left[1])
        bottom_right = Point(bottom_right[0], bottom_right[1])
        top_left = Point(top_left[0], top_left[1])
        tracks = self.rewards
        for x in tracks:
            if (pointOfIntersection(top_right, dir1, x[0], x[1]) < hgt or
                    pointOfIntersection(bottom_right, dir2, x[0], x[1]) < wid or
                    pointOfIntersection(bottom_left, dir3, x[0], x[1]) < hgt or
                    pointOfIntersection(top_left, dir4, x[0], x[1]) < wid):
                return 1000
            else:
                return 0