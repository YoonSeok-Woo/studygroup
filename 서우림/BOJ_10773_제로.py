import sys

k = int(sys.stdin.readline())
i = 0
money = []
for _ in range(k):
    num = int(input())
    i += 1
    if num != 0:
        money.append(num)
    else:
        money.pop()

print(sum(money))

