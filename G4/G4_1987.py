# 1987 G4
from sys import stdin
R, C = map(int, stdin.readline().split())

BOARD = []
for i in range(R):
    BOARD.append(list(stdin.readline()))
ROOT = [BOARD[0][0]] # 초기위치
UseAlpahbat = [False] * 26
UseAlpahbat[ord(BOARD[0][0])-ord('A')] = True

max_path = 0
def DFS_Stack(x, y):
    global max_path
    max_path = max(max_path, len(ROOT)) # 이동최대값 계산

    if ((x+1) < C) and (BOARD[y][x+1] in ROOT) == False: # 좌측이동
        ROOT.append(BOARD[y][x+1])
        DFS_Stack(x+1, y)
        ROOT.pop()
    if x > 0 and (BOARD[y][x-1] in ROOT) == False: # 우측
        ROOT.append(BOARD[y][x-1])
        DFS_Stack(x-1, y)
        ROOT.pop()
    if (y+1) < R and (BOARD[y+1][x] in ROOT) == False: # 아래이동
        ROOT.append(BOARD[y+1][x])
        DFS_Stack(x, y+1)
        ROOT.pop()
    if y > 0 and (BOARD[y-1][x] in ROOT) == False: # 위이동
        ROOT.append(BOARD[y-1][x])
        DFS_Stack(x, y-1)
        ROOT.pop()

def DFS_Flag(x, y, maxval):
    global max_path
    max_path = max(max_path, maxval) # 이동최대값 계산

    if (x+1) < C and UseAlpahbat[ord(BOARD[y][x+1])-ord('A')] == False: # 좌측이동
            UseAlpahbat[ord(BOARD[y][x+1])-ord('A')] = True
            DFS_Flag(x+1, y, maxval+1)
            UseAlpahbat[ord(BOARD[y][x+1])-ord('A')] = False
    if x > 0 and UseAlpahbat[ord(BOARD[y][x-1])-ord('A')] == False: # 우측
            UseAlpahbat[ord(BOARD[y][x-1])-ord('A')] = True
            DFS_Flag(x-1, y, maxval+1)
            UseAlpahbat[ord(BOARD[y][x-1])-ord('A')] = False
    if (y+1) < R and UseAlpahbat[ord(BOARD[y+1][x])-ord('A')] == False: # 아래이동
            UseAlpahbat[ord(BOARD[y+1][x])-ord('A')] = True
            DFS_Flag(x, y+1, maxval+1)
            UseAlpahbat[ord(BOARD[y+1][x])-ord('A')] = False
    if y > 0 and UseAlpahbat[ord(BOARD[y-1][x])-ord('A')] == False: # 위이동
            UseAlpahbat[ord(BOARD[y-1][x])-ord('A')] = True
            DFS_Flag(x, y-1, maxval+1)
            UseAlpahbat[ord(BOARD[y-1][x])-ord('A')] = False

#DFS_Stack(0,0) #-- 시간초과
DFS_Flag(0,0, 1)
print(max_path)