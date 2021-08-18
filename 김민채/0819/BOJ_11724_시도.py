import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e] = arr[e][s] = 1

k = [0] * (N+1)
s = 1
cnt = 0

while sum(k) < N:
    if sum(k) == N:
        break
    else:
        cnt += 1
        k[s] = 1
        
    for j in range(1, N+1):
        if arr[s][j] == 1 and k[j] == 0:
            s = j
            k[j] = 1
    

    for i in range(1, N+1):
        if k[i] == 0:
            s = i
            break
print(cnt)
