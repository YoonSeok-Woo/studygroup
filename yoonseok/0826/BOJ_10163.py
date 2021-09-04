N = int(input())
board = [[-1]*1001 for i in range(1001)]#1001사이즈 초기화를 해줬고 N개의 인풋이 들어오는데 각각 인덱스를 종이 넘버로 볼려고 첫 종이가 0번이라
nop = [0]*N #각 종이의 갯수
for k in range(N):
    x1,y1,x2,y2 = map(int,input().split())#인풋을 받고
    for i in range(y1,y1+y2):#각 종이의 범위만큼 for문을 전부 돌면서
        for j in range(x1,x1+x2):
            if board[i][j]!=-1:#-1이면 빈공간이니까 -1이 아닐때에만(다른종이가 붙어있는 경우에만)
                nop[board[i][j]]-=1#그 다른종이의 칸수를 하나씩 빼줍니다.
            nop[k]+=1 #종이 한칸 늘어날때마다 종이 칸수를 하나씩 더해주고
            board[i][j]=k#그 종이가 맨위에 있따는걸 표시해주는 겁니다.
for i in range(N):
    print(nop[i]) #nop그대로 출력하면 끝