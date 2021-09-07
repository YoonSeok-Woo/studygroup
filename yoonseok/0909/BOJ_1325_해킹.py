from collections import deque
N, M = map(int,input().split())
trust = [0]*(N+1)
net = [[]for i in range(N+1)]
for i in range(M):
    A, B = map(int,input().split())
    net[B].append(A)

def bfs(com):
    q = deque()
    q.append(com)
    count = 1
    hacked = [False]*(N+1)
    #print(com)
    hacked[com] = True
    while q:
        ncom = q.popleft()
        for i in net[ncom]:
            if hacked[i]:
                continue
            count+=1
            hacked[i]=True
            q.append(i)
    return count
for i in range(1,N+1):
    trust[i] = bfs(i)
target = max(trust)
for i in range(1,N+1):
    if trust[i]==target:
        print(i,end= ' ')