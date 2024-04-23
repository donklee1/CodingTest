# S1_2178 미로탐색
from sys import stdin
from collections import deque
import sys

row_count, column_count = map(int, stdin.readline().split())
GRAPH = []
for i in range(row_count):
    GRAPH.append(list(map(int, stdin.readline().rstrip())))

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]
def BFS():
    global row_count, column_count
    q = deque()
    q.append((0,0))

    while q:
        x, y = q.popleft()
        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= row_count or nx >= column_count:
                continue
            if GRAPH[ny][nx] == 1:
                q.append((nx, ny))
                GRAPH[ny][nx] = GRAPH[y][x] + 1 # 그래프 배열을 재사용!!
    return GRAPH[row_count-1][column_count-1]

val = BFS()
print(val)
