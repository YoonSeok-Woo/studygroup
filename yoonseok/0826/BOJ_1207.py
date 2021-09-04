row, col = map(int,input().split()) #종이의 너비
N = int(input())#선 갯수
rline = [0]#가로선
cline = [0]#세로선
for i in range(N):
    rc, loc = map(int,input().split())
    if rc == 0:#가로선이면 가로선에 추가
        rline.append(loc)
    else:#세로선이면 세로선에 추가
        cline.append(loc)
cline.append(row)#row col
rline.append(col)
rline.sort()
cline.sort()
#print(rline)
#print(cline)
a = 0 #가로 최대값
b = 0 #세로 최대값
for i,num in enumerate(rline):
    if i == 0:
        continue
    if a< num-rline[i-1]:
        a = num-rline[i-1]
for i, num in enumerate(cline):
    if i ==0:
        continue
    if b < num-cline[i-1]:
        b = num-cline[i-1]
print(a*b)
