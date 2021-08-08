#블루레이에는 총 N개의 레슨이 들어가는데, 블루레이를 녹화할 때, 레슨의 순서가 바뀌면 안 된다. 
#즉, i번 레슨과 j번 레슨을 같은 블루레이에 녹화하려면 i와 j 사이의 모든 레슨도 같은 블루레이에 녹화해야 한다.
# 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다.
#고민 끝에 강토는 M개의 블루레이에 모든 기타 레슨 동영상을 녹화하기로 했다.
#이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

#강토의 각 레슨의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

#첫째 줄에 레슨의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다. 
#다음 줄에는 강토의 기타 레슨의 길이가 레슨 순서대로 분 단위로(자연수)로 주어진다.

# 9 3   9개의 레슨, 3개의 같은 길이의 블루레이에 모두 담고싶음
# 1 2 3 4 5 6 7 8 9         9개 레슨 각각의 영상시간.

#첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.

#----------------
# 레슨은 총 9개이고, 블루레이는 총 3개 가지고 있다.

# 1번 블루레이에 1, 2, 3, 4, 5, 2번 블루레이에 6, 7, 3번 블루레이에 8, 9 를 넣으면 
# 각 블루레이의 길이는 15, 13, 17이 된다. 블루레이의 길이는 모두 같아야 하기 때문에, 
# 블루레이의 길이는 17이 된다. 17보다 더 작은 길이를 가지는 블루레이를 만들 수 없다.  ??????????왜 블루레이의 길이는 17?
import sys
input=sys.stdin.readline    #??사용법
from collections import deque   #??사용법

n,m=map(int,input().split())

lessons_each_lengh_list=list(map(int,input().split()))  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lesson)
left = max(lessons_each_lengh_list)
right = sum(lessons_each_lengh_list)
ans=sys.maxsize         #??사용법
while left <= right:
    mid=(left+right)//2
    cnt=0
    sum=0
    for i in range(len(lessons_each_lengh_list)):
        if sum+lessons_each_lengh_list[i]>mid:
            cnt+=1
            sum=0
        sum+=lessons_each_lengh_list[i]
    if sum:
        cnt+=1

    if cnt>m: # 블루레이 개수가 m보다 커 (각 크기가 작음)
        left=mid+1
    else:
        ans=min(ans,mid)
        right=mid-1
print(ans)

#참조: https://haerang94.tistory.com/144
# l=min(lesson)으로 해줬었는데 그러면 기준 크기 mid보다 각 음악의 길이가 더 클 때 문제가 된다. 

# 따라서 l=max(lesson)으로 해줘서 최소 한 블루레이 크기에 한 음악은 들어갈 수 있도록 해줘야한다. 

#-------------------
#다른 방식: 참조: https://deok2kim.tistory.com/109









