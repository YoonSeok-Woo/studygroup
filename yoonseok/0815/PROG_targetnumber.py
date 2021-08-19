count = 0
def dfs(numbers,i,now,target):
    global count
    if i == len(numbers):
        return
    if numbers[i]+now==target and i==len(numbers)-1:
        count+=1
        return
    if now-numbers[i]==target and i==len(numbers)-1:
        count+=1
        return
    dfs(numbers,i+1,now+numbers[i],target)
    dfs(numbers,i+1,now-numbers[i],target)
def solution(numbers, target):
    answer = 0
    global count
    dfs(numbers,0,0,target)
    answer = count
    return answer