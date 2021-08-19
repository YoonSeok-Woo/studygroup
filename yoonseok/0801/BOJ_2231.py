def n_sum(num):
    res = num
    while num>0:
        res+=num%10
        num=num//10
    return res
N = int(input())
for i in range(N):
    if n_sum(i)==N:
        print(i)
        break