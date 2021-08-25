T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(T):
    M = int(input())
    answer = [0] * 8

    for i in range(8):
        while M >= money[i]:
            M -= money[i]
            answer[i] += 1

    print(f"#{tc + 1}")
    for i in range(8):
        print(answer[i], end=" ")
    print()