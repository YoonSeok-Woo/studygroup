# https://www.acmicpc.net/problem/13706
# 제곱근
n = int(input())

# start, end index 지정
start = 0
end = n

while end >= start:
    mid = (start + end) // 2

    if mid**2 == n:
        print(mid)
        break

    elif mid**2 > n:
        end = mid - 1

    else:
        start = mid + 1