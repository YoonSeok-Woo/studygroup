# 외판원순회2 이건진짜모르겠다

문제출처 - [10971번: 외판원 순회 2 (acmicpc.net)](https://www.acmicpc.net/problem/10971)

문제 요약 

​	1. 외판원이 돌아다니는데 최소비용

input - 

```
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
```

output-

```
35
```

해설코드 

```
import sys
sys.stdin = open("input.txt","r")
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
visited=[False]*n
res=1e9
def dfs(start,cur,cost): #시작점, 노드, 비용
    global arr,visited,res
    if visited.count(True)==n: #방문한 것이 노드의 개수와 같으면
        if arr[cur][start]!=0: #길이 있으면 
            res=min(cost+arr[cur][start],res)
    else:
        for next in range(n):
            if arr[cur][next] != 0 and visited[next]==False: #길이 있고, 방문안했으면
                visited[next]=True
                dfs(start,next,cost+arr[cur][next])
                visited[next]=False

for i in range(n):
    visited[i]=True
    dfs(i,i,0)
    visited[i]=False
print(res)
```

해설2

```
N = int(input())
cities = []
for i in range(N):
    cities.append(list(map(int,input().split())))

def bfs(now, visit, start, cs, cost):
    if cs == N:
        return cost+cities[now][start]
    else:
        ans = 10000000000
        for i in range(N):
            if cities[now][i]==0:
                continue
            if not visit[i]:
                visit[i]=True
                ans = min(ans, bfs(i,visit,start,cs+1,cost+cities[now][i]))
                visit[i]=False
        return ans
ans = 100000000000
visit = [False]*N
for start in range(N):
    visit[start]=True
    ans = min(ans,bfs(start,visit,start, 1,0))
    visit[start]=False
print(ans)
```

