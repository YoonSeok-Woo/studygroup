import sys
class queue:
    q_list=[]
    f_index=0
    b_index=-1
    def __init__(self):
        self.q_list = []
        self.f_index = 0
        self.b_index = -1
    def empty(self) :
        if self.b_index-self.f_index<0 :
            return True
        else :
            return False
    def push(self,num) :
        self.q_list.append(num)
        self.b_index+=1
    def front(self) :
        if self.empty() :
            return -1
        else :
            return self.q_list[self.f_index]
    def back(self) :
        if self.empty():
            return -1
        else :
            return self.q_list[self.b_index]
    def pop(self) :
        if self.empty():
            return -1
        else :
            res = self.q_list[self.f_index]
            self.q_list[self.f_index]=0
            self.f_index+=1
            return res
    def size(self) :
        return self.b_index-self.f_index+1
N = int(input())
a = queue()
for i in range(N) :
    command = sys.stdin.readline().split()
    if command[0]=='push':
        a.push(command[1])
    elif command[0]=='pop':
        print(a.pop())
    elif command[0]=='size':
        print(a.size())
    elif command[0]=='empty':
        if a.empty():
            print(1)
        else :
            print(0)
    elif command[0]=='front':
        print(a.front())
    elif command[0]=='back':
        print(a.back())
    #print(a.q_list)