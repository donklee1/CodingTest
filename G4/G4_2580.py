# 2580 스도쿠 G4
from sys import stdin
BLANK = []

def CheckHorz(row, val):
    global BOARD
    for i in range(9):
        if BOARD[row][i] == val: # 이미 있으므로 불가
            return False
    return True 

def CheckCol(col, val):
    global BOARD
    for i in range(9):
        if BOARD[i][col] == val: # 이미 있으므로 불가
            return False
    return True 

def CheckRect(row, col, val):
    global BOARD
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
          if BOARD[row_start+i][col_start+j] == val: # 이미 있으므로 불가
            return False
    return True 

def PrintList(N, BOARD):
    for i in range(N):
        for j in range(N):
            print(BOARD[i][j], end = ' ')
        print()

def DFS(N, count, MAX):
    global BOARD
    if count == MAX:
        PrintList(N, BOARD)
        exit(0)
        return
    (y, x) = BLANK[count]
    for val in range(1, 10):
        if CheckHorz(y, val) and CheckCol(x, val) and CheckRect(y, x, val):
            BOARD[y][x] = val
            DFS(N, count+1, MAX)
            BOARD[y][x] = 0

# ------------------------------------------------
N = 9
BOARD = [[0] * N for _ in range(N)]
for i in range(N):
    S = stdin.readline()
    BOARD[i] = list(map(int, S.split()))

for i in range(N):
    for j in range(N):
        if BOARD[i][j] == 0:
            BLANK.append((i,j))
DFS(N, 0, len(BLANK))
