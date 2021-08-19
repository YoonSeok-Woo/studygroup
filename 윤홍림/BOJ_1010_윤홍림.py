T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, list(input().split()))
    M_fact = 1
    N_fact = 1
    MN_fact = 1
    for i in range(1, M+1):
        M_fact *= i
    for i in range(1, N+1):
        N_fact *= i
    for i in range(1, M-N+1):
        MN_fact *= i
    ans = M_fact // (N_fact * MN_fact)
    print(ans)