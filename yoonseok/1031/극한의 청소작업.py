TC = int(input())

def remove4(num):
    t_res = []
    while num>0:
        temp = num%10
        if temp > 4:
            temp -=1
        t_res.append(temp)
        num = num//10
    res = 0
    while t_res:
        res*=9
        res += t_res.pop()

    return res

for tc in range(1,TC+1):
    A, B = map(int,input().split())
    answer = 0
    if A<0 and B>0:
        answer = remove4(abs(A))+remove4(abs(B))-1
    elif A > 0 and B > 0:
        answer = remove4(abs(B))-remove4(abs(A))
    else:
        answer = remove4(abs(A))-remove4(abs(B))
    print(f'#{tc} {answer}')