N = int(input())
t1, t2 = map(int,input().split())
M = int(input())
con = [[] for x in range(N+1)]
for i in range(M):
    x, y = map(int,input().split())
    con[x].append(y)
    con[y].append(x)
visit = [False]*(N+1)
q = []
front = 0
back = -1
q.append((t1,0))#시작점과 시작점의 촌수는 0이니까
back+=1
visit[t1]=True
while back>=front:#큐가 비어있지 않는 동안에
    now, ans = q[front]
    front+=1
    if now == t2:#도착했다면
        print(ans)#촌수 출력하고 마무리
        break
    for i in con[now]:
        if visit[i]:
            continue
        q.append((i,ans+1))
        back+=1
        visit[i]=True
else:
    print(-1)
