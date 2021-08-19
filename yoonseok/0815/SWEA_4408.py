TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    tfr = [0]*401
    for i in range(N):
        now, back = map(int,input().split())
        for j in range(now,back):
            tfr[j]+=1
    print(f'#{tc} {max(tfr)}')