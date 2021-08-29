# def dfs(i, cnt, sum):
#     if cnt == N:
#         if sum not in answer:
#             answer.append(sum)
#     else:
#         dfs(i + 1, cnt + 1, sum)
#         dfs(i + 1, cnt + 1, sum + scores[i])
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     answer = []
#     dfs(0, 0, 0)
#     print('#{} {}'.format(tc + 1, len(answer)))


# def dfs(i, cnt, sum):
#     if cnt == N:
#         if answer[sum] == 0:
#             answer[sum] = 1
#     else:
#         dfs(i + 1, cnt + 1, sum)
#         dfs(i + 1, cnt + 1, sum + scores[i])
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     answer = [0] * (sum(scores) + 1)
#     dfs(0, 0, 0)
#     print('#{} {}'.format(tc + 1, sum(answer)))



# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     answer = [0]
#     for i in range(N):
#         temp = []
#         for j in range(len(answer)):
#             if answer[j] + scores[i] not in answer:
#                 temp.append(answer[j] + scores[i])
#         answer.extend(temp)
#
#     print('#{} {}'.format(tc + 1, len(answer)))


# from itertools import combinations
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     answer = []
#     for i in range(N + 1):
#         for x in combinations(scores, i):
#             answer.append(sum(x))
#
#     print('#{} {}'.format(tc + 1, len(set(answer))))


# #성공
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     scores = list(map(int, input().split()))
#     answer = [0] * (sum(scores) + 1)
#     an = len(answer)
#     answer[0] = 1
#     for i in range(N):
#         temp = [0] * (sum(scores) + 1)
#         for j in range(an):
#             if answer[j] == 1:
#                 temp[j + scores[i]] = 1
#         for k in range(an):
#             if temp[k] == 1:
#                 answer[k] = 1
#
#     print('#{} {}'.format(tc + 1, sum(answer)))


#실행시간 절반으로 줄인 코드
T = int(input())
for tc in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    visited = [0] * (sum(scores) + 1)
    answer = [0]
    for i in range(N):
        temp = []
        for x in answer:
            if visited[x + scores[i]] == 0:
                temp.append(x + scores[i])
        for x in temp:
            answer.append(x)
            visited[x] = 1

    print('#{} {}'.format(tc + 1, len(answer)))