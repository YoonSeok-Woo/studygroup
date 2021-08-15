TC = int(input())
for tc in range(1,TC+1):
    words = []
    max = 0
    for i in range(5):
        words.append(input())
        if max<len(words[i]):
            max = len(words[i])
    ans = ''
    for i in range(max):
        for j in range(5):
            if len(words[j])<=i:
                continue
            else:
                ans = ans+words[j][i]
    print(f'#{tc} {ans}')
            
