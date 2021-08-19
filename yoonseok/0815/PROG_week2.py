graph=[
    [0,0,0,0,0,1],
    [0,0,1,1,0,0],
    [0,1,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,0,1],
    [1,0,0,0,1,0]
]
par = list(x for x in range(6))#각 노드의 부모
print(par)
def getPar(x):
    #부모가 자기 자신이면
    if par[x]==x :
        return x
    par[x] = getPar(par[x])
    return par[x]

def union(x1,x2):
    x1_par = getPar(x1)
    x2_par = getPar(x2)
    if x1_par <x2_par:
        par[x2]=x1_par
    else :
        par[x1]=x2_par
    print(x1,x2,par)

def findPar(x1,x2):
    a = getPar(x1)
    b = getPar(x2)
    if a==b:
        return True
    else:
        return False

for i in range(6):
    for j in range(i+1,6):
        if graph[i][j]==1:
            union(i,j)
print(par)