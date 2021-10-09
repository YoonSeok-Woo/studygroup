from collections import deque
N, M = map(int,input().split())

con = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int,input().split())
    con[B].append(A)
    
visit = [False]*(N+1)
X = int(input())

q = deque()
cnt = 0
q.append(X)
visit[X] = True
while q:
    now = q.popleft()
    for i in con[now]:
        if visit[i]:
            continue
        visit[i] = True
        q.append(i)
        cnt+=1
print(cnt)