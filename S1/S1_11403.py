# S1-11403 경로찾기
from collections import deque

N = int(input())
GRAPH = []
for _ in range(N):
    GRAPH.append(list(map(int, input().split())))

def BFS(v):
    q = deque()
    q.append(v)
    while q:
        node = q.popleft()
        for idx, w in enumerate(GRAPH[node]):
            if w == 1 and Visited[idx] == 0:
                Visited[idx] = 1
                q.append(idx)

RESULT = []
for v in range(N):
    Visited = [0] * N
    BFS(v)
    RESULT.append(Visited)

for i in range(N):
    print(*RESULT[i])
