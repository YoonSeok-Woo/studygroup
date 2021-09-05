TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = list(map(int,input().split()))
    LIS = [-1]*N
    LIS[0] = arr[0]
    ans = 1
    max_num = arr[0]
    for i in range(1,N):
        if max_num < arr[i]:
            LIS[ans] = arr[i]
            max_num = arr[i]
            ans+=1
        else:
            for j in range(ans):
                if LIS[j] > arr[i]:
                    LIS[j] = arr[i]
                    if j==ans-1:
                        max_num = arr[i]
                    break
    print(f'#{tc} {ans}')