import sys

def solve():
    # global : visited, ret
    visited[0] = True
    go(path=[0], cost=0, visit_cnt=1)
    
    print(ret)

# dfs+backtracking travasal function
def go(path, cost, visit_cnt):
    global ret
    # global : ret, costs, visited

    if cost >= ret:
        return
    

    last = path[-1]
    if visit_cnt == len(costs):
        # travasal finish

        start = path[0]
        if costs[last][start] != 0:
            ret = min(ret, cost+costs[last][start])
        return

    for i in range(1, n):
        if visited[i] or costs[last][i] == 0:
            continue
        visited[i] = True
        path.append(i)

        go(path,cost+costs[last][i],visit_cnt+1)
        
        visited[i] = False
        path.pop()
    return

n = int(input())
costs = [[int(_) for _ in input().split()] 
                   for y in range(n)]
visited = {city: False for city in range(n)}
ret = sys.maxsize

solve()