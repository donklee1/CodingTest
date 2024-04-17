# S1_2468 장마-인접영역
from sys import stdin
import sys
sys.setrecursionlimit(100000)

N = int(input())
AREA =  [[0] * N for _ in range(N)]
Visited = [[False] * N for _ in range(N)]
for i in range(N):
    AREA[i] = list(map(int, stdin.readline().split()))

def dfs_find_area(y, x):
    global N, rain_height
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    if (AREA[y][x] <= rain_height) or Visited[y][x] == True:
        return False
    
    Visited[y][x] = True
    dfs_find_area(y, x-1) #좌
    dfs_find_area(y, x+1) #우
    dfs_find_area(y-1, x) #상
    dfs_find_area(y+1, x) #하
    return True

max_area_height = 0
for i in range(N):
    max_area_height = max(max_area_height, max(AREA[i])) # 지역의 최대높이 계산

max_count = 0
for rain_height in range(max_area_height):
    count = 0
    Visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if dfs_find_area(y, x):
                count += 1
    max_count = max(max_count, count)

print(max_count)