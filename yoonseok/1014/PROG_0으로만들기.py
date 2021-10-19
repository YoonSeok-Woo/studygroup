import sys
sys.setrecursionlimit(3000000)

def postfix(i,a):
    global answer
    global tree
    res = 0
    for node in tree[i]:
        if visit[node]:
            continue
        visit[node] = True
        temp= postfix(node,a)
        res += temp
        answer += abs(temp)
    #print(answer)
    a[i] +=res
    return a[i]

def solution(a, edges):
    global answer
    global tree
    global visit
    answer = 0
    if sum(a)!=0:
        return -1
    tree = [[] for i in range(len(a))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])
    visit = [False]*len(a)
    postfix(0,a)
        
    return answer