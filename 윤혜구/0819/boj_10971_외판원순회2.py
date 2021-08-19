# import sys
# N = int(input())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    #비용 행렬
# min_cost = 100000000

# def dfs(start, i, visited_num, visited, cost):
#     global min_cost

#     if cost > min_cost:
#         return

#     if visited_num == N:
#         cost += board[i][start]
#         min_cost = cost if cost < min_cost else min_cost
#         return
    
#     for j in range(N):
#         if board[i][j] and not visited[j]:
#             visited[j] = 1
#             dfs(start, j, visited_num + 1, visited, cost + board[i][j])


# for i in range(N):
#     visited = [0] * N
#     visited[i] = 1
#     dfs(i, i, 1, visited, 0)

# print(min_cost)


#다른 코드 참고한 코드
import sys
N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]    #비용 행렬
visited = [0] * N
min_cost = 100000000

def travel(n, cost):
    global N, board, visited, min_cost

    if cost < min_cost:     #이미 비용이 최소비용 이상이 된 경우 건너뜀
        if all(visited) and n == 0:     #한바퀴 다 돌았을 경우에만
            min_cost = min(min_cost, cost)  #최소비용 업데이트
    
        for i in range(N):
            if board[n][i] and not visited[i]:
                visited[i] += 1
                travel(i, cost + board[n][i])
                visited[i] -= 1

travel(0, 0)        #어디서 시작해도 결국 한바퀴를 돌게 되므로 한 군데서만 시작해보면 됨
print(min_cost)