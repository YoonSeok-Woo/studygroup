import queue
M, N = map(int,input().split())
maze = []
visit = list([False]*N for x in range(M))
#print(visit)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(M):
    maze.append(list(map(int,input())))
#print(maze)
q = queue.Queue()
q.put((0,0,1))
visit[0][0]=True
while not q.empty():
    i, j,count = q.get()
    if i == M-1 and j == N-1:
        print(count)
        break
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]
        nc = count+1
        if ni >= M or nj >= N or ni<0 or nj <0:
            continue
        #print(ni,nj)
        if maze[ni][nj]==0 or visit[ni][nj]==True:
            continue
        q.put((ni,nj,nc))
        visit[ni][nj]=True
