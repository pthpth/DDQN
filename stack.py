# import numpy as np
# import cv2 as cv
# from collison import Point
#
#
# # def track_maker(name):
# #     img = cv.imread(name)
# #     hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# #     lower_red = np.array([80, 255, 255])
# #     upper_red = np.array([100, 255, 255])
# #     mask = cv.inRange(hsv, lower_red, upper_red)
# #     res = cv.bitwise_and(img, img, mask=mask)
# #     gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# #     lines = cv.HoughLinesP(gray, 1, np.pi / 360, 100, minLineLength=0, maxLineGap=10)
# #     lines2 = []
# #     lines3 = []
# #     for line in lines:
# #         x1, y1, x2, y2 = line[0]
# #         lines2.append([Point(x1, 629-y1), Point(x2, 629-y2)])
# #         lines3.append([(x1, 629-y1), (x2, 629-y2)])
# #         cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #         cv.imwrite('track.jpg', img)
# #     return (lines2, lines3)
# #
# #
# # def reward_lines(name):
# #     img = cv.imread(name)
# #     hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# #     lower_red = np.array([140, 255, 255])
# #     upper_red = np.array([160, 255, 255])
# #     mask = cv.inRange(hsv, lower_red, upper_red)
# #     res = cv.bitwise_and(img, img, mask=mask)
# #     gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
# #     lines = cv.HoughLinesP(gray, 1, np.pi / 360, 100, minLineLength=0, maxLineGap=10)
# #     lines2 = []
# #     lines3 = []
# #     for line in lines:
# #         x1, y1, x2, y2 = line[0]
# #         lines2.append([Point(x1, 629-y1), Point(x2, 629-y2)])
# #         lines3.append([(x1, 629-y1), (x2, 629-y2)])
# #         cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
# #         cv.imwrite('reward.jpg', img)
# #     return (lines2, lines3)
# points1 = [[-200, 200], [200, 200], [-200, 200], [-200, -200], [-100, 100], [100, 100], [-100, 100], [-100, -100]]
# points2 = [[-200, -200], [200, -200], [200, 200], [200, -200], [-100, -100], [100, -100], [100, 100], [100, -100]]
#
#
# def track_maker(name):
#     lines2=[]
#     lines3=[]
#     for p1,p2 in zip(points1,points2):
