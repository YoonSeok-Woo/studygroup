dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]
def bfs(n, m):
    s[n][m] = 0
    queue = [[n, m]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(8):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < h and 0<= y < w and s[x][y] == 1:
                s[x][y] = 0
                queue.append([x, y])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    s = []
    cnt = 0
    for i in range(h):
        s.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if s[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
