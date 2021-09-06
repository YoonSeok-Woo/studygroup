from queue import Queue
dx = [1,0,-1,0]
dy = [0,1,0,-1]
M,N,K = map(int,input().split())
paper = [[0]*(N) for i in range(M)]
for i in range(K):
    y1,x1,y2,x2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            paper[i][j] = 1
def bfs(i,j):
    q = Queue()
    q.put((i,j))
    paper[i][j] = 1
    count = 1
    while not q.empty():
        x,y = q.get()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny<0 or nx>=M or ny>=N:
                continue
            if paper[nx][ny]==1:
                continue
            #print(nx,ny)
            paper[nx][ny]=1
            q.put((nx,ny))
            count+=1
    return count
ans = 0
al = []
for i in range(M):
    for j in range(N):
        if paper[i][j] ==0:
            ans+=1
            al.append(bfs(i,j))
al.sort()
print(ans)
for i in al:
    print(i,end = ' ')