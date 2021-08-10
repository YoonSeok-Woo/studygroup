N = int(input())
arr = list(map(int,input().split()))
son = []
inp = 0
for i in arr:
    if inp<0:
        inp = i
    else:
        inp+=i
    son.append(inp)
print(max(son))
