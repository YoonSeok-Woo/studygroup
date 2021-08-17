import sys
sys.setrecursionlimit(10000)
import queue
N, M = map(int,input().split())
con = [[] for x in range(N+1)]
connected = [False]*(N+1)
def bfs(now):
    q = queue.Queue()
    q.put(now)
    connected[now]=True
    while not q.empty():
        now = q.get()
        for i in con[now]:
            next = i
            if connected[next]:
                continue
            connected[next]=True
            q.put(next)

ans = 0
for k in range(M):
    i, j = map(int,input().split())
    con[i].append(j)
    con[j].append(i)
#print(con)
for i in range(1,N+1):
    if connected[i]:
        continue
    else:
        ans+=1
        bfs(i)
        #print(connected)
print(ans)
