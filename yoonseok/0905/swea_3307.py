TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    arr = list(map(int,input().split()))    #[ 4, 2, 3, 1, 5, 6] arr
    LIS = [-1]*N                            #[ 1, 3,-1,-1,-1,-1] LIS
    LIS[0] = arr[0]                         #[ 0, 1, 2, 3, 4, 5] index
    ans = 1                                 #ans = 2  range(ans) = (0,1)
    max_num = arr[0]                        #max_num LIS배열에서 가장 큰 수 3
    for i in range(1,N):
        if max_num < arr[i]:
            LIS[ans] = arr[i]
            #max_num= max(LIS)
            max_num = arr[i]
            ans+=1
        else:
            for j in range(ans):
                if LIS[j] > arr[i]:
                    LIS[j] = arr[i]
                    #max_num = max(LIS)
                    if j==ans-1: #방금 LIS배열에서 값을 갱신해준 곳이 LIS에서 제일 큰수가 오는 곳일 경우
                        max_num = arr[i]
                    break
    print(f'#{tc} {ans}')