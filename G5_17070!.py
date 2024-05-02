# GS-17070 파이프옮기기-1
from collections import deque

N = int(input())
ROOM = []
for _ in range(N):
    ROOM.append(list(map(int, input().split())))
Visited = [[False] * N for _ in range(N)]
# for i in range(N):
#     print(ROOM[i])

POS_HORZ = 0 # -
POS_VERT = 1 # |
POS_DIAG = 2 # \

def CheckVisited(L):
    for (y,x) in L:
        if Visited[y][x] == True:
            return True
    return False

count = 0
def DFS(y,x, pos):
    global count
    print("DFS(",y,x,") pos = ", pos)
    if (x == N-1) and (y == N-1):
        print("카운트 증가",x,y)
        count += 1
        return
    if (x == N-1) or (x == N-1): # 우측, 아래벽 위치
        print("벽에서 종료",x,y)
        return

    # --- 회전 ---
    if pos == POS_HORZ and ROOM[y+1][x] == 0 and not Visited[y+1][x]:
            print(" 대각회전",y+1, x)
            Visited[y+1][x] = True
            DFS(y+1,x, POS_DIAG) # 수평 --> 대가회전
    elif pos == POS_HORZ and ROOM[y+1][x-1] == 0 and not Visited[y+1][x-1]:
            Visited[y+1][x-1] = True 
            DFS(y+1,x-1, POS_VERT) # 수평 --> 수직회전
    elif pos == POS_VERT and ROOM[y-1][x-1] == 0 and not Visited[y-1][x-1]:
            Visited[y-1][x-1] = True 
            DFS(y-1,x-1, POS_HORZ) # 수직 --> 수평회전
    elif pos == POS_VERT and ROOM[y][x+1] == 0 and not Visited[y][x+1]:
            Visited[y][x+1] = True 
            DFS(y,x+1, POS_HORZ) # 수직 --> 대각회전
    else:
        print(" 회전안함",x,y)

    # --- 밀기 ---
    if pos == POS_DIAG and ROOM[y+1][x+1] == 0 and not Visited[y+1][x+1]:
        print(" 대각선 밀기",x,y)
        Visited[y+1][x+1] = True
        DFS(y+1,x+1, POS_DIAG) # 대각선 밀기
    else:
        print(" 밀기안함",x,y)

    # --- 이동 ---
    if pos == POS_HORZ:
        if ROOM[y][x+1] == 0 and not CheckVisited([(y, x+1)]):
            print(" 이동->",x+1,y)
            Visited[y][x+1] = True
            DFS(y, x+1, pos)
        elif ROOM[y+1][x+1] == 0 and not CheckVisited([(y+1,x+1),(y,x+1),(y+1,x)]):
            print(" 이동 대각",x+1,y+1)
            Visited[y+1][x+1] = True
            DFS(y+1, x+1, POS_DIAG)
    elif pos == POS_VERT:
        if ROOM[y+1][x] == 0 and not CheckVisited([(y+1, x)]):
            print(" 이동아래",y+1,x)
            Visited[y+1][x] = True
            DFS(y+1, x, pos)
        elif ROOM[y+1][x+1] == 0 and not CheckVisited([(y+1,x+1),(y,x+1),(y+1,x)]):
            print(" 이동 대각",x+1,y+1)
            Visited[y+1][x+1] = True
            DFS(y+1, x+1, POS_DIAG)
    elif pos == POS_DIAG:
        if ROOM[y][x+1] == 0 and not CheckVisited([(y, x+1)]):
            print(" -->",y+1,x)
            Visited[y][x+1] = True
            DFS(y, x+1, POS_HORZ)
        elif ROOM[y+1][x] == 0 and not CheckVisited([(y+1, x)]):
            print(" 아래",y+1,x)
            Visited[y+1][x] = True
            DFS(y+1, x, POS_VERT)
        elif ROOM[y+1][x+1] == 0 and not CheckVisited([(y+1,x+1),(y,x+1),(y+1,x)]):
            print(" 이동 대각",x+1,y+1)
            Visited[y+1][x+1] = True
            DFS(y+1, x+1, POS_DIAG)
    else:
        print(" 이동안함",x,y)

    print("-- DFS 끝 --")

DFS(0, 1, POS_HORZ) #헤드위치
print(count)

