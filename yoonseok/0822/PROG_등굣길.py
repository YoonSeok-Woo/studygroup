def solution(m, n, puddles):
    answer = 0
    road = [[0]*m for x in range(n)]
    puddcheck = [[False]*m for x in range(n)]
    road[0][0] = 1
    for [j,i] in puddles:
        puddcheck[i-1][j-1] = True
    for i in range(n):
        for j in range(m):
            if i == 0 and j==0:
                continue
            if i==0:
                if not puddcheck[i][j]:
                    road[i][j] = road[i][j-1]
            elif j ==0:
                if not puddcheck[i][j]:
                    road[i][j] = road[i-1][j]
            else:
                if not puddcheck[i][j]:
                    road[i][j] = (road[i-1][j]+road[i][j-1])%1000000007
    #for i in range(n):
    #    print(road[i])
    #for i in range(n):
    #    print(puddcheck[i])
    answer = road[n-1][m-1]
    return answer