import sys
N, M = map(int,sys.stdin.readline().split())
enters = []
r = 0
for i in range(N):
    enters.append(int(sys.stdin.readline()))
    if enters[i]>r:
        r = enters[i]
r *=M
l = 0
while l<=r:
    mid = (l+r)//2
    tr = 0
    for i in enters:
        tr+=mid//i
    if tr>=M:
        r = mid-1
    else :
        l = mid+1
print(l) 