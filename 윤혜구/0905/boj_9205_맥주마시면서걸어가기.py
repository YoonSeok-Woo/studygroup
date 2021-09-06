def go():
    q = [(sr, sc)]
    while q:
        ci, cj = q.pop(0)
        for n in range(N + 1):
            nc, nr = stops[n]
            if visited[n] == 0 and abs(nr - ci) + abs(nc - cj) <= 1000:
                if n == N:
                    return 'happy'
                else:
                    q.append((nr, nc))
                    visited[n] = 1
        
    return 'sad'


T = int(input())
for tc in range(T):
    N = int(input())
    sc, sr = map(int, input().split())
    stops = [list(map(int, input().split())) for _ in range(N + 1)]
    visited = [0] * (N + 1)

    print(go())
