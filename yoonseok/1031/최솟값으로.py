TC = int(input())
for tc in range(1,TC+1):
    W, H, N = map(int,input().split())
    goals = list(list(map(int,input().split())) for i in range(N))
    answer = 0
    for i in range(N-1):
        start = goals[i]
        end = goals[i+1]
        if (start[0]<end[0] and start[1]<end[1]) or (start[0]>end[0] and start[1]>end[1]):
            max_dis = max(abs(start[1]-end[1]),abs(start[0]-end[0]))
            answer += max_dis
        else:
            answer += abs(start[0]-end[0])+abs(start[1]-end[1])
    print(f'#{tc} {answer}')