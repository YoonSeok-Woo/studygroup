# 계속 고치다보니 코드가 꼬임
# 예시 문제만 맞음
import sys
N, M = map(int, sys.stdin.readline().split())
arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    arr[s][e] = arr[e][s] = 1                       # 대각선을 기준으로 대칭이 되도록 그래프 만듦

k = [0] * (N+1)                                     # 연결이 된 노드의 인덱스를 1로 바꿔서, 리스트의 합이 N이 되면 종료하도록 만들려고 했음
s = 1
cnt = 0

while sum(k) < N:
    if sum(k) == N:
        break
    else:
        cnt += 1
        k[s] = 1
        
    for j in range(1, N+1):
        if arr[s][j] == 1 and k[j] == 0:           # 1번 노드에서 시작해서, 연결이 된 노드를 계속 이어가며 k의 인덱스 값을 바꿔줌
            s = j
            k[j] = 1
    

    for i in range(1, N+1):                        # 한 번 끝내면 아직 1로 바뀌지 않은 가장 작은 k의 인덱스 값을 찾아 새로운 루프를 돌려주기
        if k[i] == 0:
            s = i
            break
print(cnt)
