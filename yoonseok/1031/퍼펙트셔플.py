TC = int(input())
for tc in range(1,TC+1):
    N = int(input())
    cards = list(input().split())
    if not N%2:
        left = cards[:N//2]
        right = cards[N//2:]
    else :
        left = cards[:N//2+1]
        right = cards[N//2+1:]
    print(f'#{tc}',end = ' ')
    #print(left,'\n', right)
    for i in range(N//2):
        print(f'{left[i]} {right[i]}', end = ' ')
    if N%2:
        print(left[N//2],end = ' ')
    print()