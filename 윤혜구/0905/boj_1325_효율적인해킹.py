# #시간초과...
# N, M = map(int, input().split())
# trusts = [map(int, input().split()) for _ in range(M)]
# adj = [[] for _ in range(N + 1)]
# for a, b in trusts:
#     adj[b].append(a)

# max_com = [[0, 0]]
# for n in range(1, N + 1):
#     q = [n]
#     visited = [0] * (N + 1)
#     visited[n] = 1
#     cnt = 0
#     while q:
#         now = q.pop(0)
#         cnt += 1
#         for next in adj[now]:
#             if not visited[next]:
#                 q.append(next)
#                 visited[next] = 1
#     if cnt > max_com[-1][1]:
#         max_com = [[n, cnt]]
#     elif cnt == max_com[-1][1]:
#         max_com.append([n, cnt])

# max_com.sort()
# print(*map(lambda x : x[0], max_com))




#입력방식이랑 큐를 deque로 바꿔주니 통과
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
trusts = [map(int, sys.stdin.readline().split()) for _ in range(M)]
adj = [[] for _ in range(N + 1)]
for a, b in trusts:
    adj[b].append(a)

max_v = 0
max_com = []
for n in range(1, N + 1):
    q = deque()
    q.append(n)
    visited = [0] * (N + 1)
    visited[n] = 1
    cnt = 0
    while q:
        now = q.popleft()
        cnt += 1
        for next in adj[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
    if cnt >= max_v:
        if cnt > max_v:
            max_com = []
        max_v = cnt
        max_com.append(n)

max_com.sort()
print(*max_com)




