# S2_2667 단지번호 붙이기
from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
MAP = []
Visited = [[False] * N for _ in range(N)]
for _ in range(N):
    MAP.append(list(stdin.readline().rstrip()))

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]
def DFS(N, x, y):
    global count
    Visited[y][x] = True
    if MAP[y][x] == '1':
        count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or  nx >= N or ny < 0 or ny >= N:
            continue
        if Visited[ny][nx] == False and MAP[ny][nx] == '1':
            DFS(N, nx, ny)

RESULT = []
for x in range(N):
    for y in range(N):
        if Visited[y][x] == False and MAP[y][x] == '1':
            count = 0
            DFS(N, x,y)
            RESULT.append(count)

RESULT.sort()
print(len(RESULT))
for c in RESULT:
    print(c)