# #시간초과...
# #그럴만도.. 최대 2**1000임...
# n = int(input())
# boxes = list(map(int, input().split()))
# max_len = 0

# for i in range(1<<n):
#     cnt = 0
#     temp_max_num = 0
#     for j in range(n):
#         if i & (1<<j):
#             if temp_max_num >= boxes[j]:
#                 break
#             temp_max_num = boxes[j]
#             cnt += 1
#     else:
#         if cnt > max_len:
#             max_len = cnt

# print(max_len)


# DP
# 풀이방법 참고: https://sihyungyou.github.io/baekjoon-1965/
n = int(input())
boxes = list(map(int, input().split()))
dp = [1] * n
answer = 1

for i in range(1, n):
    max_v = 0
    for j in range(i):
        if boxes[j] < boxes[i] and dp[j] > max_v:
            max_v = dp[j]
    dp[i] += max_v
    if dp[i] > answer:
        answer = dp[i]

print(answer)