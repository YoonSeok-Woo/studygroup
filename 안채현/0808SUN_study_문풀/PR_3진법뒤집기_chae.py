def solution(n):
    answer = 0
       
    #user_input = int(input())  #함수이므로, 필요없는과정.
    #3진법 도출

    quotient = n    
    #remainder = 0
    remainder_list = []
    while quotient != 0:
        remainder_list.append((quotient%3))  
        quotient = quotient // 3
        #remainder = user_input % 3
        
    #print(remainder_list)   #[0, 0, 2, 1] #3진법 결과 앞뒤 반전.

    #리스트 뒤집기.
    reversed_list = remainder_list[::-1]
    #print(reversed_list)    #[1, 2, 0, 0]   #3진법 결과.

    #print(remainder_list)   #[0, 0, 2, 1] #3진법 결과 앞뒤 반전

    ten_result = 0
    # for i in remainder_list:    #0*3의세제곱 0*3의2제곱 2*3의 1제곱 1*3의 0제곱
    #     ten_result += 
    for i in range(len(reversed_list)):    #0*3의세제곱 0*3의2제곱 2*3의 1제곱 1*3의 0제곱  [1, 2, 0, 0]
        ten_result += 3**i*reversed_list[i]
    #print(ten_result)  #7
    answer = ten_result

    return answer

solution(45)

#테스트 통과





#-------------
#시도들



# def solution(n):
#     answer = 0
    
    
#     #user_input = int(input())  #함수이므로, 필요없는과정.
#     #3진법 도출

#     quotient = n    
#     #remainder = 0
#     remainder_list = []
#     while quotient != 0:
#         remainder_list.append((quotient%3))  #나중 join을 위해 인자들을 스트링으로 넣어주기 // c취소!!
#         quotient = quotient // 3
#         #remainder = user_input % 3
        
#     #print(remainder_list)   #['0', '0', '2', '1'] #3진법 결과 앞뒤 반전.

#     #리스트 뒤집기.
#     reversed_list = remainder_list[::-1]
#     #print(reversed_list)    #['1', '2', '0', '0']   #3진법 결과.

#     #print(remainder_list)   #['0', '0', '2', '1'] #3진법 결과 앞뒤 반전
#     #이제 이 21을 십진법으로 뽑기 위해, 먼저 join으로 빼주기..
#     # ten =''.join(remainder_list)
#     # print(ten)  #0021

#     ten_result = 0
#     # for i in remainder_list:    #0*3의세제곱 0*3의2제곱 2*3의 1제곱 1*3의 0제곱
#     #     ten_result += 
#     for i in range(len(reversed_list)):    #0*3의세제곱 0*3의2제곱 2*3의 1제곱 1*3의 0제곱  ['1', '2', '0', '0']
#         ten_result += 3**i*reversed_list[i]
#     #print(ten_result)  #7
#     answer = ten_result



#     return answer

# solution(45)

# #테스트 통과