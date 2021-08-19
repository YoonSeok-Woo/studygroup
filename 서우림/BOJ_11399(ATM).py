

N = int(input())
total = 0
result = 0
time = map(int, input().split())
sort_list = sorted(time)
for i in sort_list:
    total += i
    i = total
    result += i
print(result)