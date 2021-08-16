N = int(input())
dp = list([0]*11 for i in range(1001))
for i in range(10):
    dp[1][i]=1
dp[1][10]=sum(dp[1])
for i in range(2,N+1):
    for j in range(10):
        if j == 0:
            dp[i][j]=dp[i-1][10]
            dp[i][10]= dp[i][j]
        else:
            dp[i][j] = (dp[i][j-1]-dp[i-1][j-1])%10007
            dp[i][10]= (dp[i][10]+dp[i][j])%10007
print(dp[N][10])