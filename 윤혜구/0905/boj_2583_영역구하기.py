M, N, K = map(int, input().split())
squares = [map(int, input().split()) for _ in range(K)]
board = [[0] * N for _ in range(M)]
for sc, sr, ec, er in squares:          #사각형 그리기
    for i in range(sr, er):
        for j in range(sc, ec):
            board[i][j] = 1

ans_list = []
for i in range(M):                      #bfs
    for j in range(N):
        if board[i][j] == 0:
            q = [(i, j)]
            board[i][j] = 1
            temp_cnt = 1
            while q:
                ci, cj = q.pop(0)
                for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 0:
                        q.append((ni, nj))
                        board[ni][nj] = 1
                        temp_cnt += 1
            ans_list.append(temp_cnt)

ans_list.sort()
print(len(ans_list))
print(*ans_list)




#이게 오히려 더 느림
# from collections import deque
# import pprint

# M, N, K = map(int, input().split())
# squares = [map(int, input().split()) for _ in range(K)]
# board = [[0] * N for _ in range(M)]
# for sc, sr, ec, er in squares:          #사각형 그리기
#     for i in range(sr, er):
#         for j in range(sc, ec):
#             board[i][j] = 1

# area_num = 0
# ans_list = []
# for i in range(M):                      #bfs
#     for j in range(N):
#         if board[i][j] == 0:
#             # pprint.pprint(board)
#             q = deque()
#             q.append((i, j))
#             board[i][j] = 1
#             temp_cnt = 1
#             while q:
#                 # print(f'{q=}')
#                 ci, cj = q.popleft()
                
#                 for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
#                     ni, nj = ci + di, cj + dj
#                     if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 0:
#                         q.append((ni, nj))
#                         board[ni][nj] = 1
#                         temp_cnt += 1
#             ans_list.append(temp_cnt)
#             area_num += 1

# ans_list.sort()
# print(area_num)
# for ans in ans_list:
#     print(ans, end=" ")