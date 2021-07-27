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

def solution(board, moves):
    answer = 0
    s = len(board)
    st_board = []
    basket = stack()
    for i in range(s):
        temp = stack()
        st_board.append(temp)
    for i in range(s-1,-1,-1):
        for j in range(s):
            if board[i][j]!=0:
                st_board[j].push(board[i][j])
    for i in moves :
        #print(basket.st_list)
        if not st_board[i-1].empty():
            temp = st_board[i-1].top()
            st_board[i-1].pop()
            if basket.empty():
                basket.push(temp)
            elif basket.top()!=temp:
                basket.push(temp)
            else :
                basket.pop()
                answer+=1
        
    return answer*2

board1=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves1 = [1,5,3,5,1,2,1,4]
print(solution(board1,moves1))