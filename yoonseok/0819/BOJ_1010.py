TC = int(input())
for _ in range(TC):
    M, N = map(int,input().split())
    dp = list([0]*(N+1) for x in range(M+1))
    dp[0][0] = 1
    for i in range(1,N+1):
        dp[0][i] = dp[0][i-1]
    for i in range(1,M+1):
        for j in range(1,N+1):
            dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
    print(dp[M][N])