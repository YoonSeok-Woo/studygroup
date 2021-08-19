N = int(input())
f1 = 0
f2 = 1
ans = f1+f2
for i in range(2,N):
    f1 = f2
    f2 = ans
    ans = f1+f2
print(ans)
    