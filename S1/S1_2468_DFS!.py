# S1_2468 장마-인접영역
from sys import stdin
import sys
sys.setrecursionlimit(10000)

N = int(input())
AREA =  [[0] * N for _ in range(N)]
Visited = [[False] * N for _ in range(N)]
for i in range(N):
    AREA[i] = list(map(int, stdin.readline().split()))

def InitVALID(N, rain_height):
    for i in range(N):
        for j in range(N):
            if (rain_height > 0) and (AREA[j][i] <= rain_height):
                Visited[j][i] = True # 물에잠김
            else:
                Visited[j][i] = False # 안전지역

# 한셀에 대하여 전후좌우 연속스캔
def DFS(N, x, y):
    if (x < 0) or (y < 0) or (x >= N) or (y >= N):
        return False
    if Visited[y][x] == True:
        return False

    #안전지역
    Visited[y][x] = True
    DFS(N, x-1, y) # 좌
    DFS(N, x+1, y) # 우
    DFS(N, x, y-1) # 상
    DFS(N, x, y+1) # 하
    return True

max_height = 0
for i in range(N):
    max_height = max(max(AREA[i]), max_height)

max_count = 0
for height in range(0, max_height):
    InitVALID(N, height)
    count = 0
    for i in range(N):
        for j in range(N):
            if Visited[i][j] == False:
                res = DFS(N, j, i)
                if res == True:
                    count += 1
    max_count = max(max_count, count)

print(max_count)