# #처음 풀었던 풀이
# #시간 개느림
# def bridgeNum(N, M):                #recursive function
#     if N == 0 or M == 0 or N > M:
#         return 0
#     elif N == 1:                    #base case
#         return M
#     else:
#         answer = 0
#         for i in range(M):
#             if (N - 1, M - i -1) not in memo:       #memoization
#                 memo[(N - 1, M - i -1)] = bridgeNum(N - 1, M - i - 1)
#             answer += memo[(N - 1, M - i -1)]
#         return answer

# T = int(input())

# for tc in range(T):
#     N, M = map(int, input().split())
    
#     memo = {}
#     print(bridgeNum(N, M))



#조합으로 푼 풀이
#어차피 우측 m개 스팟 중에서 n개를 고르기만 하면 다리의 순서는 정해져있기 때문에 mCn의 결과와 같음
#mCn = m!/(m-n)!n!
#참고: https://yoonsang-it.tistory.com/33
def factorial(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    bridges = factorial(M) // (factorial(M - N) * factorial(N))
    print(bridges)

