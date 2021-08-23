N, L = map(int,input().split())
holes = list(map(int,input().split()))
count = 0
fh = 0
for i in holes:
    if fh==0 or i-fh>=L:
        fh = i
        count+=1
print(count)