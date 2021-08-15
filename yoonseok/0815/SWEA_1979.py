TC = int(input())
for tc in range(1,TC+1):
    N,K = map(int,input().split())
    puzzle = []
    ans =0
    for i in range(N):
        puzzle.append(list(map(int,input().split())))
    for i in range(N):
        for j in range(N):
            if puzzle[i][j]==1:
                #먼저 세로부터 확인
                if i-1<0 or puzzle[i-1][j]==0:
                    ni = i+1
                    count = 1
                    while ni <N:
                        if puzzle[ni][j]==1:
                            count+=1
                        else:
                            break
                        ni+=1
                    if count==K:
                        ans+=1
                    #print(count,i,j,'세로')
                if j-1<0 or puzzle[i][j-1]==0:
                    nj = j+1
                    count = 1
                    while nj <N:
                        if puzzle[i][nj]==1:
                            count+=1
                        else:
                            break
                        nj+=1
                    if count==K:
                        ans+=1
                    #print(count,i,j,'가로')
    print(f'#{tc} {ans}')

