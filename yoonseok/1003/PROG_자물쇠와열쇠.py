def rotation(key):
    M = len(key)
    res = [[0]*M for i in range(M)]
    for i in range(M):
        for j in range(M):
            res[i][j] = key[M-j-1][i]
    return res

def check(key,lock,x, y):
    M = len(key)
    N = len(lock)
    temp = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = lock[i][j]
    for i in range(M):
        for j in range(M):
            if i+x>=N or j+y>=N or i+x<0 or j+y <0:
                continue
            temp[i+x][j+y] = lock[i+x][j+y] +key[i][j]
    #print(temp)
    for i in range(N):
        for j in range(N):
            if temp[i][j]!=1:
                return False
    return True



def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    
    for k in range(4):
        #print(key)
        for i in range(-M+1,N):
            for j in range(-M+1,N):
                if check(key,lock,i,j):
                    answer = True
                    break
            if answer:
                break
        if answer:
            break
        key = rotation(key)
        
                
                
    return answer