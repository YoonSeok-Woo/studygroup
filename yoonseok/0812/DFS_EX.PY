import time
maze = [
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,0]
]
N = 5
di = [0,1,0,-1] #오른쪽 아래 왼쪽 위
dj = [1,0,-1,0]
visit = list([False]*5 for x in range(5))
maze[0][0]=2
def dfs(i,j):
    global N
    for x in range(N):
        for y in range(N):
            print(maze[x][y],end=' ')
        print()
    print("------------------------------------------")
    time.sleep(1)
    if i==N-1 and j == N-1:
        return
    for dir in range(4):
        ni = i+di[dir]
        nj = j+dj[dir]
        
        if ni<0 or nj<0 or ni>=N or nj>=N:
            continue
        #print(ni,nj)
        if maze[ni][nj]==1 or visit[ni][nj]==True:
            continue
        
        maze[ni][nj]=2
        visit[ni][nj]=True
        dfs(ni,nj)
        maze[ni][nj]=0
        visit[ni][nj]=False
        for x in range(N):
            for y in range(N):
                print(maze[x][y],end=' ')
            print()
        print("------------------------------------------")
        time.sleep(1)

dfs(0,0)