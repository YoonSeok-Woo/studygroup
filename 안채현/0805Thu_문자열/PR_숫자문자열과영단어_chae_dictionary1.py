"""num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def solution(s):
    answer = s

    for key, value in num_dict.items():
        answer = answer.replace(key, value)     #TypeError: replace() argument 2 must be str, not 
int

    return int(answer)
"""
#틀린 이유: TypeError: replace() argument 2 must be str, not int

"""num_dict = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s      #??
    for key, value in num_dict.items():
        answer = answer.replace(key, value)
    #print(int(answer)) 1478  234567  234567  123
    return int(answer)



solution('one4seveneight')
solution('23four5six7')
solution('2three45sixseven')
solution('123')"""

