answers = []
def dfs(now,ans,tickets):
    global used
    
    if not False in used:
        answers.append(ans+[now])
        return
    for i,ticket in enumerate(tickets):
        if ticket[0] != now:
            continue
        if used[i]:
            continue
        used[i] = True
        dfs(ticket[1],ans+[ticket[0]],tickets)
        used[i] = False

def solution(tickets):
    global used
    answer = []
    used = [False]*len(tickets)
    dfs('ICN',[],tickets)
    answers.sort()
    answer = answers[0]
    
    return answer