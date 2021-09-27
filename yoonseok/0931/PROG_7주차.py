def solution(enter, leave):
    
    n = len(enter)
    answer = [0]*n
    li = 0
    stack = []
    for i in range(n):
        for num in stack:
            answer[num-1]+=1
        answer[enter[i]-1]+=len(stack)
        stack.append(enter[i])
        
        while stack and leave[0] in stack:
            stack.pop(stack.index(leave[0]))
            leave.pop(0)
        #print(answer, leave, stack)
            
    return answer