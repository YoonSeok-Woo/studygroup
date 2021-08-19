total=0
t=0
N= int(input())
b= list(map(int,input().split()))

while len(b) >0:
    t = min(b)
    total += t*len(b)
    b.remove(min(b))
print(total)