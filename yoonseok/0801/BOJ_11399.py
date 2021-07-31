N = int(input())
P = list(map(int,input().split()))
P.sort()
print(P)
ans = 0
sum = 0
for i in P:
    sum+=i
    ans +=sum
    
print(ans)