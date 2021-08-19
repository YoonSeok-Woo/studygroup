#인접리스트 방식 그래프, dfs
import sys
sys.setrecursionlimit(10000)    #재귀 한도 늘려줌

def dfs(i):
    visited[i] = 1

    for j in adj[i]:
        if not visited[j]:
            dfs(j)

N, M = map(int, sys.stdin.readline().split())    #node개수, edge개수
edges = [map(int, sys.stdin.readline().split()) for _ in range(M)]
adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for u, v in edges:          #그래프 연결을 나타내는 인접리스트 생성
    adj[u].append(v)
    adj[v].append(u)

answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1
print(answer)