from functools import cmp_to_key
def compare(a,b):
    A = a+b
    B = b+a
    if a+b<b+a:
        return -1
    elif a+b==b+a:
        return 0
    else:
        return 1
def solution(numbers):
    answer = ''
    str_nums = list(map(str,numbers))
    new_nums = sorted(str_nums,key = cmp_to_key(compare),reverse = True)
    #print(new_nums)
    for i in new_nums:
        answer+=i
    answer = str(int(answer))
    return answer