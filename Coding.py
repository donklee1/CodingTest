# S1-14940 쉬운최단거리
from collections import deque

N, M = map(int, input().split())
MAP = []
org_y, org_x = 0,0
for i in range(N):
    L = list(input().split())
    if '2' in L:
        org_y = i
        org_x = L.index('2')
    MAP.append(L)

RESULT = [[-1] * M for _ in range(N)] # 도달못한 경우의 기본값 -1

dx = [-1, 1,  0, 0]
dy = [ 0, 0, -1, 1]
def BFS(y, x):
    global N, M
    q = deque()
    q.append((y, x, 1))
    RESULT[y][x] = 0 #목표점
    Visited[y][x] = 1
    while q:
        (y2, x2, dist) = q.popleft()
        for i in range(4):
            ny = y2 + dy[i]
            nx = x2 + dx[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N or Visited[ny][nx] == 1:
                continue
            Visited[ny][nx] = 1
            if MAP[ny][nx] == '0':
                RESULT[ny][nx] = 0 # 갈수없는땅 --> 이 방법으로 완전하게 채울 수 없다 !!
                continue
            if MAP[ny][nx] == '1': # 갈수있는길
                RESULT[ny][nx] = dist
                q.append((ny,nx, dist+1))

Visited = [[0] * M for _ in range(N)]
BFS(org_y, org_x) # 주의 - 한번호출로 완전탐색 가능!!

for i in range(N):
    for j in range(M):
        if MAP[i][j] == '0':
            RESULT[i][j] = 0 # 벽위치 채움 
    print(*RESULT[i])