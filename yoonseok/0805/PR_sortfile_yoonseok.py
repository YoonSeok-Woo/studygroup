from functools import cmp_to_key
def hnt(file):
    l = len(file)
    i = 0
    h_ind = -1
    for i in range(l) :
        if h_ind ==-1 and ord('9')>=ord(file[i])>=ord('0'):
            head = file[:i]
            h_ind = i
        if h_ind!=-1 and not(ord('9')>=ord(file[i])>=ord('0')):
            number = file[h_ind:i]
            break
    else:
        number = file[h_ind:]
        
    return (head.upper(),int(number))

def compare(file1,file2):
    head1, number1 = hnt(file1)
    head2, number2 = hnt(file2)
    if head1 < head2:
        return -1
    elif head1 > head2:
        return 1
    else :
        if number1 <number2 :
            return -1
        elif number1 > number2:
            return 1
        else :
            return 0

def solution(files): 
    answer = []
    for i in files:
        print(hnt(i))
    answer = sorted(files,key = cmp_to_key(compare))
    return answer