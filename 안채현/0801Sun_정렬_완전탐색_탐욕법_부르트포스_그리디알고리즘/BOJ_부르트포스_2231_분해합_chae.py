n = int(input()) #245

result = 0
for i in range(1, n+1): #range(1, 246) : 1 2 3 4 ...245
    new_list = list(map(int, str(i)))   #ex str(245) 를 int로 뽑아오면 [2, 4, 5]
    #print(new_list)
    result = i + sum(new_list)  #result = 1+1   #result가 분해합. i + 각 자릿수 숫자의 합

    if result == n:     #i를 돌면서 만들어진 새로운 분해합이 == input(분해합)과 같으면
        print(i)        #i(생성자)를 출력
        break

    if i == n:          #i생성자 자체가 input(분해합)과 같으면 생성자가 따로 없으므로 0을 출력
        print(0)


#129같은 분해합의 입장에서 123같은 생성자를 구함
#참조: https://ywtechit.tistory.com/110
#폴더명에 ()넣으면 오류생김 #https://codefather.tech/blog/bash-syntax-error-near-unexpected-token/
#?? 생성자가 여러개이면? 어떻게 최소 생성자를 뽑아내나..//아아 print(i)로 생성자들 구해질 때마다 다 출력되겠다.


#print(new_list)
"""[1]
[2]
[3]
[4]
[5]
[6]
[7]
[8]
[9]
[1, 0]
[1, 1]
[1, 2]
[1, 3]
[1, 4]
[1, 5]
[1, 6]
[1, 7]
[1, 8]
[1, 9]
[2, 0]
[2, 1]
[2, 2]
[2, 3]
[2, 4]
[2, 5]
[2, 6]
[2, 7]
[2, 8]
[2, 9]
[3, 0]
[3, 1]
[3, 2]
[3, 3]
[3, 4]
[3, 5]
[3, 6]
[3, 7]
[3, 8]
[3, 9]
[4, 0]
[4, 1]
[4, 2]
[4, 3]
[4, 4]
[4, 5]
[4, 6]
[4, 7]
[4, 8]
[4, 9]
[5, 0]
[5, 1]
[5, 2]
[5, 3]
[5, 4]
[5, 5]
[5, 6]
[5, 7]
[5, 8]
[5, 9]
[6, 0]
[6, 1]
[6, 2]
[6, 3]
[6, 4]
[6, 5]
[6, 6]
[6, 7]
[6, 8]
[6, 9]
[7, 0]
[7, 1]
[7, 2]
[7, 3]
[7, 4]
[7, 5]
[7, 6]
[7, 7]
[7, 8]
[7, 9]
[8, 0]
[8, 1]
[8, 2]
[8, 3]
[8, 4]
[8, 5]
[8, 6]
[8, 7]
[8, 8]
[8, 9]
[9, 0]
[9, 1]
[9, 2]
[9, 3]
[9, 4]
[9, 5]
[9, 6]
[9, 7]
[9, 8]
[9, 9]
[1, 0, 0]
[1, 0, 1]
[1, 0, 2]
[1, 0, 3]
[1, 0, 4]
[1, 0, 5]
[1, 0, 6]
[1, 0, 7]
[1, 0, 8]
[1, 0, 9]
[1, 1, 0]
[1, 1, 1]
[1, 1, 2]
[1, 1, 3]
[1, 1, 4]
[1, 1, 5]
[1, 1, 6]
[1, 1, 7]
[1, 1, 8]
[1, 1, 9]
[1, 2, 0]
[1, 2, 1]
[1, 2, 2]
[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 2, 6]
[1, 2, 7]
[1, 2, 8]
[1, 2, 9]
[1, 3, 0]
[1, 3, 1]
[1, 3, 2]
[1, 3, 3]
[1, 3, 4]
[1, 3, 5]
[1, 3, 6]
[1, 3, 7]
[1, 3, 8]
[1, 3, 9]
[1, 4, 0]
[1, 4, 1]
[1, 4, 2]
[1, 4, 3]
[1, 4, 4]
[1, 4, 5]
[1, 4, 6]
[1, 4, 7]
[1, 4, 8]
[1, 4, 9]
[1, 5, 0]
[1, 5, 1]
[1, 5, 2]
[1, 5, 3]
[1, 5, 4]
[1, 5, 5]
[1, 5, 6]
[1, 5, 7]
[1, 5, 8]
[1, 5, 9]
[1, 6, 0]
[1, 6, 1]
[1, 6, 2]
[1, 6, 3]
[1, 6, 4]
[1, 6, 5]
[1, 6, 6]
[1, 6, 7]
[1, 6, 8]
[1, 6, 9]
[1, 7, 0]
[1, 7, 1]
[1, 7, 2]
[1, 7, 3]
[1, 7, 4]
[1, 7, 5]
[1, 7, 6]
[1, 7, 7]
[1, 7, 8]
[1, 7, 9]
[1, 8, 0]
[1, 8, 1]
[1, 8, 2]
[1, 8, 3]
[1, 8, 4]
[1, 8, 5]
[1, 8, 6]
[1, 8, 7]
[1, 8, 8]
[1, 8, 9]
[1, 9, 0]
[1, 9, 1]
[1, 9, 2]
[1, 9, 3]
[1, 9, 4]
[1, 9, 5]
[1, 9, 6]
[1, 9, 7]
[1, 9, 8]
[1, 9, 9]
[2, 0, 0]
[2, 0, 1]
[2, 0, 2]
[2, 0, 3]
[2, 0, 4]
[2, 0, 5]
[2, 0, 6]
[2, 0, 7]
[2, 0, 8]
[2, 0, 9]
[2, 1, 0]
[2, 1, 1]
[2, 1, 2]
[2, 1, 3]
[2, 1, 4]
[2, 1, 5]
[2, 1, 6]
[2, 1, 7]
[2, 1, 8]
[2, 1, 9]
[2, 2, 0]
[2, 2, 1]
[2, 2, 2]
[2, 2, 3]
[2, 2, 4]
[2, 2, 5]
[2, 2, 6]
[2, 2, 7]
[2, 2, 8]
[2, 2, 9]
[2, 3, 0]
[2, 3, 1]
[2, 3, 2]
[2, 3, 3]
[2, 3, 4]
[2, 3, 5]"""