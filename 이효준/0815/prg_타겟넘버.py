# https://eda-ai-lab.tistory.com/475
def dfs(arr, num, target, size):
    answer = 0
    if len(arr) == size:
        if sum(arr) == target:
            return 1
        else:
            return 0
    else:
        A = num.pop(0)
        for i in [1, -1]:
            arr.append(A * i)
            answer += dfs(arr, num, target, size)
            arr.pop()
        num.append(A)
        return answer


def solution(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))

    return answer
