#윤석님 탐색알고리즘 설명

#탐색해야 할 범위의 크기: N
#들어가는 시간 O(N)
#9 3 1 2 5 6 2 10 8 7
#in 시간을 많이 잡아먹는다
#in iterable의 크기만큼 전부 뒤져봐야돼서
#O(logN) 이붙남색 알고리즘
#탐색범위가 정렬되어 있어야 함.
#1 2 3 4 5 6 7 8 9 10
#탐색범위가 크고 정렬되어 있으면 엄청 효과적

#while l <= r:

#list[mid] > traget
#l = mid+1

#list[mid] < target
#r = mid-1

#---------------------------------
#윤석님 설명
N = int(input())    #5
N_list = list(map(int, input().split()))    #4 1 5 2 3
N_list.sort()                               #1 2 3 4 5  #1. 탐색할  리스트 전체를 정렬 /2. l과 r의 기준점을 이 리스트(N)을 기준으로 잡음

M_needless = int(input())    #5 #사실상 문제푸는데 필요없는. 왜냐. 이개수만큼 M 리스트의 인자개수이므로
M_list = list(map(int, input().split()))    #1 3 7 9 5

for m in M_list:    #M_list의 인자 하나 하나 1 3 7 9 5 가 N_list에 있나 볼 것.
    l = 0
    r = N-1    #N리스트 내 자리수 기준이므로 .

    while l <= r:
        mid = (l+r)//2  #자릿수이므로 몫으로 딱 떨어지게 int로 값이 나오도록. / mid값은 while을 돌 때마다 갱신되야하므로 이부분.
                        #이 mid의 위치??! 왜 여기? 위 l과 r과 함께가 아니라?
        if N_list[mid] == m:  #리스트의 인자들끼리 비교
            print(1)
            break
        elif N_list[mid] < m:
            l = mid + 1
        
        else:           # N_list[mid] > m:
            r = mid - 1

    else:
        print(0)