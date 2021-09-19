def solution(board):
    answer = 0
    m = len(board)
    n = len(board[0])
    dp = [[0]*n for x in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or j == 0:
                dp[i][j] = board[i][j]
            else:
                if board[i][j]!=0:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
            answer = max(answer,dp[i][j])
    #for i in range(m):    
    #    print(dp[i])
    return answer**2
# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
# def solution(board):
#     answer = 0
#     m = len(board)
#     n = len(board[0])
#     for i in range(m):
#         for j in range(n):
#             #이 칸에서 시작하는 가장 큰 정사각형을 찾아볼 것
#             for k in range(min(m-i,n-j),-1,-1):
#                 ok = True  #정사각형인가
#                 for a in range(k):
#                     if not ok:
#                         break
#                     for b in range(k):
#                         if board[i+a][j+b]==0:
#                             ok = False
#                             break
#                 if ok : #큰순서대로 찾아보는거라서 방금 탐색한 범위가 정사각형이라면 이 칸에서 찾을수 있는 가장 큰 정사각형을 찾은거니까
#                     answer = max(k,answer)#다음칸으로 넘어간다
#                     break
                



#     return answer**2



# print(solution(board))
