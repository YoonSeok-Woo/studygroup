def dfs(node):
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            dfs(i)

N, M = map(int, input().split())

adj = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)