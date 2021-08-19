N = int(input())
cities = []
for i in range(N):
    cities.append(list(map(int,input().split())))
for i in range(N):
    print(cities[i])
def dfs(now, visit, start, cs, cost):
    if cs == N:
        if cities[now][start]==0:
            return 100000000000
        return cost+cities[now][start]
    else:
        ans = 10000000000
        for i in range(N):
            if cities[now][i]==0:
                continue
            if not visit[i]:
                visit[i]=True
                ans = min(ans, dfs(i,visit,start,cs+1,cost+cities[now][i]))
                visit[i]=False
        return ans
ans = 100000000000
visit = [False]*N
for start in range(N):
    visit[start]=True
    ans = min(ans,dfs(start,visit,start, 1,0))
    visit[start]=False
print(ans)