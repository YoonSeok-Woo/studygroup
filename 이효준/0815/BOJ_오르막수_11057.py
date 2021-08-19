# 오르막 수는 수의 자리가 오름차순을 이루는 수.
# 인접한 경우도 오름차순
# 1 2 3 4 5...
# 1 3 5 11 21...

N = int(input())

# n x 10 행렬 초기화
up = [[0] * 10 for _ in range(N+1)]

# N = 1 // 한자리 수 일 때의 base-case
up[1] = [1] * 10

for i in range(2, N+1):
    #  0일 경우 0 밖에 없으니 0으로 끝나는 N자리 숫자의 개수 = 1
    up[i][0] = 1

    for j in range(10):
        up[i][j] = up[i-1][j] + up[i][j-1]

print(sum(up[N]) % 10007)