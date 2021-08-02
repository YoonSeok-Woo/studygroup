TC = int(input())
count = 0
for _ in range(TC):
    word = input()
    l = len(word)
    check = [False]*26
    check[ord(word[0])-ord('a')] = True
    i = 1
    while i<l:
        if word[i]!=word[i-1] and check[ord(word[i])-ord('a')]:
            break
        i+=1
    else :
        count+=1
print(count)
