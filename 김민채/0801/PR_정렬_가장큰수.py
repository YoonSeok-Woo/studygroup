def solution(numbers):
    str_num = list(map(str, numbers))
    str_num.sort(key=lambda x: x*3, reverse = True)
    answer = str(int(''.join(str_num)))
    
    return answer

# 마지막으로 시도한 풀이
from itertools import permutations

def solution(numbers):
    str_num = list(map(str, numbers))
    combis = list(permutations(str_num))
    new = []
    new = list(map(''.join, combis))
    answer = sorted(new, key=int, reverse=True)[0]
    return answer