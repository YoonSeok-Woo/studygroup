class stack :
    def __init__(self) :
        self.st_list=[]
        self.st_ind=-1
    def push(self,char):
        self.st_list.append(char)
        self.st_ind+=1
    def pop(self):
        self.st_list.pop()
        self.st_ind-=1
    def empty(self):
        if self.st_ind ==-1 :
            return True
        else : 
            return False
    def top(self):
        if self.empty():
            return -1
        return self.st_list[self.st_ind]
    
while 1 :
    sentence = input()
    if sentence == '.':
        break
    else :
        checking = stack()
        for c in sentence :
            if c == '(' or c=='[':
                checking.push(c)
            elif c==')':
                if checking.top() !='(':
                    checking.push(c)
                    break
                else :
                    checking.pop()
            elif c==']':
                if checking.top()!='[':
                    checking.push(c)
                    break
                else :
                    checking.pop()
            #if(c =='(' or c==')' or c=='[' or c==']'):
                #print(checking.st_list)
        if checking.empty():
            print("yes")
        else :
            print("no")