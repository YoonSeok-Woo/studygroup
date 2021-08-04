T = int(input())    #3


input_list = []
for i in range(T):      #T번만큼 i돌려주면서 빈 인풋리스트에 값 쌓아두기! (여러 줄의 인풋을 받을 때!)
                        #range(3): 0 1 2
    input_list.append(input())

#print(input_list)   #['happy', 'new', 'year']

#letter_list = []   #letter_list는 여기에 위치하는 것이 아님.
group_word_count = 0
for word in input_list:
#    print(word) #happy  new  year
    
    #이 위치에 letter_list가 들어가줘야할 것 같은데..!
    letter_list = []
    for loc in range(len(word)):    #happy면, range(5): loc : 0 1 2 3 4
        #print(loc)  #0 1 2 3 4
        if loc == len(word)-1:  #즉. 마지막 레터, y는 loc이 4, 즉 len(happy)=5에 1을 뺀 값!
            letter_list.append(word[loc])   #앞에거랑 달랐으면 다르니 이것도 들어가는 게 맞고, 같았으면 앞에건 안들어갔으니 지금 넣어주면 중복 없음.
                    #여기 break넣어줘야 하나?
        else:       #즉 마지막 레터가 아니면
            if word[loc] != word[loc+1]:    #앞-뒤가 다를 경우에만
                letter_list.append(word[loc])   #앞 글자는 리스트에 추가해줌.
#여기까지 돌았을 때, 각 단어에 대한 letter_list가 나오는걸까? 아닌데..!
#letter_list는 happy new year모든 레터에 대한 리스트가 아니라, happy이 하나씩에 대한 리스트가 나와줘야 함. 리셋되기 전에 다른 리스트 뽑아내줘야.
#첫번째 for문이 끝날 부분에는 count가 들어가야 할 것!(group_word_count)

    #print(letter_list)  #한 happy돌고나서 레터리스트 나와줘야하므로 이 위치가 아마 맞을 것! ['h', 'a', 'p', 'y']
                        #['h', 'a', 'p', 'y']

    #이제 이 letter_list가 나와준 위치에서 이 리스트 안에 중복값이 있다면 그룹단어가 아니고, 중복값이 없어야 그룹단어임.
    if len(letter_list) == len(list(set(letter_list))):
        group_word_count += 1

print(group_word_count)




#확인할 점: T 인풋 개수만큼 인풋을 여러개 받고, 쌓아놨다가 한번에 출력함.
#연속단어 문제가 어디 있었는데..! hwk인가 wks인가. 다르면 앞에거 넣어주고.!
#확인할 점 2: 프린트로 한번에 값을 출력하는 법.! / 모든 for문이 다 돌고 나오는 경우(여기서는 group_word_count)이므로 정의/출력위치를 처음으로 맞춰주기 





