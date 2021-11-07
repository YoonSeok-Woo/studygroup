TC = int(input())
def dfs(ind):
    global answer
    answer +=1
    #print(burger)
    for i in range(ind+1,N+1):
        if visit[i]:
            continue
        for j in burger:
            if comb[i][j]:
                break
        else:
            visit[i]=True
            burger.append(i)
            dfs(i)
            visit[i]=False
            burger.pop()
        

for tc in range(1,TC+1):
    N, M = map(int,input().split())
    comb = [[0]*(N+1) for _ in range(N+1)]
    for i in range(M):
        A, B = map(int,input().split())
        comb[A][B]=1
        comb[B][A]=1
    visit = [False]*(N+1)
    burger = []
    answer = 0
    dfs(0)
    print(f'#{tc} {answer}')