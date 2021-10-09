def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a = len(A)
    b = len(B)
    i = 0
    j = 0
    while i<a and j <b:
        if A[i] < B[j]:
            answer+=1
            i+=1
            j+=1
        else:
            j+=1
            
    return answer