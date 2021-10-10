def check(st):
    stack = []
    for i in st:
        if not stack and i == '(':
            stack.append(i)
        elif not stack and i == ')':
            return False
        elif stack[-1]=='(' and i==')':
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True

def func(st):
    if not st:
        return st
    l = 0
    r = 0
    ls = len(st)
    if st[0]=='(':
        l+=1
    elif st[0]==')':
        r+=1
    for i in range(1,ls):
        if st[i]=='(':
            l+=1
        if st[i]==')':
            r+=1
        if l==r:
            u = st[:i+1]
            v = st[i+1:]
            break
    if check(u):
        return u+func(v)
    temp = ''
    temp +='('
    temp+=func(v)
    temp+=')'
    tempu = u[1:-1]
    for i in tempu:
        if i==')':
            temp+='('
        else:
            temp+=')'
    return temp
def solution(p):
    answer = ''
    if check(p):
        return p
    answer = func(p)
    
    return answer