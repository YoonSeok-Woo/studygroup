from itertools import combinations

def solution(number, k):
    answer = ''
    num_list = list(str(number))

    a = (len(list(num_list))-k)
    all_list = list(combinations(list(num_list), a))


    result_list = []
    result = ''

    for i in all_list:
        for j in range(len(i)):
            result += i[j]
        result_list.append(result)
        result = ''

    answer = max(result_list)
    return answer


