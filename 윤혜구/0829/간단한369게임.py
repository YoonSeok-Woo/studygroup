def num(n):
    orig = n
    cnt = 0
    while n > 0:
        c = n % 10
        if c == 3 or c == 6 or c == 9:
            cnt += 1
        n //= 10
    return '-' * cnt if cnt > 0 else orig


N = int(input())
for i in range(1, N + 1):
    print(num(i), end=" ")
