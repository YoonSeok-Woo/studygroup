from queue import Queue
TC = int(input())
def get_dis(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

for tc in range(TC):
    N = int(input())
    points = []
    for i in range(N+2):
        points.append(list(map(int,input().split())))
    visit = [False]*(N+2)
    q = Queue()
    q.put((points[0],0))
    visit[0]=True
    Found = False
    while not q.empty():
        now,ind = q.get()
        if ind == N+1:
            print('happy')
            Found = True
            break
        for i,next in enumerate(points):
            if get_dis(now,next)>1000:
                continue
            if visit[i]:
                continue
            q.put((next,i))
            visit[i]=True
    else:
        print('sad')