def solution(numbers, target):
    if len(numbers) == 1:
        return 1 if numbers[0] == target or numbers[0] == -target else 0
    else:
        return solution(numbers[1:], target + numbers[0]) + solution(numbers[1:], target - numbers[0])