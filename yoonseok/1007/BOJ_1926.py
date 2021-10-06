from collections import deque
N, M = map(int,input().split())
paper = [list(map(int,input().split())) for i in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
paintings = 0
ans = 0
for i in range(N):
    for j in range(M):
        if paper[i][j]==1:
            paintings+=1
            count = 1
            q = deque()
            q.append((i,j))
            paper[i][j] = 0
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if nx < 0 or ny<0 or nx>=N or ny >=M:
                        continue
                    if paper[nx][ny]==0:
                        continue
                    count+=1
                    q.append((nx,ny))
                    paper[nx][ny] = 0
            ans = max(ans,count)
print(paintings)
print(ans)
