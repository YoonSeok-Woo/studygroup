# 목
# https://www.acmicpc.net/problem/11053
# 가장 긴 증가하는 부분 수열
# set 안쓰고 이분탐색으로

n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n
idx, cnt = 0, 0
minV = min(arr)

while True:
    if arr[idx] == minV:
        temp[idx] = cnt
    elif minV > arr[idx]:
        minV = arr[idx]
        idx = 0

    if idx == n:
        idx += 1

    cnt += 1





# while start >= end:
    # mid = (start + end) // 2