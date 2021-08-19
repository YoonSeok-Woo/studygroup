# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )\"\"\"\\')
# print("|\"^\"`    |")
# print("||_/=\\\\__|")

# 
# A, B, C = map(int, input().split())
# print((A+B)%C) 
# print(((A%C) + (B%C))%C) 
# print((A*B)%C) 
# print(((A%C) * (B%C))%C) 

#2558번
# a = int(input())
# b = int(input())

# print(a*(b%10))
# print(a*((b//10)%10))
# print(a*(b//100%10))
# print((a*(b%10)) + 10 * (a*((b//10)%10)) + 100 * (a*(b//100%10)))

# numbers = [1, 2, 3]

# # 위의 변수 numbers를 문자열 '123'으로 만드세요. (join 메서드 활용)
# new_numbers = ''
# for i in numbers:
#     new_numbers += ', '.join(str(i))
# print(new_numbers)
a = 'yaya!'
b = 'wooooowoo'
a.replace('y', 'h')
print(a)
# print(a.replace('y', 'h'))