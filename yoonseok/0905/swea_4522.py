TC = int(input())
for tc in range(1,TC+1):
    word = input()
    l = len(word)
    middle = l//2
    ans = True
    for i in range(middle):
        if not (word[i]==word[l-1-i] or word[i]=='?' or word[l-i-1]=='?'):
            ans = False
            break
    if ans:
        print(f'#{tc} Exist')
    else:
        print(f'#{tc} Not exist')