import sys
N, M = map(int,sys.stdin.readline().split())
enters = []
r = 0
for i in range(N):
    enters.append(int(sys.stdin.readline()))
    if enters[i]>r:
        r = enters[i]
r *=M #가장 오래걸리는 경우가 가장 긴곳에서 모든 사람이 다 입국심사를 받을때
l = 0
while l<=r:
    mid = (l+r)//2 #이번 경우에서 걸리는 시간
    tr = 0 #시간동안 통과하는 여행객 수
    for i in enters:
        tr+=mid//i #해당 시간동안 각 입국심사장을 통과할 수 있는 사람수
    if tr>=M: #다 통과하거나 더 많이 통과하는 경우 (시간이 넉넉)
        r = mid-1
    else : #시간내에 모든 여행객이 통과 못한 경우 
        l = mid+1
print(l) 