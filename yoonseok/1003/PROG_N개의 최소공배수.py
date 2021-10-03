def get_lcm(a,b):
    gcd = 1
    for i in range(2,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd = i
    return a*b//gcd
def solution(arr):
    answer = 0
    l = len(arr)
    temp = get_lcm(arr[0],arr[1])
    for i in range(1,l-1):
        #print(temp,arr[i+1])
        temp = get_lcm(temp,arr[i+1])
    return temp