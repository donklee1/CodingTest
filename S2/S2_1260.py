# 1260 S2 DFS/BFS
from sys import stdin

vertex_count, edge_count, start_vertex = map(int, stdin.readline().split())
GRAPH = [[0] * (vertex_count+1) for _ in range(vertex_count+1)]
Visited1 = [False] * (vertex_count + 1)
Visited2 = [False] * (vertex_count + 1)

# ---- 인접행렬 생성 ---
for _ in range(edge_count):
    v1, v2 = map(int, stdin.readline().split())
    GRAPH[v1][v2] = 1
    GRAPH[v2][v1] = 1

# ----------------------------------------------
def DFS(v):
    print(v, end=" ")
    Visited1[v] = True
    for w in range(1, vertex_count+1):
        if not Visited1[w] and GRAPH[v][w] == 1:
            DFS(w)

# ----------------------------------------------
BFS_QUEUE = []
def BFS(v):
    BFS_QUEUE.append(v)
    print(v, end=" ")
    Visited2[v] = True

    while len(BFS_QUEUE) > 0:
        v = BFS_QUEUE.pop(0)
        for w in range(1, vertex_count+1):
            if not Visited2[w] and GRAPH[v][w] == 1:
                BFS_QUEUE.append(w)
                print(w, end=" ")
                Visited2[w] = True

DFS(start_vertex)
print("")
BFS(start_vertex)

