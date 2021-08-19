import sys
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
st = stack()
for i in range(N):
    s = sys.stdin.readline().split()
    if s[0]=='push':
        st.push(s[1])
    if s[0]=='pop':
        print(st.top())
        st.pop()
    if s[0]=='size':
        print(st.size())
    if s[0]=='empty':
        if st.empty() :
            print(1)
        else :
            print(0)
    if s[0]=='top':
        print(st.top())
    