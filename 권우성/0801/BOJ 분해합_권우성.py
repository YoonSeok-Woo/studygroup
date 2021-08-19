k=[]
a= int(input())
for i in range(0,a+1):
    b=str(i)
    if (sum(map(int,b))+i) ==a:
        k += [i]
        print(min(k))
        break


if (i == a):
    print(0)