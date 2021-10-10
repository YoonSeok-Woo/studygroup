from itertools import permutations
def solution(expression):
    answer = 0
    opers = ['*','+','-']
    orders = list(permutations(opers,3))
    l = len(expression)
    nums = []
    oper = []
    temp = ''
    for i in range(l):
        if expression[i]=='-' or expression[i]=='+' or expression[i]=='*':
            nums.append(int(temp))
            oper.append(expression[i])
            temp = ''
        else:
            temp+=expression[i]
    nums.append(int(temp))
    for i in orders:
        tnums = nums[:]
        toper = oper[:]
        for j in i :
            tl = len(toper)
            k = 0
            while k < tl:
                if toper[k] == j:
                    res =0
                    if toper[k] == '-':
                        res = tnums[k]-tnums[k+1]
                    if toper[k] == '*':
                        res = tnums[k]*tnums[k+1]
                    if toper[k] == '+':
                        res = tnums[k]+tnums[k+1]
                    tnums.pop(k)
                    toper.pop(k)
                    tnums[k]=res
                    #print(res)
                    tl-=1
                    
                else:
                    k+=1
        #print(tnums)
        if abs(tnums[0])>answer:
            answer= abs(tnums[0])
    return answer