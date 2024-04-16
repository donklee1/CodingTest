# 2583 S1 영역구하기
from sys import stdin
import sys
sys.setrecursionlimit(10**7)

ROW, COL,K = map(int, stdin.readline().split()) #행,열,종이수
PAPER = [[0] * COL for _ in range(ROW)]

def PrintPaper(PAPER):
    for i in range(ROW):
        print(PAPER[i])

for i in range(K): # 사각형
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            PAPER[ROW-1-y][x] = 1

def scanDFS(y, x):
    global area
    if PAPER[y][x] == 0:
        PAPER[y][x] = 1
        area += 1
    if x < (COL-1) and PAPER[y][x+1] == 0: # 좌측이동
        scanDFS(y, x+1)
    if x > 0 and PAPER[y][x-1] == 0: # 우측이동
        scanDFS(y, x-1)
    if y < (ROW-1) and PAPER[y+1][x] == 0: # 아래로이동
        scanDFS(y+1, x)
    if y > 0 and PAPER[y-1][x] == 0: # 위로이동
        scanDFS(y-1, x)

# ----------------------------------------------------
#PrintPaper(PAPER)
AREA = []
area = 0
for y in range(ROW):
    for x in range(COL):
        if PAPER[y][x] == 0:
            area = 0
            scanDFS(y, x)
            AREA.append(area)

AREA.sort()
print(len(AREA))
print(*AREA)
