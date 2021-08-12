X,Y = map(int,input().split())
Z = Y*100//X
ans = -1
l = 0
r = 10000000000
if Z >=99:
    print(-1)
else:
    while l<=r:
        mid = (l+r)//2
        if (Y+mid)*100//(X+mid) >Z:
            r = mid-1
            ans = mid
        else :
            l = mid+1
    print(ans)