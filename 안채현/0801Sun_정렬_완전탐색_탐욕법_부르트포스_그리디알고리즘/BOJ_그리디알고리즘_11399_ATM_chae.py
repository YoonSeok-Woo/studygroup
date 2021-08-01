#https://www.acmicpc.net/problem/11399

n = int(input())    #사람 수
arrange = list(map(int, input().split()))   #각 사람 별 인출시간
arrange.sort()  #인출시간 짧은 순서로 정렬
#print(arrange)  #[1, 2, 3, 3, 4]

for i in range(1, n): #사람 수가 5명이면 i : 1 2 3 4
    arrange[i] += arrange[i-1]    #arrange[1] = arrange[1] + arrange[0] // arrange[1] = 1+2  >> new arrange = [1, 3V, 3, 3, 4]
                                    #arrange[2] = arrange[2] + arrange[1] // arrange[2] = 3+3V >> new arrange = [1, 3V, 6V, 3, 4]
                                    #arrange[3] = arrange[3] + arrange[2] // arrange[3] = 3+6V >> new arrange = [1, 3V, 6V, 9V, 4]
                                    #arrange[4] = arrange[4] + arrange[3] // arrange[4] = 4+9V >> new arrange = [1, 3V, 6V, 9V, 13V]
print(sum(arrange))


#참조: https://deep-learning-study.tistory.com/629