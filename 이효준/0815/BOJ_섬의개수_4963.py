# 참고: https://pacific-ocean.tistory.com/273


# 8 방향을 봐야함 3시 기준 시계방향
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = 0
    # grid 만들기
    grid = [[0] * w for _ in range(h)]
    for i in range(0, h):
        temp = list(map(int, input().split()))
        k = -1
        for j in range(0, w):
            k += 1
            grid[i][j] = temp[k]

    for i in range(0, h):
        for j in range(0, w):
            if grid[i][j] == 1:
                for k in range(8):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1:
                        pass

    print(island)
