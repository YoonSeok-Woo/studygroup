word = input()
count = 0
i = 0
l = len(word)
while i <l:
    if ord(word[i]) <= ord('z') and ord(word[i]) >= ord('a'):
        count+=1
    if word[i]=='c':
        if i <l-1 and (word[i+1]=='=' or word[i+1]=='-'):
            i+=1
    elif word[i]=='l' or word[i]=='n':
        if i<l-1 and word[i+1]=='j':
            i+=1
    elif word[i]=='s' or word[i]=='z':
        if i<l-1 and word[i+1]=='=':
            i+=1
    elif word[i]=='d' :
        if i<l-1 and word[i+1]=='-':
            i+=1
        if i<l-2 and word[i+1]=='z' and word[i+2]=='=':
            i+=2
    
    i+=1
print(count)