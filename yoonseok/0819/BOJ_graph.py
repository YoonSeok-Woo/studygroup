V, E = map(int,input().split())
array_2d = [[0]*(V+1) for x in range(V+1)]
list_grp = [[] for x in range(V+1)]
for x in range(E):
    i, j = map(int,input().split())
    array_2d[i][j]=1
    array_2d[j][i]=1
    list_grp[i].append(j)
    list_grp[j].append(i)

for i in range(1,V+1):
    print(array_2d[i][1:])
for j in range(1,V+1):
    print(list_grp[j])
