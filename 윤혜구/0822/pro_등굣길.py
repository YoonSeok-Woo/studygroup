#DP
def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    for x, y in puddles:            #웅덩이 = -1
        board[y - 1][x - 1] = -1

    for i in range(n):
        for j in range(m):
            if board[i][j] != -1:   #웅덩이가 아니면 해당 자리까지 올 수 있는 경로의 수 구하기
                if 0 <= i - 1 and board[i-1][j] != -1:  #위에서 오는 경우
                    board[i][j] += board[i-1][j]
                if 0 <= j - 1 and board[i][j-1] != -1:  #왼쪽에서 오는 경우
                    board[i][j] += board[i][j-1]
                board[i][j] = board[i][j]%1000000007
    return board[n-1][m-1]