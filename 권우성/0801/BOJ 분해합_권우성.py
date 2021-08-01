
total=0
t=0
b= [3,1,4,3,2]
while len(b) >0:
    t = min(b)
    total += t*len(b)
    b.remove(min(b))
print(total)