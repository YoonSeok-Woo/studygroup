def solution(number, k):
    answer = number
    l = len(number)

    count = 0
    i = 0
    while i < len(answer)-1:
        if k-count >=len(answer):
            answer = []
            break
        if answer[i]<answer[i+1]:
            answer = answer[:i]+answer[i+1:]
            if i>0:
                i-=1
            count+=1
        else:
            i+=1
        if count==k:
            break;
    if count < k:
        l = len(answer)
        rem = k-count
        answer = answer[:l-rem]
    return answer