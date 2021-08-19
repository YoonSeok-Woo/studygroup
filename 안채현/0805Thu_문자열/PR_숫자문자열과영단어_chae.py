#딕셔너리 형태로 한번 더!! 
"""def solution(s):
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    answer = s

    for k, v in num_dict.items():
        if k in s:
            s.replace(k, str(v))
    print(s)

    
    return answer

solution('one4seveneight')
    
"""
""""
one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123
"""

#-------------------
#atpt2 : 리스트 형식으로 풀어보기

"""def solution(s):
    #num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    pre_answer = s

    for str_num in num_list1:
        #print(str_num in s) #False True False False False False False True True False
            index_in_num_list1 = num_list1.index(str_num)
            a = s.replace(str_num, str(num_list2[index_in_num_list1]))  
            pre_answer = a
            print(a)    #one4seveneight 14seveneight one4seveneight one4seveneight one4seveneight one4seveneight one4seveneight one47eight one4seven8 one4seveneight

    
    return answer

solution('one4seveneight')"""
#------------------------------------
#atpt3:
#틀린 이유2: 숫자로 바뀐 값이 나오면(a), 그 값을 pre_answer에 재 할당해서 for문 다시 돌려줌// 원본 s를 for문에 쓰지 않고. 이 s는 계속 갱신되게끔 
def solution(s):
    #num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = 0
    pre_answer = s

    for str_num in num_list1:   #one4seveneight  #['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        #print(str_num in s) #False True False False False False False True True False
        if str_num not in pre_answer:    #위 값이 False인 경우에는 그냥 지나감.
            pass
        else:
            index_in_num_list1 = num_list1.index(str_num)
            a = pre_answer.replace(str_num, str(num_list2[index_in_num_list1]))  ##딕셔너리처럼 풀지 않고, 바로 자릿수 받아서 int를 str으로 바꿔서 넣으면 될 것!
            pre_answer = a      #a를 pre_answer에 재할당 (s에서 교체)
            #print(a)    #14seveneight one47eight one4seven8 

    #print(pre_answer)   #값 확인용! 1478
    answer = int(pre_answer)
    #print(answer)   #최종 값 확인용!    1478    234567  234567  123
    return answer

solution('one4seveneight')
solution('23four5six7')
solution('2three45sixseven')
solution('123')

#틀린 이유1: .replace()는 원본 값을 변경하지 않는 것 같음. 새로운 변수(b)에 지정해주고 프린트하면 값나옴.
"""s = "one7eightten"
print("one" in s)   #True
print(s.replace('one', '0'))    #07eightten

print(s)    #one7eightten


b = s.replace('one', '0')
print(b)    #07eightten"""