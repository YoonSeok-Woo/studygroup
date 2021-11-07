TC = int(input())

for tc in range(1,TC+1):
    a,b,c = map(int,input().split())
    lengthes = [0]*101
    lengthes[a]+=1
    lengthes[b]+=1
    lengthes[c]+=1
    for i,num in enumerate(lengthes):
        if num%2:
            print(f'#{tc} {i}')
            break