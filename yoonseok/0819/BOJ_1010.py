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
    #print(dp)
    print(dp[M][N])
    #숫자가 너무커서 오히려 계산이 불가능하기 때문에 
    #dp로 풀어야 하는 문제 