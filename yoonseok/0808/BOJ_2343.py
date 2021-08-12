M, N = map(int,input().split())

brs = list(map(int,input().split()))
l = max(brs)
r = sum(brs)  #전체 블루레이 길이
while l<=r:
    mid = (l+r)//2
    nob = 1   #블루레이 갯수
    sum = 0   #블루레이에 담긴 레슨들 길이
    flag = True #혹시 마지막에 담긴 Cd가 남은 길이보다 mid = 15, i= 16 nob+=1 이게 없으면 nob+=1을 안해줌
    for i in brs:
        if i >mid:
            flag = False
            break
        if sum+i<=mid:
            sum+=i
        else :
            nob+=1 #새로운 블루레이에 레슨을 저장
            sum = i #이번에 새로 들어간 레슨
    if not flag:  #범위를 벗어났으니까 
        l=mid+1
    elif nob <=N:
        r = mid-1
    else:
        l = mid+1
print(l)