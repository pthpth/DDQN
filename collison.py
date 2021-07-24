import math


# Point class to store two integers
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# function to calculate dot product of 2 vectors
def dot(a, b):
    return a.x * b.x + a.y * b.y


# function to calculate cross product
def cross(a, b):
    return a.x * b.y - a.y * b.x


# made using https://stackoverflow.com/a/565282
def pointOfIntersection(origin, direction, point1, point2):
    v1 = Point(origin.x - point1.x, origin.y - point1.y)
    v2 = Point(point2.x - point1.x, point2.y - point1.y)
    v3 = Point(-direction.y, direction.x)

    dot_product = dot(v2, v3)
    if abs(dot_product) < 0.000001:
        return None
    t1 = cross(v2, v1) / dot_product
    t2 = dot(v1, v3) / dot_product

    if t1 > 0 and (0 <= t2 <= 1):
        return t1
