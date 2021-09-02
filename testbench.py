import math
def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]
def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

# points1=[[-200,200],[200,200],[-200,200],[-200,-200],[-100,100],[100,100],[-100,100],[-100,-100]]
# points2=[[-200,-200],[200,-200],[200,200],[200,-200],[-100,-100],[100,-100],[100,100],[100,-100]]
# q=[-100,-140]
def input_generator(q):
    points1=[[-200,200],[200,200],[-200,200],[-200,-200],[-100,100],[100,100],[-100,100],[-100,-100]]
    points2=[[-200,-200],[200,-200],[200,200],[200,-200],[-100,-100],[100,-100],[100,100],[100,-100]]
    directions=[[math.cos(math.radians(180)),math.sin(math.radians(180))],[math.cos(math.radians(0)),math.sin(math.radians(0))],[math.cos(math.radians(-90)),math.sin(math.radians(-90))],[math.cos(math.radians(90)),math.sin(math.radians(90))],[math.cos(math.radians(135)),math.sin(math.radians(135))],[math.cos(math.radians(45)),math.sin(math.radians(45))]]
    inputs=[]
    for direction in directions:
        final_l=[]
        for p,d in zip(points1,points2):
            r=[d[0]-p[0],d[1]-p[1]]
            s=direction
            c=[q[0]-p[0],q[1]-p[1]]
            if(cross(r,s)==0 and cross(c,r)==0):
                final_l.append(math.sqrt(dot(c,c)))
                # t0=dot(c,r)/dot(r,r)
                # t1=t0+dot(s,r)/dot(r,r)
                # if(dot(s,r)<0):
                #     if 0<=t1<=t0<=1:
                #         final_l.append((True,1))
                #     else:
                #         final_l.append((False,1))
                # else:
                #     if 0<=t0<=t1<=1:
                #         final_l.append()
                #     # else:
                #     #     final_l.append((False,2))
            elif(cross(r,s)==0 and cross(c,r)!=0):
                continue
                # final_l.append((False,3))
            else:
                t=cross(c,s)/cross(r,s)
                u=cross(c,r)/cross(r,s)
                if 0<t<1 and 0<u:
                    final_l.append(u)
                    # final_l.append((False,4))
        inputs.append(min(final_l))
    print(inputs)
    return inputs

def done(q):
    points1 = [[-200, 200], [200, 200], [-200, 200], [-200, -200], [-100, 100], [100, 100], [-100, 100], [-100, -100]]
    points2 = [[-200, -200], [200, -200], [200, 200], [200, -200], [-100, -100], [100, -100], [100, 100], [100, -100]]
    directions = [[math.cos(math.radians(180)), math.sin(math.radians(180))],
                  [math.cos(math.radians(0)), math.sin(math.radians(0))],
                  [math.cos(math.radians(-90)), math.sin(math.radians(-90))],
                  [math.cos(math.radians(90)), math.sin(math.radians(90))],
                  [math.cos(math.radians(135)), math.sin(math.radians(135))],
                  [math.cos(math.radians(45)), math.sin(math.radians(45))]]
    inputs = False
    for direction in directions:
        for p, d in zip(points1, points2):
            r = [d[0] - p[0], d[1] - p[1]]
            s = direction
            c = [q[0] - p[0], q[1] - p[1]]
            if (cross(r, s) == 0 and cross(c, r) == 0):
                # final_l.append(math.sqrt(dot(c, c)))
                t0=dot(c,r)/dot(r,r)
                t1=t0+dot(s,r)/dot(r,r)
                if(dot(s,r)<0):
                    if 0<=t1<=t0<=1:
                        inputs=inputs or True
                    else:
                        inputs=inputs or False
                else:
                    if 0<=t0<=t1<=1:
                        inputs=inputs or True
                    else:
                        inputs=inputs or False
            elif (cross(r, s) == 0 and cross(c, r) != 0):
                inputs=inputs or False
            else:
                t = cross(c, s) / cross(r, s)
                u = cross(c, r) / cross(r, s)
                if 0 < t < 1 and 0 < u:
                    inputs=inputs or True
                else:
                    inputs=inputs or False
    print(inputs)
    return inputs

