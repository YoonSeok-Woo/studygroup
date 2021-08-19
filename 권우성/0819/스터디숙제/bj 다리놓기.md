# 다리놓기

문제출처 - [1010번: 다리 놓기 (acmicpc.net)](https://www.acmicpc.net/problem/1010)

문제 요약 

​	1. 동과 서를 겹치지 않게 연결하는 직선의 갯수 

input - 

```
3
2 2
1 5
13 29
```

output-

```
1
5
67863915
```

해설코드 

```
def fac(i):
    a=1
    for k in range(i,0,-1):
        a=a*k
        k=k-1
    return a

T = int (input())
for t in range(1,T+1):
    a,b =list(map(int,input().split()))
    answer1=fac(a)
    # print(answer1)
    answer2=fac(b-a)
    # print(answer2)
    answer3=fac(b)
    answer=answer3//answer2//answer1
    print(answer)

```

