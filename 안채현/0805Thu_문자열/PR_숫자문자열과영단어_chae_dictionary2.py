num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

def solution(s):
    answer = s      #초기값 s로 시작// for문 돌면서 answer을 answer.replace(key, str(value))로 갱신해감. 

    for key, value in num_dict.items():
        answer = answer.replace(key, str(value))     #TypeError: replace() argument 2 must be str, not int
    print(int(answer))                               #딕셔너리는 있으면 찾아서 '다' 바꿔라.. 이런 느낌인가.! / (순서 이런거 없이..?)
    return int(answer)

solution('one4seveneight')
solution('23four5six7')
solution('2three45sixseven')
solution('123')

#틀린 이유: TypeError: replace() argument 2 must be str, not int
#해결: 딕셔너리 value자체를 모두 ''씌워주거나 .replace()에서 value에 str씌워주기
