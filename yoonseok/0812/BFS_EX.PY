import time
import queue
maze = [
    [0,1,1,1,1],
    [0,0,0,0,1],
    [1,0,1,1,1],
    [0,0,0,0,1],
    [1,1,1,0,0]
]
N = 5
di = [0,1,0,-1]
dj = [1,0,-1,0]
visit = list([False]*5 for x in range(5))
maze[0][0]=2
def bfs(i,j):
    q = queue.Queue()
    q.put((i,j))
    for x in range(N):
        for y in range(N):
            print(maze[x][y],end=' ')
        print()
    print("------------------------------------------")
    time.sleep(1)
    while not q.empty():
        ti,tj = q.get()
        for dir in range(4):
            ni = ti+di[dir]
            nj = tj+dj[dir]
            if ni>=N or nj>=N or ni<0 or nj<0:
                continue
            if visit[ni][nj]==True or maze[ni][nj]==1:
                continue
            q.put((ni,nj))
            visit[ni][nj]=True
            maze[ni][nj]=2
            for x in range(N):
                for y in range(N):
                    print(maze[x][y],end=' ')
                print()
            print("------------------------------------------")
            time.sleep(1)
bfs(0,0)