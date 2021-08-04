
#atpt3
user_input = input()

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alpha_list = []
count = 0
for alph in cro_alpha:  
    #1. if alph가 dz=인 경우, 굳이 이렇게 안해도 되겠는게.. 
    if alph in user_input:  #alph: dz= // user_input: dz=dz=dz=
        a = user_input.count(alph)
        #print(a)    #3
        count += a  ##여기서 dz=인 경우 조정하지 말고, 마지막에 count에서 user_input.count('dz=') 한 것을 빼주기
        # alpha_list.append(alph)
        # count += 1
#print(count)    #6이 나옴(dz=가 3번 카운트, z=가 3번 카운트 --> 즉, 중복카운트)
count -= user_input.count('dz=')        #dz=가 카운트된만큼 기존 count에서 빼서 count값 재할당.
#print(count)

#이제 카운트가 나왔으니..! // 이 다음에는 for문 돌면서 제거도 가능할 것.
#  크로아티아 문자들을 다 원본 스트링에서 제거해줘야 함.
#그 뒤에 제거완료된 문자의 .len을 세면 그게 일반 알파벳
#일반알파벳을 count에 더해서 count값을 재할당한후, print.하면 답이 나올 것 같다.

for alph in cro_alpha:
    # while user_input.count(alph) > 0:       #??? 질문! 왜 여기 while을 쓰면 답이 나오지 않는 것일까요..!
    user_input = user_input.replace(alph, '*')   #값을 재할당.

#print(user_input)   #모든 크로아티아 문자가 제거된 순수 알파벳만 나옴.

count = count + len(user_input) - user_input.count('*')   #순수 알파벳 개수를 더하여 count에 재할당.

print(count)    #정답일 것!

#---------------------------------------------------------------------------------------------------------------
# dz= 이랑 z= 주의하기 
# 만약 input문자열에 dz= 가 있으면 dz=가 카운트된 개수마다 z=도 카운트되었을것이므로, user_input.count('dz=') 개수만큼 count에서 빼주기


#틀린 이유1: 크로아티아 알파벳리스트를 기준으로 인풋에 있나없나만 확인하니까, dz=가 3개나 있어도 한개만 카운트 됨.
"""dz=dz=dz=
['dz=', 'z=']
2"""
#해결책: 크로아티아 알파벳리스트를 for문으로 돌려서 'count'를 세어야 할 듯,
#단, 'dz='가 있던 개수만큼 z=도 중복카운트되었을것이므로 dz=개수만큼 count에서 빼줌
#남은 z=가 카운트된 개수는 순수 z=일 것이기 때문에, 이 경우에는 조정필요x (ex sz=f)


#틀린 이유2: remove로 스트링을 제거하려하면 안됨.
# AttributeError: 'str' object has no attribute 'remove'
"""
for alph in cro_alpha:
    while user_input.count(alph) > 0:
        user_input.remove(alph)     #이부분 이렇게 처리 못함. alph는 스트링이고 user_input도 스트링

    print(user_input)"""

#해결책: alph문자를 replace해서 ''공백으로 바꿔보자.
#https://www.journaldev.com/23674/python-remove-character-from-string


#틀린 이유 3: 여기서 nljj가 복병이었다.. lj가 나와서 먼저 삭제하면. nj가 남으니까 이게 n<-->j 로 별개인 문자열인데도 카운트되어버리는구나..!
#해결책... 아무 의미 없는 '-'로 replace를 해야하나..! / 그래서 리스트에 남은 요소들을 모두 어펜드해서 len(list)-len('-')하면 답이 나올까..?


#틀린 이유 4: 처음에 '*' 대신 '-'로 바꿨었는데 여기서는 ddz=z=가 복병이었다.. dz= 나와서 먼저 삭제하면. d-z= 가 남는데 여기서 d-도 하나의 크로아티아문자열..!이어서 같이 삭제되어버림(일반 알파벳만 뽑아내는것을 의도했는데도)
#해결책... 아무 의미 없는 '*'로 replace를 해야..! / 그래서 리스트에 남은 요소들을 모두 어펜드해서 len(list)-len('*')하면 답이 나올까..? //
#문제 잘 보기!
