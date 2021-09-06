T = int(input())
for tc in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    check = [0] * (N + 1)
    answer = 0
    for i in range(1, N + 1):
        max_i = 0
        for j in range(0, i):
            if nums[i] >= nums[j] and check[j] > check[max_i]:
                max_i = j
        check[i] = check[max_i] + 1
        if check[i] > answer:
            answer = check[i]
    print(f'#{tc + 1} {answer}')