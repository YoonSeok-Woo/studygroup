N = int(input())
dice = list(list(map(int,input().split())) for i in range(N))#여기까진 인풋을 받는과정
def find_top(i):#i가 바닥인데 바닥의 인덱스를 받으면 위로 오는 부분의 인덱스를 반환하는 함수
    if i == 0:
        return 5
    if i == 1:
        return 3
    if i == 2:
        return 4
    if i == 3:
        return 1
    if i == 4:
        return 2
    if i == 5:
        return 0
ans = 0
for bottom in range(6):#바닥이 하나가 정해지면 나머진 다 정해져있는 경우기 때문에 첫 주사위의 각 면을 바닥으로 하고 그 떄의 결과들을 비교해서 최대값을 찾는 부분
    top = find_top(bottom) #1번주사위의 꼭대기 면
    top_num = dice[0][top] #1번주사위의 꼭대기 숫자가 2번주사위의 꼭대기 숫자와 같아야하니까
    smaller = min(top,bottom) #바닥과 꼭대기 중에서 더 작은 인덱스 값을 가지는거
    larger = max(top,bottom) #더 큰 인덱스 가지는거죠
    temp = max(dice[0][:smaller]+dice[0][smaller+1:larger]+dice[0][larger+1:])#옆면의 최대값을 찾습니다.
    for i in range(1,N): #0번주사위는 했으니까 1번주사위부터 N-1번주사위까지 올라가면서 옆면의 최대값을 찾아서 temp에 더해줍니다.
        for k in range(6):
            if dice[i][k] == top_num:#바로 아래있는 주사위의 윗면 값이랑 같은 면을 찾아서 바닥에 둡니다.
                nb = k#nb-> nowbottom
                break

        top = find_top(nb)#꼭대기로 갈 면을 찾고
        top_num = dice[i][top]# 새로운 꼭대기를 업데이트
        smaller = min(top, nb)
        larger = max(top, nb)
        temp += max(dice[i][:smaller] + dice[i][smaller + 1:larger] + dice[i][larger + 1:])#i번쨰 주사위의 옆면중 가장 큰값
    if temp>ans:#모든 주사위를 다 쌓고 옆면의 최대값을더해준 값이 현재까지의 최대값보다 크다면
        ans = temp#갱신
print(ans)
