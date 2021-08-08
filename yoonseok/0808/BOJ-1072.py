from math import floor
X,Y = map(int,input().split())
Z = int(Y/X*100)
ans = -1
l = 0
r = 10000000000
if Z >=99:
    print(-1)
else:
    while l<=r:
        mid = (l+r)//2
        if (Y+mid)*100//(X+mid) >Z:
            ans = mid
            r = mid-1
        else :
            l = mid+1
    print(r+1)