from pyglet.gl import *

# class Quad:
#     def __init__(self):
#         self.vertices = pyglet.graphics.vertex_list_indexed(20,
#                                                             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
#                                                              17, 18, 19],
#                                                             ("v3f",
#                                                              [
#                                                                  -1, 1, 0.0,
#                                                                  -0.7, 1, 0.0,
#                                                                  -0.7, 0.7, 0,
#                                                                  -1, 0.7, 0,
#                                                                  -0.2, 1, 0,
#                                                                  1, 1, 0,
#                                                                  1, 0.6, 0,
#                                                                  -0.2, 0.6, 0,
#                                                                  -0.5, 0.4, 0,
#                                                                  0.3, 0.4, 0,
#                                                                  0.3, -0.4, 0,
#                                                                  -0.5, -0.4, 0,
#                                                                  -1, 0, 0,
#                                                                  -0.7, 0, 0,
#                                                                  -0.7, -1, 0,
#                                                                  -1, -1, 0,
#                                                                  -0.1, -0.6, 0,
#                                                                  0.1, -0.6, 0,
#                                                                  0.1, -1, 0,
#                                                                  -0.1, -1, 0
#                                                              ]))

import pyglet
from pyglet import shapes

window = pyglet.window.Window(500, 500)
batch = pyglet.graphics.Batch()

lists = [(0, 0, 3, 9), (0, 9, 5, 11), (5, 12, 2, 2), (0, 20, 2, 3), (0, 23, 10, 2), (7, 9, 8, 11), (10, 6, 6, 3),
         (10, 4, 5, 1), (11, 2, 5, 1), (10, 0, 5, 1)]
listed = [shapes.Rectangle(x[0] / 25 * 500, x[1] / 25 * 500, x[2] / 25 * 500, x[3] / 25 * 500, batch=batch) for x in
          lists]


@window.event
def on_draw():
    window.clear()
    batch.draw()


pyglet.app.run()
# list=[(3.5,14.5,5,11)]
# class Player:
#     def __init__(self):
#         self.values = [
#             -0.975, 0.475, 0,
#             -0.925, 0.475, 0,
#             -0.925, 0.425, 0,
#             -0.975, 0.425, 0
#         ]
#         self.vertices = pyglet.graphics.vertex_list(4, ("v3f", self.values),
#                                                     ("c3f",
#                                                      [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0]))
#         self.shape = pyglet.shapes()
#
#
# class winning_area:
#     def __init__(self):
#         self.vertices = pyglet.graphics.vertex_list(4, ("v3f",
#                                                         [
#                                                             0.1, -0.8, 0,
#                                                             0.1, -1, 0,
#                                                             0.3, -1, 0,
#                                                             0.3, -0.8, 0
#                                                         ]),
#                                                     (
#                                                         "c3f",
#                                                         [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0])
#                                                     )
#
#
# class MyWindow(pyglet.window.Window):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.set_minimum_size(400, 300)
#         glClearColor(0.2, 0.3, 0.2, 1.0)
#         self.quad = Quad()
#         self.player = Player()
#         self.win = winning_area()
#
#     def on_draw(self):
#         self.clear()
#         # self.triangle.vertices.draw(GL_TRIANGLES)
#         self.quad.vertices.draw(GL_QUADS)
#         self.player.vertices.draw(GL_QUADS)
#         self.win.vertices.draw(GL_QUADS)
#
#     def on_resize(self, width, height):
#         glViewport(0, 0, width, height)
#
#
# if __name__ == "__main__":
#     wind = MyWindow(1280, 720, "hello")
#     pyglet.app.run()
