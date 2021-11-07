TC = int(input())
for tc in range(1,TC+1):
    N, K = map(int,input().split())
    dp = [[0]*(K+1) for i in range(N)]
    
    V, C = map(int,input().split())
    for j in range(K+1):
        if V<=j:
            dp[0][j] = C
    for i in range(1,N):
        V,C = map(int,input().split())
        for j in range(K+1):
            if j < V:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-V]+C)
    for i in range(N):
        print(dp[i])
    print(f'#{tc} {dp[N-1][K]}')
