def solution(A,B):
    answer = 0
    s = len(A)
    A.sort()
    B.sort()
    while A and B:
        answer+= A.pop()*B.pop(0)
        if A and B:
            answer+= A.pop(0)*B.pop()
        
    return answer