N = int(input())
sour = []
bit = []
for i in range(N):
    s, b = map(int,input().split())
    sour.append(s)
    bit.append(b)
ss = 1
bb = 0
answer = 987654321
def dfs(used):
    global answer
    global ss
    global bb
    if used >=N:
        if ss != 1 or bb !=0:
            answer = min(answer, abs(ss-bb))
        return
    ss*=sour[used]
    bb+=bit[used]
    dfs(used+1)
    ss//=sour[used]
    bb-=bit[used]
    dfs(used+1)
dfs(0)
print(answer)