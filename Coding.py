# 1987 G4
from sys import stdin
import itertools
SAMPLE = ["HFDFFB", "AJHGDH", "DGAGEH"]
R, C = 3, 6

BOARD = []
for i in range(R):
    BOARD.append(list(SAMPLE[i]))
ROOT = [BOARD[0][0]] # 초기위치
print(BOARD)
print(ROOT)

max_path = 0
def DFS(x, y):
    global max_path
    max_path = max(max_path, len(ROOT)) # 이동최대값 계산
    if x < 0 or y < 0:
        return
    if x >= C or y >= R:
        return
    print("DFS(",x,y,") max-->", max_path)

    while True:
        if ((x+1) < C) and (BOARD[y][x+1] in ROOT) == False: # 좌측이동
                print("-->", BOARD[y][x+1])
                ROOT.append(BOARD[y][x+1])
                DFS(x+1, y)
                ROOT.pop()
        elif x > 0 and (BOARD[y][x-1] in ROOT) == False: # 우측
                print("<--", BOARD[y][x-1])
                ROOT.append(BOARD[y][x-1])
                DFS(x-1, y)
                ROOT.pop()
        elif (y+1) < R and (BOARD[y+1][x] in ROOT) == False: # 아래이동
                print("아래", BOARD[y+1][x])
                ROOT.append(BOARD[y+1][x])
                DFS(x, y+1)
                ROOT.pop()
        elif y > 0 and (BOARD[y-1][x] in ROOT) == False: # 위이동
                print("위", BOARD[y-1][x])
                ROOT.append(BOARD[y-1][x])
                DFS(x, y-1)
                ROOT.pop()
        else:
            break
              

DFS(0,0)
print(max_path)