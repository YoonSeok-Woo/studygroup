import queue
dx = [0,1,0,-1]
dy = [1,0,-1,0]
visit_table = []
visit_gb = []
s = 0
def bfs_table(table,i,j):#조각들의 위치와 크기를 구합니다.
    q = queue.Queue()
    x1 = i
    x2 = i
    y1 = j
    y2 = j
    q.put((i,j))
    while not q.empty():
        x, y = q.get()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny < 0 or nx>=s or ny >=s:
                continue
            if table[nx][ny]==0 or visit_table[nx][ny]:
                continue
            visit_table[nx][ny]=1
            q.put((nx,ny))
            x1 = min(x1,nx)
            x2 = max(x2,nx)
            y1 = min(y1,ny)
            y2 = max(y2,ny)
    return [[x1,y1],[x2,y2],[x2-x1+1,y2-y1+1]]

def bfs_gb(game_board,i,j):#빈공간의 위치와 크기들을 구합니다.
    q = queue.Queue()
    x1 = i
    x2 = i
    y1 = j
    y2 = j
    q.put((i,j))
    while not q.empty():
        x, y = q.get()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if nx<0 or ny < 0 or nx>=s or ny >=s:
                continue
            if game_board[nx][ny]==1 or visit_gb[nx][ny]:
                continue
            visit_gb[nx][ny]=1
            q.put((nx,ny))
            x1 = min(x1,nx)
            x2 = max(x2,nx)
            y1 = min(y1,ny)
            y2 = max(y2,ny)
    return [[x1,y1],[x2,y2],[x2-x1+1,y2-y1+1]]

def rot(table):
    res = list([0]*s for x in range(s))
    for i in range(s):
        for j in range(s):
            res[j][s-1-i] = table[i][j]
    return res
def ijrot(p):
    return (p[1],s-1-p[0])
def matching(game_board,gx,gy,table,tp1,tp2,gs,ts):
    if gs[0]!=ts[0] or gs[1]!=ts[1]:
        return 0
    res = 0
    tpx = min(tp1[0],tp2[0])
    tpy = min(tp1[1],tp2[1])
    for i in range(gs[0]):
        for j in range(gs[1]):
            if game_board[gx+i][gy+j]+table[tpx+i][tpy+j]!=1:
                return 0
            else:
                if game_board[gx+i][gy+j]==0:
                    res+=1
    return res
def solution(game_board, table):
    answer = 0
    global s
    s = len(game_board)
    global visit_table
    global visit_gb
    piece = []
    for i in range(s):
        visit_table.append([False]*s)
        visit_gb.append([False]*s)
    for i in range(s):
        for j in range(s):
            if table[i][j]==1 and (not visit_table[i][j]):
                piece.append(bfs_table(table,i,j))
    used = [False]*len(piece)
    space = []
    for i in range(s):
        for j in range(s):
            if game_board[i][j]==0 and (not visit_gb[i][j]):
                space.append(bfs_gb(game_board,i,j))
    t90 = rot(table)
    t180 = rot(t90)
    t270 = rot(t180)
    for i in space:
        for j,p in enumerate(piece):
            if (used[j]):
                continue
            if (i[2][0]==p[2][0] and i[2][1]==p[2][1]) or (i[2][0]==p[2][1] and i[2][1] == p[2][0]):
                #회전 X
                p0 = p[0]
                p1 = p[1]
                a = matching(game_board,i[0][0],i[0][1],table,p0,p1,i[2],p[2])
                #90
                p0 = ijrot(p0)
                p1 = ijrot(p1)
                b = matching(game_board,i[0][0],i[0][1],t90,p0,p1,i[2],[p[2][1],p[2][0]])
                #180
                p0 = ijrot(p0)
                p1 = ijrot(p1)
                c = matching(game_board,i[0][0],i[0][1],t180,p0,p1,i[2],p[2])
                #270
                p0 = ijrot(p0)
                p1 = ijrot(p1)
                d = matching(game_board,i[0][0],i[0][1],t270, p0,p1,i[2],[p[2][1],p[2][0]])
                if a:
                    answer+=a
                    used[j] = True
                    print(a)
                    break
                elif b:
                    answer+=b
                    used[j] = True
                    print(b)
                    break
                elif c:
                    answer+=c
                    used[j] = True
                    print(c)
                    break
                elif d:
                    answer+=d
                    used[j] = True
                    print(d)
                    break
    print(used)
    return answer