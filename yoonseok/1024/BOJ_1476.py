E, S, M = map(int,input().split())

if E==15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
N = S
if N == 0:
    N+=28
while True:
    if N%15==E and N%19==M:
        break
    N +=28
print(N)