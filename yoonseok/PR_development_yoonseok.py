from queue import Queue
def cal_date(prog,spd) :
    remain = 100-prog
    if remain%spd :
        return remain//spd+1
    else :
        return remain//spd
def solution(progresses, speeds):
    answer = []
    q = Queue()
    for i in range(len(progresses)) :
        #print(cal_date(progresses[i],speeds[i]))
        q.put(cal_date(progresses[i],speeds[i]))
    nc = 1
    now = q.get()
    while not q.empty() :
        temp = q.get()
        if now <temp :
            answer.append(nc)
            now = temp
            nc = 1
        else :
            nc+=1
    answer.append(nc)
        
    return answer

print(solution([93,30,55],[1,30,5]))