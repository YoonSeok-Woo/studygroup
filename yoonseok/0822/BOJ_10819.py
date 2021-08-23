N = int(input())
arr = list(map(int,input().split()))
used = [False]*N
ans = 0
def bfs(used,num,now,count):
    global ans
    if count==N:
        ans = max(ans,num)
    for i,n in enumerate(arr):
        if used[i]:
            continue
        used[i]=True
        
        bfs(used,num+abs(now-n),n,count+1)
        
        used[i]=False
order = []
for i,n in enumerate(arr):
    used[i]=True
    bfs(used,0,n,1)
    used[i]=False
print(ans)