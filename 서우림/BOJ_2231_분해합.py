n = int(input()) # 216
result = 0

for i in range (1000001):
    n_list = list(map (int, str(i))) # [2, 1, 6]
    result = i + sum(n_list)   #i = 198, sum = 18  # result = 216
   
    if result == n:  
        print(i)
        break
    if i == n: 
        print(0)
    
# 자리수 합을 while로 돌리면 안되는 이유 :
# n 이 반복문 돌며 결국 0이 됨. 
# 생성자를 찾을 수없게 된다.
# sumN = 0
# while n > 0:
#     sumN += n % 10
#     n = n // 10
# print(sumN)
