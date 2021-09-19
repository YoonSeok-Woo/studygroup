def solution(enroll, referral, seller, amount):
    answer = []
    money = {}
    con = {}
    for i in enroll:
        money[i]=0
        con[i] = '-'
    
    l = len(enroll)
    for i in range(l):
        if referral[i]=='-':
            continue
        con[enroll[i]] = referral[i]
    
    
    for i, name in enumerate(seller):
        money[name]+=amount[i]*90
        receive = con[name]
        sdmoney = amount[i]*10
        while sdmoney>0:
            if receive=='-':
                break
            tsend = sdmoney//10
            money[receive]+=sdmoney-tsend
            sdmoney = tsend
            receive = con[receive]
    for i in enroll:
        answer.append(money[i])
    return answer