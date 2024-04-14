# 1012 S2
from sys import stdin
import sys
sys.setrecursionlimit(10000)
testcase = int(stdin.readline().rstrip())

def DFS(x, y, rows, cols):
    if (x < 0) or (x >= cols) or (y < 0) or (y >=rows):
        return False
    
    if (GROUND[y][x] == 1) and (Checked[y][x] == False):
        Checked[y][x] = True
        DFS(x+1, y, rows, cols) # --> 방향
        DFS(x-1, y, rows, cols) # <-- 방향
        DFS(x, y-1, rows, cols) # 위 방향
        DFS(x, y+1, rows, cols) # 아래 방향
        return True
    else:
        return False

for _ in range(testcase):
    cols, rows, pos_count = map(int, stdin.readline().split())
    GROUND = [[0] * cols for _ in range(rows)]
    Checked = [[False] * cols for _ in range(rows)]
    for i in range(pos_count):
        x, y = map(int, stdin.readline().split())
        GROUND[y][x] = 1

    count = 0
    for y in range(rows):
        for x in range(cols):
            if DFS(x, y, rows, cols) == True:
                count += 1
    print(count)
