import math

import numpy as np
def unitVector(x):
    return x/np.linalg.norm(x)
DIR = math.pi/4
x0 = 0
y0 = 0
wid = 10
hgt = 10
ROT_MAT = np.array([
    [math.cos(DIR), -math.sin(DIR)],
    [math.sin(DIR), math.cos(DIR)]
])
top_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 + hgt / 2]])
bottom_right = ROT_MAT @ np.array([[x0 + wid / 2], [y0 - hgt / 2]])
top_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 + hgt / 2]])
bottom_left = ROT_MAT @ np.array([[x0 - wid / 2], [y0 - hgt / 2]])
dir1 = unitVector(bottom_right - top_right).ravel()
dir2 = unitVector(bottom_left - bottom_right).ravel()
dir3 = unitVector(top_left - bottom_left).ravel()
dir4 = unitVector(top_right-top_left).ravel()
print(top_right," ",bottom_right," ",bottom_left," ",top_left)
print(dir1,"\n",dir2,"\n", dir3,"\n", dir4)

