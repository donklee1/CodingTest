# 1012 S2
from sys import stdin

testcase = int(stdin.readline().rstrip())
count = 0

def DFS(x, y, rows, cols):
    global count


    for i in range(cols):
        if (GROUND[y][x] == 1) and (Checked[y][x] == False):
            Checked[y][x] = True
            DFS(x+1, y, rows, cols) # --> 방향
            DFS(x-1, y, rows, cols) # <-- 방향
            DFS(x, y-1, rows, cols) # 위 방향
            DFS(x, y+1, rows, cols) # 아래 방향


for _ in range(testcase):
    cols, rows, pos_count = map(int, stdin.readline().split())
    GROUND = [[0] * cols for _ in range(rows)]
    Checked = [[False] * cols for _ in range(rows)]
    for i in range(pos_count):
        x, y = map(int, stdin.readline().split())
        GROUND[y][x] = 1

    count = 0
    DFS(0, 0, rows, cols)
    print("count=", count)
