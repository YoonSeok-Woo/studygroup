#BFS
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
queue = [[0, 0]] #[row, column]
moves = 0   #몇 번 움직였는지
turn = 0    #이번 move에 갈 수 있는 칸들의 개수

while queue:
    if turn == 0:
        turn = len(queue)
        moves += 1

    
    i, j = queue.pop(0)
    if i == N - 1 and j == M - 1:
        break

    #다음 갈 수 있는 칸 탐색
    if j - 1 >= 0 and board[i][j - 1] == 1:  #좌
        board[i][j - 1] = -1                            #이미 갔던 길을 다시 방문하지 않기 위한 처리
        queue.append([i, j - 1])                        
    if j + 1 < M and board[i][j + 1] == 1:   #우
        board[i][j + 1] = -1
        queue.append([i, j + 1])
    if i - 1 >= 0 and board[i - 1][j] == 1:  #상
        board[i - 1][j] = -1
        queue.append([i - 1, j])
    if i + 1 < N and board[i + 1][j] == 1:  #하
        board[i + 1][j] = -1
        queue.append([i + 1, j])

    turn -= 1

print(moves)

    