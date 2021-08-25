#내 풀이
#무조건 1000번 돌아야 함
N, L = map(int, input().split())
broken = list(map(int, input().split()))
pipe = [0] * 1001   #전체 파이프

for point in broken:    #파이프에 물이 새는 위치 표시
    pipe[point] = 1

tapes = 0
this_tape = 0
for i in range(1001):
    if pipe[i] == 1:  #테이프를 붙여야 하면
        if this_tape == 0:    #남은 테이프가 없으면 새로 붙여줌
            tapes += 1
            this_tape = L
    if this_tape > 0:     #남은 테이프 길이 줄어듦
        this_tape -= 1

print(tapes)


# #다른 사람 풀이 참고해서 다른 풀이
# #원리는 비슷하지만 배열 사용x
# #https://www.acmicpc.net/source/32218113
# N, L = map(int, input().split())
# broken = list(map(int, input().split()))
# broken.sort()

# tapes = 1
# this_tape = broken[0] + L - 0.5
# for b in broken:
#     if this_tape < b:
#         tapes += 1
#         this_tape = b + L - 0.5

# print(tapes)