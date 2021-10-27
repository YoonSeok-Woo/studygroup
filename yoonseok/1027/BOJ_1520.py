dx = [0,1,0,-1]
dy = [1,0,-1,0]
N, M = map(int,input().split())
board = [list(map(int,input().split())) for i in range(N)]
cases = [[-1]*M for i in range(N)]

def dfs(x,y):
    if cases[x][y] != -1:
        return cases[x][y]
    if x==0 and y == 0:
        cases[x][y] = 1
        return 1
    cases[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or ny <0 or nx>=N or ny>=M:
            continue
        if board[nx][ny] > board[x][y]:
            cases[x][y] += dfs(nx,ny)
        
    return cases[x][y]

print(dfs(N-1,M-1))
for i in range(N):
    print(cases[i])