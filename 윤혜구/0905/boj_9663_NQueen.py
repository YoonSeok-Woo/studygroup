def get_bd1(r, c):
    return (c - r) + (N - 1)

def get_bd2(r, c):
    return r + c

def bt(row, cnt):
    global answer
    if row == N:
        if cnt == N:
            answer += 1
    else:
        for k in range(N + 1):      #row 줄에 놓을 수 있는 곳이 있는지 탐색
            if k == N:
                break

            if vc[k] + vd1[get_bd1(row, k)] + vd2[get_bd2(row, k)] == 0:      #놓을 수 있는 자리면
                vc[k] = 1                   #놓음 표시
                vd1[get_bd1(row, k)] = 1
                vd2[get_bd2(row, k)] = 1

                bt(row + 1, cnt + 1)        #다음 줄 탐색

                vc[k] = 0                   #놓음 표시 되돌리기
                vd2[get_bd2(row, k)] = 0
                vd1[get_bd1(row, k)] = 0



N = int(input())
answer = 0
vc = [0] * N    #visited column 
vd1 = [0] * (2 * N - 1)   #우하향 대각선 visited
vd2 = [0] * (2 * N - 1)   #좌하향 대각선 visited
bt(0, 0)
print(answer)