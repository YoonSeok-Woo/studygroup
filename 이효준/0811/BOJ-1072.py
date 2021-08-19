# https://www.acmicpc.net/problem/1072
# 게임 횟수: X
# 이긴 게임: Y
# 승률(Z) : X/Y

x, y = list(map(int, input().split()))

game = x
win = y
cnt = 0

#
Z = int(y * 100 / x)

while True:
    if Z == 100 or game > 1000000000:
        print(-1)
        break

    target = int(win * 100 / game)

    if Z != target:
        print(cnt)
        break

    else:
        win += 1
        game += 1

    cnt += 1
