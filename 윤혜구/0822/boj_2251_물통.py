#BFS
#중복을 막고 탐색시간 줄이려고 set를 썼는데
#set와 list를 자꾸 형변환하는 과정이 많아서 오히려 깨끗하지 않은 코드인 것 같음
from collections import deque
                
A, B, C = map(int, input().split())
full = [A, B, C]
found = set()
queue = deque()
queue.append((0, 0, C))
while queue:
    water = queue.popleft()
    found.add(water)
    for i in range(3):  #i물통에서 j물통으로 물 옮기기
        if water[i] == 0:
            continue
        for j in range(3):
            temp = list(water)
            if i == j:
                continue
            elif water[i] > full[j] - water[j]:     #다 옮길 수 없을 때
                temp[i], temp[j] = temp[i] - (full[j] - temp[j]), full[j]
            else:   #water[i] <= B - water[j]       #다 옮길 수 있을 때
                temp[i], temp[j] = 0, temp[j] + temp[i]
            if tuple(temp) not in found:
                queue.append(tuple(temp))

found_map = map(str, sorted(map(lambda x: x[2], filter(lambda x: x[0] == 0, found))))
print(' '.join(found_map))


# #그냥 리스트로 통일해봄
# #더 오래걸림
# from collections import deque
#
# A, B, C = map(int, input().split())
# full = [A, B, C]
# found = []
# queue = deque()
# queue.append([0, 0, C])
# while queue:
#     water = queue.popleft()
#     found.append(water)
#     for i in range(3):  #i물통에서 j물통으로 물 옮기기
#         if water[i] == 0:
#             continue
#         for j in range(3):
#             temp = water[:]
#             if i == j:
#                 continue
#             elif water[i] > full[j] - water[j]:     #다 옮길 수 없을 때
#                 temp[i], temp[j] = temp[i] - (full[j] - temp[j]), full[j]
#             else:   #water[i] <= B - water[j]       #다 옮길 수 있을 때
#                 temp[i], temp[j] = 0, temp[j] + temp[i]
#             if temp not in found:
#                 queue.append(temp)
#
# found_map = map(str, sorted(list(set(map(lambda x: x[2], filter(lambda x: x[0] == 0, found))))))
# print(' '.join(found_map))


# #다른 사람 풀이
# #DFS 재귀
# #값을 문자열로 만들어서 딕셔너리 키로 사용하는 방식으로 품
# #https://www.acmicpc.net/source/24952749
# import sys
# input = sys.stdin.readline

# def trans(stat):
#     return stat[0] * (10**(B_n + C_n)) + stat[1] *(10**C_n) + stat[2]

# # stat = [A,B,C]
# def DFS(stat):
#     visited[trans(stat)] = 1
    
#     if stat[0] == 0:
#         ans.append(stat[2])
    
#     for i in range(3):
#         if stat[i] != 0:
#             for j in range(3):
#                 if i == j:
#                     continue
#                 if stat[j] != data[j]:
#                     tmp = stat.copy()
#                     if stat[i] <= (data[j]-stat[j]):
#                         tmp[i] = 0
#                         tmp[j] = stat[j] + stat[i]
#                     else:
#                         tmp[i] = stat[i] - (data[j]-stat[j])
#                         tmp[j] = data[j]
#                     if not visited.get(trans(tmp)):
#                         DFS(tmp)
                    
# data = input().split()
# A_n= len(data[0])
# B_n= len(data[1])
# C_n= len(data[2])
# data = list(map(int, data))
# ans = []
# visited = {}

# DFS([0, 0, data[2]])

# for el in sorted(ans):
#     print(el, end=" ")