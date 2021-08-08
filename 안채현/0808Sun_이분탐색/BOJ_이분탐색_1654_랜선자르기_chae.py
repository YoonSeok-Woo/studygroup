#자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정
#N개보다 많이 만드는 것도 N개를 만드는 것에 포함
#만들 수 있는 최대 랜선의 '길이'
#첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력
#항상 K ≦ N 
#그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력
#첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.


#랜선의 길이를 움직여 랜선 개수를 채우는지 봄.
import sys
K_hold, N_need = map(int, input().split())      #4(현재 가지고있는) 11(필요한)
lan_each_length_list = [int(sys.stdin.readline()) for i in range(K_hold)] #list comprehension 쓰는 법 알아두기. (입력받는 k_hold(4개)의 랜선 cm들을 이 리스트에 모두 넣음. 안쪽괄호는 append의미. 802 743 457 539로 각각 '4번'의 입력(바깥괄호.for문))

#print(lan_each_length) #[802, 743, 457, 539]

left = 1                            #각각 랜선의 길이가 1cm여야 하나(11개의 랜선을 만들기 위해)
right = max(lan_each_length_list)   #802cm여야 하나(11개의 랜선을 만들기 위해)

while left <= right: 
    mid = (left + right) // 2       #(1cm+802cm)//2 mid: 일단 401cm로 나눠봄.
    lines = 0 #랜선 수
    for i in lan_each_length_list:  #802 743 457 539
        lines += i // mid           #0 += 802cm//401cm(:mid)로 나눈 개수. // 각 k_hold를 for문돌면서 midcm로 나눈 개수들 더해줌.
        #print(lines)                #2 1 1 1 => 총 5
    #print(lines)    #5             #이 for문을 다 돌면 길이가 401cm(mid)인 랜선의 개수가 5개 나옴


    if lines >= N_need: #랜선의 개수가 분기점 #이 바로 윗 라인에서 나온 midcm로 나눈 lines의 개수가 지금은 5인데, 이게 N_need보다 같거나 크면, 더 긴 mid값으로 쪼개서 덜 N이 나오게 할 수 있으므로 왼쪽 기준값을 mid+1로 옮겨주기
        left = mid + 1
    else:               #lines < N_need 필요한 랜선의 개수보다 적게 되면, 더 잘게 쪼개야 하므로 우측 기준값을 mid값 아래쪽으로 바꿔주기
        right = mid - 1
print(right)    #?? 왜 print(left)하면 값이 한개 더 나오는지??!!


#참조: https://claude-u.tistory.com/443

#----------------------------------------------
# 
# K, N = map(int, input().split())
# N_list = [int(input()) for _ in range(K)]
# result = 0
# s, e = 1, max(N_list)
# while s <= e:
#     m = (s + e) // 2
#     key = sum([num // m for num in N_list])
#     if key < N: # => m의 값이 큰경우 => m을 줄이는 방향
#         e = m - 1
#     else:
#         s = m + 1
#         result = max(result, m) # 랜선의 최대 길이를 찾아야 하므로
# print(result)

# #참조: https://sinawi.tistory.com/272 & https://inspirit941.tistory.com/151
#위 방식 이해해보기

#---------------
#함수써서 작성법:https://velog.io/@wjdtmdgml/%EB%B0%B1%EC%A4%80%EB%9E%9C%EC%84%A0-%EC%9E%90%EB%A5%B4%EA%B8%B01654%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython%EC%9D%B4%EB%B6%84%ED%83%90%EC%83%89
