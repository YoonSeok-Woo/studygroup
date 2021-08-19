"""def solution(numbers, k):

    result = []
    answer = ''
    remove_count = k

    for n in numbers:
        while result and result[-1] and remove_count > 0:
            result.pop()
            remove_count -= 1
        result.append(n)    #while문을 끝낼 때.

    if remove_count != 0:
        return ''.join(result)"""

#----------------
"""def solution(number, k):
    lst = []

    for i, v in enumerate(number):
        while lst and lst[-1] < v and k > 0: #리스트와 리스트에서 맨 뒷자리수가 지금 비교할 i번째 자릿수의 v value보다 작고, k(지울 것이 아직 남아있으면)
            lst.pop()   #지워줌.
            k -= 1  #지워야할 것의 카운트도 하나 줄여줌

        if k == 0:
            lst.extend([x for x in number[i:]]) #더이상 지울 숫자가 남아있지 않다면, 나머지 숫자를 모두 리스트에 어펜드.
            break
        lst.append(v)
    
    list = """

#------------------
def solution(number, k):
    answer = ''
    temp = []
    #number 리스트의 에 있는 문자들을 정수로 바꾸어 temp 배열에 넣어줌.
    for i in range(len(number)):
        temp.append(str(number[i]))
        print(temp)


    number = '4177252841'



#참조: https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%83%90%EC%9A%95%EB%B2%95Greedy-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0
#참조: https://sexy-developer.tistory.com/45
