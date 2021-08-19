#DFS
memo = {}
def cres(n, ceil = 9):
    if n == 1:              #base case
        return ceil + 1
    else:
        answer = 0
        for i in range(ceil + 1):
            if (n - 1, i) not in memo:              #memoization
                memo[(n - 1, i)] = cres(n - 1, i)   #재귀. 마지막 숫자를 가정하고 가능한 n-1 길이의 숫자 개수 모두 구해서 더함
            answer += memo[(n - 1, i)]
        memo[(n, ceil)] = answer
        return answer

print(cres(int(input()))%10007)