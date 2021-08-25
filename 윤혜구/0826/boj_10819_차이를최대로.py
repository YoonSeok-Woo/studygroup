#최대한 내장함수 안쓰고 풀기
#순열 구한다음에 합 비교
N = int(input())
nums = list(map(int, input().split()))
max_sum = 0

def f(s, N):        #순열 구하는 함수
    global max_sum
    if s == N - 1:      #순열을 마지막 수까지 구했으면 합 비교
        temp_sum = 0
        for k in range(N-1):    
            temp_sum += nums[k] - nums[k+1] if nums[k] >= nums[k+1] else nums[k+1] - nums[k]
        if temp_sum > max_sum:
            max_sum = temp_sum

    for i in range(s, N - 1):
        for j in range(i, N):
            nums[i], nums[j] = nums[j], nums[i]
            f(i + 1, N)                             #재귀
            nums[i], nums[j] = nums[j], nums[i]

f(0, N)
print(max_sum)
        


# #다른 사람 풀이
# #https://www.acmicpc.net/source/31969985
# #내장함수 full활용
# #빠름
# from itertools import permutations
# n=int(input())
# a=list(map(int, input().split()))
# ans=0
# for i in permutations(a, n):
#   SUM=0
#   for j in range(len(i)-1):
#     SUM+=abs(i[j]-i[j+1])
#   ans=max(ans, SUM)
# print(ans)