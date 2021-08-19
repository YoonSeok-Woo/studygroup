INF = 100
graph = [
    [INF, 5, INF, 8],
    [7, INF, 9, INF],
    [2, INF, INF, 4],
    [INF, INF, 3, INF]
]
for k in range(4): #중간 경유지
    for i in range(4): #출발지
        for j in range(4): #도착지
            if i==j:
                continue
            if graph[i][j] > graph[i][k]+graph[k][i]: #i에서 j를 가는데 k를 거쳐서 가는게 더 짧을경우
                graph[i][j] = graph[i][k]+graph[k][i]
for i in range(4):
    print(graph[i])
