def solution(absolutes, signs):
    answer = 123456789
    
    answer = 0  #왜 위의 answer이 123456789 / 의미 없음. 이거 그냥 지우고 하기 / return에 answer사실 안써도 됨! 함수있는내용 싹다지우고 다시 써도 되고! /중요하지 않음!

    for i in range(len(absolutes)):   #[4,7,12] 0 1 2 자릿수
        #for bool in signs:  #[True,False,True]
        if signs[i] == True:
            answer += absolutes[i]

        else:
            answer -= absolutes[i]

       
    return answer




solution([4,7,12], [True,False,True])       #bool로 입력받는다고 했으므로! True False이런식으로 써주기
solution([1,2,3], [False,False,True])          #???질문? 이걸 소문자로 쓰면 노란줄로 뜬느 이유? 그냥 돌려도 되는것인가? //이유는 문제가 c같은경우는 소문자로 줘도 변수로 들어가는데 파이썬은 이 경우에 true false를 대문자로 바꿔줘야 함.


    #absolute: 정수배열(정수들의 절댓값)
    #signs(정수의 부호들)
    #실제 정수들의 합을구하기.

#테스트 결과: 성공