N = int(input())
arr_2d = list(list(0 for i in range(N)) for i in range(N))
for i in range(N):
    fl = list(map(int,input().split()))
    for j, num in enumerate(fl):
        arr_2d[i][j]=num
    del fl
    print(arr_2d[i])
for i, arr in enumerate(arr_2d):
    if(i==0):
        continue
    for j, num in enumerate(arr):
        if j==0:
            arr_2d[i][j]=arr_2d[i-1][j]+arr_2d[i][j]
        else:
            arr_2d[i][j] += max(arr_2d[i-1][j],arr_2d[i-1][j-1])
    print(arr_2d[i])
print(max(arr_2d[N-1]))
