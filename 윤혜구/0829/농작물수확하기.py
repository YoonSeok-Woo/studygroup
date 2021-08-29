T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    c = N // 2
    total = sum(board[c])
    for i in range(1, c + 1):
        total += sum(board[c + i][i:N-i])
        total += sum(board[c - i][i:N - i])
    print('#{} {}'.format(tc + 1, total))