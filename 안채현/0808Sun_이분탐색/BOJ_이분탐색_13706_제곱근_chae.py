#정수 N이 주어졌을 때, N의 제곱근을 구하는 프로그램을 작성하시오.
#첫째 줄에 양의 정수 N이 주어진다. 정수 N의 제곱근은 항상 정수이며, N의 길이는 800자리를 넘지 않는다.
#첫째 줄에 정수 N의 제곱근을 출력한다.


n = int(input())
low = 1     #left   1
high = n    #right  36

while 1:                    #???? while 1이라는 것은??? while True? / 언젠가 0이되는 순간을 고려한것인가? 무엇이? /아니면 그냥 True해놓고 계속 돌다가 break언젠가 되면 끝나는?
    mid = (low + high) // 2 #(1+36)//2 = 18.5(mid)
    if mid ** 2 == n:       #18.5(mid)값의 제곱이 인풋값 #36 이라면, / 이 mid값이 36의 제곱근임. mid를 출력.
        print(mid)
        break
    elif mid ** 2 > n:      #18.5(mid)값의 제곱이 인풋값 #36 보다 크다면, mid를 줄여서 다시 제곱해야되므로, 우측 기준값을 mid아래로 내려줌
        high = mid - 1
    elif mid ** 2 < n:      #18.5(mid)값의 제곱이 인풋값 #36 보다 작다면, mid를 키워서 다시 제곱해야되므로, 좌측 기준값을 mid위로 올려줌
        low = mid + 1

#참조: https://sinawi.tistory.com/231
