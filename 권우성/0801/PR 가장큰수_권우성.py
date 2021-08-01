# 소수찾기 -못품
# 1
def gen_permutations(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i, elem in enumerate(arr):
        for P in gen_permutations(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + P]
    return result


def collect(arr):
    result_arr = []
    for i in arr:
        if "".join(i) not in result_arr:
            result_arr.append("".join(i))
    return result_arr


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    list_chars = []

    # 순열구하기
    for i in range(1, len(numbers) + 1):
        list_chars += gen_permutations(numbers, i)

    # 각 요소 합치기
    collect_chars = collect(list_chars)

    # 숫자로 바꾸기
    list_numbers = list(map(int, collect_chars))

    # 중복제거
    set_numbers = set(list_numbers)

    # 소수판별
    for i in set_numbers:
        if is_prime_number(i):
            answer += 1

    return answer


# 2

from itertools import permutations


def solution(numbers):
    answer, new, new2 = [], [], []
    for k in range(1, len(numbers) + 1):

        for i in list(permutations(numbers, k)):
            num = "".join(list(i))
            new.append(num)

    new = list(set(new))
    for i in new:
        if int(i) == 1 or int(i) == 0:
            continue
        new2.append(int(i))

    new2 = list(set(new2))

    def prime_num(n):
        if n != 1:
            for i in range(2, n):
                if n % i == 0:
                    return False
        else:
            return False
        return True

    for i in new2:
        if prime_num(int(i)):
            answer.append(i)

    return len(answer)