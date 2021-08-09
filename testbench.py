t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if((3*a-b-c)%4==0 and (3*b-c-a)%4==0 and (3*c-b-a)%4==0):
        print("YES")
    else:
        print("NO")