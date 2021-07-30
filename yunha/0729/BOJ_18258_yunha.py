class Queue():
    def __init__(self):
        self.queue = []  
    
    # push X: 정수 X를 큐에 넣는 연산이다. 
    def push(self, x):
        self.x = [x]
        self.queue = self.x + self.queue # 뒤에서 리스트 더해줌..ㅎ.. 이렇게 하면 되는가?
    
    # pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 
    # 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def pop(self):
        if self.queue == []:
            print(-1)
        else:
            print(self.queue[0])
            del self.queue[0]
    
    # size: 큐에 들어있는 정수의 개수를 출력한다.
    def size(self):
        print(len(self.queue))

    # empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    def empty(self):
        if len(self.queue) == 0:
            print(1)
        else:
            print(0)
    
    # front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def front(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[0])

    # back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    def bakc(self):
        if len(self.queue) == 0:
            print(-1)
        else:
            print(self.queue[-1])


# input 받는 걸 모르겠음... 
