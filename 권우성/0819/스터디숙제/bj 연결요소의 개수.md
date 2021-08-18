# 연결요소의개수

문제출처 - [11724번: 연결 요소의 개수 (acmicpc.net)](https://www.acmicpc.net/problem/11724)

문제 요약 

​	1. 연결요소의 개수 

input - 

```
6 5
1 2
2 5
5 1
3 4
4 6
```

output-

```
2
```

제출코드 

```
a,b=list(map(int,input().split()))
lst=[]
for t in range(1,b+1):
    lst+=[list(map(int,input().split()))]
# print(lst)
    answer=1
    lsta=[]
    lstb=[]
    l=len(lst)
    samlst=lst[::1]
for i in range (a):
    for i in range(1,l-1):
        lsta +=lst[0]
        # print(lsta)
        if lst[i][0] in lsta:
            lsta += lst[i]
        elif lst[i][1] in lsta:
            lsta += lst[i]
        else:
            lstb +=lst[i]

        for i in (lstb):
            if i in lsta:
                lsta+=lstb
                lstb=[]

            # answer +=1
# print(lsta)
# print(lstb)

# 질문  lst 를 반복문돌때 새로운 공란을 만들어서 돌리면  될거같은데 모르겟음 .... 테케는 됨

    # if lst[i][0] == lst[i+1][0] or lst[i][0] == lst[i+1][1] or lst[i][1] == lst[i+1][0] or lst[i][1] == lst[i+1][1]:
    #     samlst.remove(lst[i])
    #     print(samlst)
    # elif  lst[i][1] == lst[i+1][0] or lst[i+1][1]:
    #     lstb+=lst[i]
    #     print(lstb)
    # else:
    #     answer+=1
    if lstb !=[]:
        answer =2
print(answer)
# print(lst)
```

해설코드 

```
def dfs(x):
    c[x] = 1
    for i in a[x]:
        if c[i] == 0:
            dfs(i)


n, m = map(int, input().split())
c = [0 for _ in range(n)]
# print(c)
a = [[] for _ in range(n)]
# print(a)
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1;
    v -= 1
    a[u].append(v)
    # print(a)
    a[v].append(u)
    # print(a)

cnt = 0
for i in range(n):
    if c[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
```

