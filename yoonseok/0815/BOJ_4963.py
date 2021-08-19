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
                q.put((i,j))#첫 방문지점 큐에 추가
                visit[i][j]=True
                while not q.empty(): #큐가 비어있지 않는동안에 탐색 진행
                    x,y = q.get()    #큐의 맨 앞원소를 현재 탐색할 지점
                    for k in range(8):#탐색 조건
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx <0 or nx>=h or ny<0 or ny>=w:
                            continue
                        if visit[nx][ny] or island[nx][ny]==0:
                            continue
                        q.put((nx,ny)) #탐색 조건에 부합하면 큐에 추가 BFS 구현 방식
                        visit[nx][ny]=True
                    
    print(ans)
