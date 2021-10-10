def solution(s):
    answer = [0,0]
    while s!='1':
        answer[0]+=1
        answer[1]+=s.count('0')
        s = ''.join(s.split('0'))
        l = len(s)
        s = str(bin(l))[2:]
    #print(s)
    return answer