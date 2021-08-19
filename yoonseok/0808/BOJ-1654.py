K, N = map(int,input().split())
lans = []
l = 0
r = 0
for i in range(K):
    lans.append(int(input()))
    if r <lans[i]:
        r = lans[i]
ans = 0
while l<=r:
    mid = (l+r)//2
    check = 0
    for i in lans:
        check+=i//mid
    if check >= N:
        ans = mid
        l = mid+1
    else:
        r = mid-1
print(int(ans))
