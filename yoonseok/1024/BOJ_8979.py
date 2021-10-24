N, K = map(int,input().split())
medals = []

def cmp(a,b):
    if a[1]==b[1] and a[2]==b[2] and a[3]==b[3]:
        return True
    else:
        return False

for i in range(1,N+1):
    medals.append(list(map(int,input().split())))

medals.sort(key = lambda k : (k[1],k[2],k[3]),reverse = True)
for i in range(1,N):
    if medals[i][0]==K:
        target = i
        break
for i in range(N):
    if cmp(medals[i],medals[target]):
        print(i+1)
        break


