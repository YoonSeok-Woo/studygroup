def solution(play_time, adv_time, logs):
    
    answer = ''
    H,M,S = map(int,play_time.split(':'))
    pt = H*3600+M*60+S
    watchers = [0]*(pt+1)
    H,M,S = map(int,adv_time.split(':'))
    at = H*3600+M*60+S
    nlogs = []
    for i in logs:
        H,M,S = map(int,i[:8].split(':'))
        start = H*3600+M*60+S
        H,M,S = map(int,i[9:].split(':'))
        end = H*3600+M*60+S
        watchers[start]+=1
        watchers[end]-=1
    for i in range(1,pt+1):
        watchers[i]+=watchers[i-1]
    time = 0
    for i in range(at):
        time +=watchers[i]
    ans = 0
    lt = time
    for i in range(pt-at+1):
        time-=watchers[i]
        time+=watchers[i+at]
        if time > lt:
            ans = i+1
            lt = time
    
    aH = ans//3600
    aM = (ans%3600)//60
    aS = ans%60
    if aH<10:
        ansH='0'+str(aH)
    else:
        ansH = str(aH)
    if aM<10:
        ansM='0'+str(aM)
    else:
        ansM = str(aM)
    if aS<10:
        ansS='0'+str(aS)
    else:
        ansS =str(aS)
    answer = ansH+':' + ansM+':'+ansS
    return answer

#https://dev-note-97.tistory.com/156 참고