# import sys
# input = sys.stdin.readline

# x_num, y_win = map(int, input().rsplit())       #게임횟수 x, 이긴게임 y 
# z_winningrate = y_win * 100 // x_num            #승률 z   #소수점 버리기 위해 y_win에 먼저 100곱하고
#                                                 #참조: https://www.acmicpc.net/board/view/68226
#                                                 #참조: https://ahn3330.tistory.com/110
# ans = sys.maxsize
# l, r = 1, x_num
# print("[z_winningrate]:", z_winningrate)

# while l <= r:
#     mid = (l + r) // 2

#     curr_vic = (y_win + mid) * 100 // (x_num + mid)
   
#     if curr_vic > z_winningrate:
#         ans = min(mid,ans)
#         r = mid - 1
#     else:
#         l = mid + 1

# if ans == sys.maxsize:
#     print(-1)
# else:
#     print(ans)


#참조: https://velog.io/@uoayop/BOJ-1072-%EA%B2%8C%EC%9E%84Python

#-------------------------------
#형택이가 게임을 최소 몇 번 더 해야 Z가 '변하는지' 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

x_num, y_win = map(int, input().split())       #게임횟수 x, 이긴게임 y     #예제 입력: 각 줄에 정수 X와 Y가 주어진다.
z_winningrate = y_win * 100 // x_num            #승률 z   #소수점 버리기 위해 y_win에 먼저 100곱하고
                                                #참조: https://www.acmicpc.net/board/view/68226
                                                #참조: https://ahn3330.tistory.com/110

if z_winningrate >= 99: #???아, 이미 winning rate가 99라면 (즉, 앞에서 형택이가 한번이라도 졌으면, 승률이 100%은 절대 될 수 없을거니까. 소수점을 자른 상황, 에서 "변하지 않는"수준은 99%가 최선. 100%에 닿지 못하는)
    #이미 전의 모든 게임을 이긴 상황에서만 100%가 가능.
    print(-1)   #예제 출력: 형택이가 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력한다

else:   #z_winningrate < 99 ** 
        #승률이 변한다면 winning rate가 현재 98.xx이면 승률이 최대로 변할 수 있는 99%까지의 1%의 z가 오를 쿠션이 있는 상태. (이미 한번이상은 졌을것이므로 부등호의 기준점이 100%은 아님 이 경우는 패스, 이 경우는 위의 if문에 걸림)
    answer = 0  #형택이가 게임을 최소 몇 판 더 해야하는지 출력값
    left = 1
    right = x_num   #총 할 수 있는 게임횟수!
    
    while left <= right:
        mid = (left + right) // 2
        if (y_win+mid)*100 // (x_num) <= z_winningrate: #x_num은 고정. (총 할 수 있는 게임횟수) / 계속 winningrate가 오르지 않으면 게임을 더 해야하는 것이므로 좌측 기준값을 미드 이상으로 올려줌
            left = mid+1
        else:   #(y_win+mid)*100 // (x_num) > z_winningrate / 기존 winningrate보다 승률이 높아지면, 그 순간 mid값을 일단 answer에 고정해두고(더 while에 걸리면 이걸 바로 답으로 뽑아내도록) 앞으로는 이 mid값보다 더 게임을 적게 했는데도 승률이 바뀔 경우를 보면 되므로 오른쪽 비굣값을 미드 밑으로 당겨옴.
            answer = mid
            right = mid-1

    print(answer)



#참조: https://hillier.tistory.com/70