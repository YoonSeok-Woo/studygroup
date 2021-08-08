
#--------------------------------------------------------
def solution(left, right):  #13 17
    answer = 0


    for num in range(left, right+1):    #range(13, 17) #13 14 15 16
        #sum_result = []
        num_list = []
        #right_num_list = []

#----------------윤석님 피드백: 두번째 for문에 range(1, right+1) 대신 range(1, num+1)으로 바꾸기 / 시간 덜 들 것 / 왜?? 
#리스트에 안넣고// 약수가 뭐가 들었는지 중요한지 않으니까 . . count만들어서 더함.!! / 리스트에 어펜드를 하는 것이 count에 덧셈보다 시간이 오래 걸릴 것.
#시간 단축을 위해서라도 이렇게 하는 것이 좋음!!
        for i in range(1, num+1): #range(1, 17)   left와 right를 각각 둘 중 더 큰수인(상관없을것) 1부터 17까지로 나눴을 때 나머지가 0이면 i가 left/right의 약수.
            if num%i == 0:
                num_list.append(i)
        if len(num_list)%2 == 0:
            answer += num
        else:
            answer -= num

    
        # for i in range(1, right+1):
        #     if right%i == 0:
        #         right_num_list.append(i)
        
    print(answer)
    return answer

solution(13, 17)
