# #brute force
# #시간 초과...
# def math(s, i, _):
#     c = nums[i + 1]
#     if _ == 0:
#         return s + c
#     elif _ == 1:
#         return s - c
#     elif _ == 2:
#         return s * c
#     elif s < 0 and c > 0:
#         return -((-s) // c)
#     else:
#         return s // c

# def bt(i, s):
#     global min_num, max_num
#     if i == N - 1:
#         if s < min_num:
#             min_num = s
#         if s > max_num:
#             max_num = s
#     else:    
#         for j in range(i, N - 1):   #i번째 연산자가 j번째 연산자랑 자리 바꿈
#             # print(i, j, s, ops, ops[i])
#             ops[i], ops[j] = ops[j], ops[i]
#             bt(i + 1, math(s, i, ops[i]))
#             ops[i], ops[j] = ops[j], ops[i]


# N = int(input())
# nums = list(map(int, input().split()))
# op = list(map(int, input().split()))
# ops = [0] * op[0] + [1] * op[1] + [2] * op[2] + [3] * op[3]
# # print(ops)
# min_num = 10000000000
# max_num = -10000000000
# bt(0, nums[0])  #이번에 자리를 바꿀 연산자 index, 현재까지의 sum
# print(max_num)
# print(min_num)




#backtracking
#같은 케이스를 또 고려하는 경우 제거
#연산자 순서 permutation을 실제로 구하면서 계산하는 방식
#864ms
def bt(i, s):
    global min_num, max_num
    case = tuple(ops[:i])
    if case not in memo[i]:
        memo[i].add(case)
    
        if i == N - 1:
            if s < min_num:
                min_num = s
            if s > max_num:
                max_num = s
        else:    
            for j in range(i, N - 1):   #i번째 연산자가 j번째 연산자랑 자리 바꿈
                ops[i], ops[j] = ops[j], ops[i]

                c = nums[i + 1]
                if ops[i] == 0:
                    temp = s + c
                elif ops[i] == 1:
                    temp = s - c
                elif ops[i] == 2:
                    temp = s * c
                elif s < 0 and c > 0:
                    temp = -((-s) // c)
                else:
                    temp = s // c
                bt(i + 1, temp)

                ops[i], ops[j] = ops[j], ops[i]


N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))
ops = [0] * op[0] + [1] * op[1] + [2] * op[2] + [3] * op[3]
memo = {}
for i in range(N):
    memo[i] = set()
min_num = 10000000000
max_num = -10000000000
bt(0, nums[0])  #이번에 자리를 바꿀 연산자 index, 현재까지의 sum
print(max_num)
print(min_num)



# #다른 사람 풀이
# #240ms
# #단순히 남은 연산자 숫자를 빼가면서 dfs 돌리는 방식
# N = int(input())
# nums = list(map(int, input().split()))
# add, sub, mul, div = (map(int, input().split()))

# max_ans = -1000000000
# min_ans = 1000000000
# def dfs(num, depth, add, sub, mul, div):
#     global max_ans, min_ans
    
#     if depth == N:
#         max_ans = max(max_ans, num)
#         min_ans = min(min_ans, num)
#         return 
    
#     if add:
#         dfs(num + nums[depth], depth + 1, add - 1, sub, mul, div)
#     if sub:
#         dfs(num - nums[depth], depth + 1, add, sub - 1, mul, div)
#     if mul:
#         dfs(num * nums[depth], depth + 1, add, sub, mul - 1, div)
#     if div:
#         dfs(int(num / nums[depth]), depth + 1, add, sub, mul, div - 1)

# dfs(nums[0], 1, add, sub, mul, div)
# print(max_ans)
# print(min_ans)
