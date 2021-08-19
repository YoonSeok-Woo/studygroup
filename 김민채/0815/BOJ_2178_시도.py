# 예제만 잘 됨. 틀림!
# 기준이 있어서 행으로 나눈 건 아니고, 그림으로 그려서 풀다 보니 행을 기준으로 나누게 됨
N, M = map(int, input().split())
mz = []
for i in range(N):
    r = list(map(int, input()))
    mz.append(r)
i = j = 0
cnt = 1
k = 0
while i*j < (N-1)*(M-1):
    if i == 0:                  # 첫 번째 행
        if mz[i][j+1] == 1:
            j += 1
            cnt += 1
            if i == N-1 and j == M-1:
                break
            elif mz[i+1][j] == 1:
                i += 1
                cnt += 1
                k = 0
            elif j == M-1 or mz[i][j+1] != 1:
                j -= 1
                i += 1
                k = 0
        else:
            i += 1
            cnt += 1
    elif i == N-1:              # 마지막 행
        if mz[i][j+1] == 1:
            j += 1
            cnt += 1
            if i == N-1 and j == M-1:
                break
            elif mz[i-1][j] == 1:
                i -= 1
                cnt += 1
                k = 1
            elif mz[i][j+1] != 1:
                j -= 1
                i -= 1
                k = 1
    else:                          # 나머지 행
        if k == 0:
            if  j < M-1 and mz[i][j+1] == 1:
                j += 1
                cnt += 1
            else:
                i += 1
                cnt += 1
        elif k == 1:
            if j < M-1 and mz[i][j+1] == 1:
                j += 1
                cnt += 1 
            else:
                i -= 1
                cnt += 1
print(cnt)    

