import math
from itertools import permutations
def p_check(num):
    point = math.sqrt(num)
    if num<=1:
        return False
    for i in range(2,int(num)):
        if num%i==0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    largest = ''.join(sorted(numbers,reverse = True))
    checked = [False]*(int(largest)+1)
    for i in range (1,len(numbers)+1):
        comb = list(map(''.join,permutations(numbers,i)))
        for j in comb:
            if checked[int(j)]:
                continue
            if p_check(int(j)):
                answer+=1
                checked[int(j)]=True
    return answer