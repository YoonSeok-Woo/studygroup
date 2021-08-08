N = int(input())
l = 0
r = N
while l<=r:
    mid = (l+r)//2
    if mid**2 == N:
        print(mid)
        break
    elif mid**2>N:
        r = mid-1
    else:
        l = mid+1
