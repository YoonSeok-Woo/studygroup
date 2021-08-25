import itertools

board = [list(map(int, input().split())) for _ in range(5)]
mc = list(itertools.chain(*[list(map(int, input().split())) for _ in range(5)]))
where = [[] for _ in range(26)]     #각 숫자의 위치 저장
row = [0] * 5
col = [0] * 5
d1 = 0      #대각선1
d2 = 0      #대각선2
bingo = 0

for i in range(5):
    for j in range(5):
        where[board[i][j]] = [i, j, i == j, i == 4-j]   #숫자가 불릴 때마다 지워지는 위치 row, col, d1여부, d2여부

for i in range(25): #i+1번째
    num = mc[i]
    row[where[num][0]] += 1
    col[where[num][1]] += 1
    if where[num][2]:
        d1 += 1
    if where[num][3]:
        d2 += 1

    if row[where[num][0]] == 5:
        bingo += 1
    if col[where[num][1]] == 5:
        bingo += 1
    if d1 == 5:
        bingo += 1
        d1 = 0
    if d2 == 5:
        bingo += 1
        d2 = 0
    if bingo >= 3:
        print(i+1)
        break
