class stack:
    top_ind=-1
    st_list=[]
    def __init__(self):
        self.top_ind=-1
        self.st_list=[]
    def empty(self):
        if self.top_ind==-1 :
            return True
        else :
            return False
    def top(self):
        if self.empty() :
            return -1
        else :
            return self.st_list[self.top_ind]
    def push(self,num):
        self.st_list.append(num)
        self.top_ind+=1
    def pop(self):
        if not self.empty():
            self.st_list.pop()
            self.top_ind-=1
    def size(self):
        return self.top_ind+1
N = int(input())
inputs = list(map(int,input().split()))
ins = stack()
for i in inputs :
    ins.push(i)
ans = stack()
nge = stack()
while not ins.empty():
    if nge.empty():
        ans.push(-1)
        nge.push(ins.top())
        ins.pop()
    elif ins.top()>=nge.top():
        nge.pop()
    else :
        ans.push(nge.top())
        nge.push(ins.top())
        ins.pop()
while not ans.empty():
    print(ans.top(),end=' ')
    ans.pop()
