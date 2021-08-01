def solution(answers):
    answer = []
    psn1 = [1, 2 ,3 ,4 ,5]
    psn2 = [2, 1, 2, 3, 2, 4, 2, 5]
    psn3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len1 = len(psn1)    #5
    len2 = len(psn2)    #8
    len3 = len(psn3)    #10
    
    score1 = 0
    score2 = 0
    score3 = 0
#IndexError: list index out of range??
    for i in range(len(answers)): #제공된 answers의 개수. i: range(5) >> i: 0 1 2 3 4
        #print(i)   #0 1 2 3 4
        if psn1[i%len1] == answer[i]:   #i:0 > psn1[0] == answer[0] // i:1 > psn1[1] == answer[1]
            score1 += 1
        if psn2[i%len2] == answer[i]:   #i:0 > psn2[0] == answer[0] // i:1 > psn2[1] == answer[1] //i:7 > psn2[7을 psn2 len인 8로 나눈 나머지, 7번째자리값과 
            score2 += 1
        if psn3[i%len3] == answer[i]:   #i:0 > psn1[0] == answer[0] // i:1 > psn1[1] == answer[1]
            score3 += 1

    max_score = max(score1, score2, score3)

    if max_score == score1:
        answer.append(1)
    if max_score == score2:
        answer.append(2)
    if max_score == score3:
        answer.append(3)

    answer = sorted(answer)

    print(answer)
    return answer


solution([1, 2, 3, 4, 5])
# print(solution([1, 3, 2, 4, 2]))

#참조: https://velog.io/@younge/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89
#참조: https://somjang.tistory.com/entry/Programmers-%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC-Python