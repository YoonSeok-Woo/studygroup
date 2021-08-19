import queue
dx = [1,0,-1,0,1,-1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]
while True:
    w, h = map(int,input().split())
    if w==0 and h==0:
        break
    island = []
    for i in range(h):
        island.append(list(map(int,input().split())))
    visit = list([False]*w for x in range(h))
    ans = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] or island[i][j]==0:
                continue
            else:
                ans+=1
                q = queue.Queue()
                q.put((i,j))
                visit[i][j]=True
                while not q.empty():
                    x,y = q.get()
                    for k in range(8):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx <0 or nx>=h or ny<0 or ny>=w:
                            continue
                        if visit[nx][ny] or island[nx][ny]==0:
                            continue
                        q.put((nx,ny))
                        visit[nx][ny]=True
                    
    print(ans)
