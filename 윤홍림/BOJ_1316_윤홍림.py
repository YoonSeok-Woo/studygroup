N = int(input())
group = 0
for j in range(N):
    word = input()
    error = 0
    word_set = set()
    for i in range(len(word)):
        if word[i] in word_set:
            if word[i-1] != word[i]:
                error = 1
                break
        else:
            word_set.add(word[i])
    if error != 1:
        group += 1
print(group)