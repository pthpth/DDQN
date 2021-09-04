# import math
# #
# # import numpy as np
# #
# #
# def dot(a, b):
#     return a[0] * b[0] + a[1] * b[1]
# def cross(a,b):
#     return a[0]*b[1]-a[1]*b[0]
#
# points1=[[-200,200],[200,200],[-200,200],[-200,-200],[-100,100],[100,100],[-100,100],[-100,-100]]
# points2=[[-200,-200],[200,-200],[200,200],[200,-200],[-100,-100],[100,-100],[100,100],[100,-100]]
# q=[50,50]
# # width=20
# # height=40
# def input_generator(q):
#     points1=[[-200,200],[200,200],[-200,200],[-200,-200],[-100,100],[100,100],[-100,100],[-100,-100]]
#     points2=[[-200,-200],[200,-200],[200,200],[200,-200],[-100,-100],[100,-100],[100,100],[100,-100]]
#     directions=[[math.cos(math.radians(180)),math.sin(math.radians(180))],[math.cos(math.radians(0)),math.sin(math.radians(0))],[math.cos(math.radians(-90)),math.sin(math.radians(-90))],[math.cos(math.radians(90)),math.sin(math.radians(90))],[math.cos(math.radians(135)),math.sin(math.radians(135))],[math.cos(math.radians(45)),math.sin(math.radians(45))]]
#     inputs=[]
#     for direction in directions:
#         final_l=[]
#         for p,d in zip(points1,points2):
#             r=[d[0]-p[0],d[1]-p[1]]
#             s=direction
#             c=[q[0]-p[0],q[1]-p[1]]
#             # print(r,c,s)
#             # print(cross(r,s),cross(c,r))
#             if(cross(r,s)==0 and cross(c,r)==0):
#                 final_l.append(math.sqrt(dot(c,c)))
#                 # t0=dot(c,r)/dot(r,r)
#                 # t1=t0+dot(s,r)/dot(r,r)
#                 # if(dot(s,r)<0):
#                 #     if 0<=t1<=t0<=1:
#                 #         final_l.append((True,1))
#                 #     else:
#                 #         final_l.append((False,1))
#                 # else:
#                 #     if 0<=t0<=t1<=1:
#                 #         final_l.append()
#                 #     # else:
#                 #     #     final_l.append((False,2))
#             elif(cross(r,s)==0 and cross(c,r)!=0):
#                 continue
#                 # final_l.append((False,3))
#             else:
#                 t=cross(c,s)/cross(r,s)
#                 u=cross(c,r)/cross(r,s)
#                 # print(t,u)
#                 if 0<=t<=1 and 0<u:
#                     final_l.append(u)
#                     # final_l.append((False,4))
#         inputs.append(min(final_l))
#     print(inputs)
# input_generator([-150,-150])
# # #     return inputs
# # def work(r,s,c):
# #     inputs=False
# #     if (cross(r, s) == 0 and cross(c, r) == 0):
# #         t0 = dot(c, r) / dot(r, r)
# #         t1 = t0 + dot(s, r) / dot(r, r)
# #         if (dot(s, r) < 0):
# #             if 0 <= t1 <= t0 <= 1:
# #                 inputs = inputs or True
# #             else:
# #                 inputs = inputs or False
# #         else:
# #             if 0 <= t0 <= t1 <= 1:
# #                 inputs = inputs or True
# #             else:
# #                 inputs = inputs or False
# #     elif cross(r, s) == 0 and cross(c, r) != 0:
# #         inputs = inputs or False
# #     else:
# #         t = cross(c, s) / cross(r, s)
# #         u = cross(c, r) / cross(r, s)
# #         if 0 < t < 1 and 0 < u:
# #             inputs = inputs or True
# #         else:
# #             inputs = inputs or False
# #     return inputs
# #
# #
# #
# # def reward(q,rot):
# #     points1 =[[200,200],[-200,200],[-200,-200],[200,-200],[-200,-100],[-200,100],[100,100],[100,100],[200,-100],[100,-100],[-100,-100],[-100,-50],[-100,0],[-100,50],[100,-50],[100,0],[100,50],[-50,100],[0,100],[50,100],[-50,-100],[0,-100],[50,-100]]
# #     points2=[[100,100],[-100,100],[-100,-100],[100,-100],[-100,-100],[-100,100],[100,200],[200,100],[100,-100],[100,-200],[-100,-200],[-200,-50],[-200,0],[-200,50],[200,-50],[200,0],[200,50],[-50,200],[0,200],[50,200],[-50,-200],[0,-200],[50,-200]]
# #     rotate=[[math.cos(rot),math.sin(rot)],[-math.sin(rot),math.cos(rot)]]
# #     points=[width/2,width/2,-width/2,-width/2],[height/2,-height/2,-height/2,height/2]
# #     points=np.array(rotate)@np.array(points)
# #     points=points.T+np.array(q)
# #     pair1=(points[0],points[1])
# #     pair2=(points[1],points[2])
# #     pair3=(points[2],points[3])
# #     pair4=(points[3],points[0])
# #     s0=points[1]-points[0]
# #     q0=points[0]
# #     s1 = points[2] - points[1]
# #     q1 = points[1]
# #     s2 = points[3] - points[2]
# #     q2 = points[2]
# #     s3 = points[0] - points[3]
# #     q3 = points[3]
# #     ans=False
# #     for p,d in zip(points1,points2):
# #         r=[d[0] - p[0], d[1] - p[1]]
# #         c0 = [q0[0] - p[0], q0[1] - p[1]]
# #         c1 = [q1[0] - p[0], q1[1] - p[1]]
# #         c2 = [q2[0] - p[0], q2[1] - p[1]]
# #         c3 = [q3[0] - p[0], q3[1] - p[1]]
# #         ans=ans or work(r,s0,c0) or work(r,s1,c1) or work(r,s2,c2) or work(r,s3,c3)
# #         if ans:
# #             return 1000
# #     return 0
import data
import math
import numpy as np
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]
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
        print(c,s)
        print(cross(c,s))
        u = cross(c, r) / cross(r, s)
        if 0 < t < 1 and 0 < u<1 :
            print(t,u)
            inputs = inputs or True
        else:
            inputs = inputs or False
    return inputs
width=20
height=20
def done(q,rot):
    points1 = data.points1
    points2 = data.points2
    rotate = [[math.cos(rot), math.sin(rot)], [-math.sin(rot), math.cos(rot)]]
    points = [width / 2, width / 2, -width / 2, -width / 2], [height / 2, -height / 2,
                                                                                  -height / 2, height / 2]
    points = np.array(rotate) @ np.array(points)
    points = points.T + np.array(q)
    pair1 = (points[0], points[1])
    pair2 = (points[1], points[2])
    pair3 = (points[2], points[3])
    pair4 = (points[3], points[0])
    s0 = points[1] - points[0]
    q0 = points[0]
    s1 = points[2] - points[1]
    q1 = points[1]
    print(points[2],points[1])
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
        print(r,s1,c1,p,d)
        ans = ans or work(r, s0, c0) or work(r, s1, c1) or work(r, s2, c2) or work(r, s3, c3)
        if ans:
            return ans
    return False

print(done([55,55],0))