M, N = map(int,input().split())

brs = list(map(int,input().split()))
l = max(brs)
r = sum(brs)
while l<=r:
    mid = (l+r)//2
    nob = 1
    sum = 0
    for i in brs:
        if sum+i<=mid:
            sum+=i
        else :
            nob+=1
            sum = i
    
    if nob <=N:
        r = mid-1
    else:
        l = mid+1
print(l)