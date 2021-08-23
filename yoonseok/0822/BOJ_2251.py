A, B, C = map(int,input().split())
check = [[[False]*(C+1) for _ in range(B+1)] for __ in range(A+1)]
def dfs(a,b,c):
    #print(a,b,c)
    check[a][b][c]=True
    #a물통에서 b물통에 물붓기
    if a+b>B:
        na = a+b-B
        nb = B
        if not check[na][nb][c]:
            dfs(na,nb,c)
    else:
        na = 0
        nb = a+b
        if not check[na][nb][c]:
            dfs(na, nb, c)
    #a물통에서 c물통에 물붓기
    if a+c>C:
        na = a+c-C
        nc = C
        if not check[na][b][nc]:
            dfs(na,b,nc)
    else:
        na = 0
        nc = a+c
        if not check[na][b][nc]:
            dfs(na,b,nc)
    #b물통에서 a물통에 물붓기
    if a+b>A:
        na = A
        nb = a+b-A
        if not check[na][nb][c]:
            dfs(na,nb,c)
    else:
        na = a+b
        nb = 0
        if not check[na][nb][c]:
            dfs(na,nb,c)
    #b물통에서 c물통에 물붓기
    if b+c>C:
        nc = C
        nb = a+c-C
        if not check[a][nb][nc]:
            dfs(a,nb,nc)
    else:
        nb = 0
        nc = b+c
        if not check[a][nb][nc]:
            dfs(a,nb,nc)
    #c물통에서 a물통으로
    if a+c>A:
        na = A
        nc = a+c-A
        if not check[na][b][nc]:
            dfs(na,b,nc)
    else:
        na = a+c
        nc = 0
        if not check[na][b][nc]:
            dfs(na,b,nc)
    #c물통에서 b물통으로
    if b+c>B:
        nb = B
        nc = b+c-B
        if not check[a][nb][nc]:
            dfs(a,nb,nc)
    else:
        nb = b+c
        nc = 0
        if not check[a][nb][nc]:
            dfs(a,nb,nc)
dfs(0,0,C)
ans = []
for j in range(B+1):
    for k in range(C+1):
        if check[0][j][k]:
            ans.append(k)
ans.sort()
for i in ans:
    print(i, end = ' ')