#DFS
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:   #0 0이면 종료
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]  #한 땅에서 갈 수 있는 모든 방향

    island = 0
    stack = []

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                stack.append([i, j])
                while stack:
                    ti, tj = stack.pop()    #현재 땅과   
                    for di, dj in direction:    #연결된 땅 모두 찾기
                        if 0 <= ti + di < h and 0 <= tj + dj < w and board[ti + di][tj + dj] == 1:
                            stack.append([ti + di, tj + dj])
                    board[ti][tj] = -1      #이미 방문한 땅
                island += 1     #연결된 땅 다 찾으면 섬 +1

    print(island)