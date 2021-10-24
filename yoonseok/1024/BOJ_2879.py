N = int(input())
nums = list(map(int,input().split()))
targets = list(map(int,input().split()))
for i in range(N):
    targets[i] -=nums[i]
def working(l,r):
    global answer
    i = l
    while i<r:
        if targets[i]==0:
            i+=1
            continue
        else:
            if targets[i]>0:
                temp_l = i
                pages = targets[i]
                while i<r and targets[i]>0:
                    pages = min(abs(targets[i]),abs(pages))
                    i+=1
                for j in range(temp_l,i):
                    targets[j]-=pages
                answer+=pages
                working(temp_l,i)
            elif targets[i]<0:
                temp_l = i
                pages = abs(targets[i])
                while i<r and targets[i]<0:
                    pages = min(abs(targets[i]),abs(pages))
                    i+=1
                for j in range(temp_l,i):
                    targets[j]+=pages
                answer+=pages
                working(temp_l,i)

answer = 0
working(0,N)
print(answer)