#첫 풀이
N = int(input())
S, E = map(int, input().split())
M = int(input())
relations = [list(map(int, input().split())) for _ in range(M)]
edge = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for x, y in relations:      # 무방향 인접리스트
    edge[x].append(y)
    edge[y].append(x)

queue = [S]
answer = 0
turn = 1    #queue에 남은 O촌관계인 사람 수
flag = False    #답을 찾았는지

while queue and not flag:
    now = queue.pop(0)
    visited[now] = 1
    for x in edge[now]:
        if not visited[x]:
            if x == E:
                flag = True
                answer += 1
                break
            else:
                queue.append(x)
    turn -= 1
    if turn == 0 and not flag:
        answer += 1
        turn += len(queue)

print(answer if flag else -1)




#다른사람 풀이 참고
# https://jinho-study.tistory.com/885

from collections import deque

def bfs(s, e):
    queue = deque()
    queue.append(s)
    while queue:
        now = queue.popleft()
        for x in edge[now]:
            if not check[x]:
                check[x] = check[now] + 1   #해당 정점에 오기까지 몇 번 건너왔는지 저장
                queue.append(x)

N = int(input())
S, E = map(int, input().split())
M = int(input())
relations = [list(map(int, input().split())) for _ in range(M)]
edge = [[] for _ in range(N+1)]

for x, y in relations:      # 무방향 인접리스트
    edge[x].append(y)
    edge[y].append(x)

check = [0] * (N+1)
bfs(S, E)
print(check[E] if check[E] > 0 else -1)