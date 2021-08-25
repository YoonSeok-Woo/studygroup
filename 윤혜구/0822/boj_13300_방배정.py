N, K= map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
room = 0
match = [[0] * 7 for _ in range(2)]     #[[여자학년], [남자학년]]

for sex, grade in students:         #성별, 학년별로 배정
    match[sex][grade] += 1
    if match[sex][grade] >= K:      #만약 한 방의 최대인원이면
        room += 1                   #새로운 방
        match[sex][grade] = 0

for m in match:                     #최대인원보다 적은 방들 다 더해주기
    for x in m:
        if x > 0:
            room += 1

print(room)