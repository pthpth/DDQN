import numpy as np
import math

import data


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def unitVector(x):
    return x / np.linalg.norm(x)


def work(r, s, c):
    inputs = False
    if cross(r, s) == 0 and cross(c, r) == 0:
        t0 = dot(c, r) / dot(r, r)
        t1 = t0 + dot(s, r) / dot(r, r)
        if dot(s, r) < 0:
            if 0 <= t1 <= t0 <= 1:
                inputs = inputs or True
            else:
                inputs = inputs or False
        else:
            if 0 <= t0 <= t1 <= 1:
                inputs = inputs or True
            else:
                inputs = inputs or False
    elif cross(r, s) == 0 and cross(c, r) != 0:
        inputs = inputs or False
    else:
        t = cross(c, s) / cross(r, s)
        u = cross(c, r) / cross(r, s)
        if 0 <= t <= 1 and 0 <= u <= 1:
            inputs = inputs or True
        else:
            inputs = inputs or False
    return inputs


# gym class to make the gym environment for Q-learning
class Gym:
    def __init__(self):
        self.speedx = 0
        self.speedy = 0
        self.MAIN_DIR = 0
        self.dir_v = 0
        self.X = 50
        self.points1 = [[0, 400], [400, 400], [00, 400], [00, 00], [100, 300], [300, 300], [100, 300],
                        [100, 100]]
        self.points2 = [[00, 00], [400, 00], [400, 400], [400, 00], [100, 100], [300, 100], [300, 300],
                        [300, 100]]
        self.rpoints1 = [[400, 400], [00, 400], [00, 00], [400, 00], [00, 100], [00, 300], [300, 300],
                         [300, 300], [400, 100], [300, 100], [100, 100], [100, 150], [100, 150], [100, 250],
                         [300, 150],
                         [300, 200], [300, 250], [150, 300], [200, 300], [250, 300], [150, 100], [200, 100], [250, 100]]
        self.rpoints2 = [[300, 300], [100, 300], [100, 100], [300, 100], [100, 100], [100, 300], [300, 400],
                         [400, 300], [300, 100], [300, 00], [100, 00], [00, 150], [00, 200], [00, 250],
                         [400, 150],
                         [400, 200], [400, 250], [150, 400], [200, 400], [250, 400], [150, 00], [200, 00], [250, 00]]
        self.width = 20
        self.height = 10
        self.Y = 50

    def input_generator(self):
        q = [self.X, self.Y]
        points1 = self.points1
        points2 = self.points2
        directions = [[math.cos(math.radians(180 + self.dir_v)), math.sin(math.radians(180 + self.dir_v))],
                      [math.cos(math.radians(0 + self.dir_v)), math.sin(math.radians(0 + self.dir_v))],
                      [math.cos(math.radians(-90 + self.dir_v)), math.sin(math.radians(-90 + self.dir_v))],
                      [math.cos(math.radians(90 + self.dir_v)), math.sin(math.radians(90 + self.dir_v))],
                      [math.cos(math.radians(135 + self.dir_v)), math.sin(math.radians(135 + self.dir_v))],
                      [math.cos(math.radians(45 + self.dir_v)), math.sin(math.radians(45 + self.dir_v))]]
        inputs = []
        for direction in directions:
            final_l = []
            for p, d in zip(points1, points2):
                r = [d[0] - p[0], d[1] - p[1]]
                s = direction
                c = [q[0] - p[0], q[1] - p[1]]
                if cross(r, s) == 0 and cross(c, r) == 0:
                    final_l.append(math.sqrt(dot(c, c)))

                elif cross(r, s) == 0 and cross(c, r) != 0:
                    continue
                else:
                    t = cross(c, s) / cross(r, s)
                    u = cross(c, r) / cross(r, s)
                    if 0 <= t <= 1 and 0 <= u:
                        final_l.append(u)
            if len(final_l) == 0:
                inputs.append(0)
            else:
                inputs.append(min(final_l))

        inputs=np.squeeze(np.array(inputs))
        print(inputs)
        return inputs

    def done(self):
        if self.X <= 0:
            return True
        if self.Y <= 0:
            return True
        if self.X >= 400:
            return True
        if self.Y >= 400:
            return True
        q = [self.X, self.Y]
        rot = self.MAIN_DIR
        points1 = self.points1
        points2 = self.points2
        rotate = [[math.cos(rot), math.sin(rot)], [-math.sin(rot), math.cos(rot)]]
        points = [self.width / 2, self.width / 2, -self.width / 2, -self.width / 2], [self.height / 2, -self.height / 2,
                                                                                      -self.height / 2, self.height / 2]
        points = np.array(rotate) @ np.array(points)
        points = points.T + np.array(q).T
        pair1 = (points[0], points[1])
        pair2 = (points[1], points[2])
        pair3 = (points[2], points[3])
        pair4 = (points[3], points[0])
        s0 = points[1] - points[0]
        q0 = points[0]
        s1 = points[2] - points[1]
        q1 = points[1]
        s2 = points[3] - points[2]
        q2 = points[2]
        s3 = points[0] - points[3]
        q3 = points[3]
        ans = False
        for p, d in zip(points1, points2):
            r = [d[0] - p[0], d[1] - p[1]]
            c0 = [q0[0] - p[0], q0[1] - p[1]]
            c1 = [q1[0] - p[0], q1[1] - p[1]]
            c2 = [q2[0] - p[0], q2[1] - p[1]]
            c3 = [q3[0] - p[0], q3[1] - p[1]]
            ans = ans or work(r, s0, c0) or work(r, s1, c1) or work(r, s2, c2) or work(r, s3, c3)
            if ans:
                return ans
        return False

    def step(self, step_number):
        # print(step_number)
        if step_number == 0:
            self.speedx += 0.05 * math.cos(self.MAIN_DIR)
            self.speedy += 0.05 * math.sin(self.MAIN_DIR)
        elif step_number == 1:
            self.speedx -= 0.05 * math.cos(self.MAIN_DIR)
            self.speedy -= 0.05 * math.sin(self.MAIN_DIR)
        elif step_number == 2:
            self.MAIN_DIR += math.pi / 36
            rot=[[math.cos(math.pi/36), math.sin(math.pi/36)], [-math.sin(math.pi/36), math.cos(math.pi/36)]]
            self.speedx, self.speedy = rot @ np.array([[self.speedx], [self.speedy]])

        elif step_number == 3:
            self.MAIN_DIR -= math.pi / 36
            rot = np.array(
                [[math.cos(math.pi / 36), math.sin(math.pi / 36)], [-math.sin(math.pi / 36), math.cos(math.pi / 36)]])
            self.speedx, self.speedy = rot @ np.array([[self.speedx], [self.speedy]])
        self.X = self.X + self.speedx * 0.01
        self.Y = self.Y + self.speedy * 0.01
        self.dir_v = math.atan2(self.speedy, self.speedx)
        return self.input_generator(), self.reward(), self.done()


    def reward(self):
        q = [self.X, self.Y]
        rot = self.MAIN_DIR
        points1 = self.rpoints1
        points2 = self.rpoints2
        normals = data.normals
        rotate = [[math.cos(rot), math.sin(rot)], [-math.sin(rot), math.cos(rot)]]
        points = [self.width / 2, self.width / 2, -self.width / 2, -self.width / 2], [self.height / 2, -self.height / 2,
                                                                                      -self.height / 2, self.height / 2]
        points = np.array(rotate) @ np.array(points)
        points = points.T + np.array(q).T
        pair1 = (points[0], points[1])
        pair2 = (points[1], points[2])
        pair3 = (points[2], points[3])
        pair4 = (points[3], points[0])
        s0 = points[1] - points[0]
        q0 = points[0]
        s1 = points[2] - points[1]
        q1 = points[1]
        s2 = points[3] - points[2]
        q2 = points[2]
        s3 = points[0] - points[3]
        q3 = points[3]
        ans = False
        for p, d, x in zip(points1, points2, normals):
            r = [d[0] - p[0], d[1] - p[1]]
            c0 = [q0[0] - p[0], q0[1] - p[1]]
            c1 = [q1[0] - p[0], q1[1] - p[1]]
            c2 = [q2[0] - p[0], q2[1] - p[1]]
            c3 = [q3[0] - p[0], q3[1] - p[1]]
            ans = ans or work(r, s0, c0) or work(r, s1, c1) or work(r, s2, c2) or work(r, s3, c3)
            if ans:
                return dot(x, [self.speedx, self.speedy]) * 1000
        return 0
