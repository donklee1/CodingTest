# 1260 S2 DFS/BFS
from sys import stdin

GRAPH = dict() # 딕셔너리로 저장
vertex_count, edge_count, start_vertex = map(int, stdin.readline().split())

# ---- 인접리스트를 생성하는 방법 ---
for _ in range(edge_count):
    v1, v2 = map(int, stdin.readline().split())
    if (v1 in GRAPH) == False:
        GRAPH[v1] = [v2]
    else:
        edge_list = GRAPH[v1]
        edge_list.append(v2)
        edge_list.sort() # 작은순서 방문을 위함
        GRAPH[v1] = edge_list

# ----------------------------------------------
DFS_RESULT = []
def DFS(v):
    DFS_RESULT.append(v)
    if (v in GRAPH) == True:
        for w in GRAPH[v]:
            if (w in DFS_RESULT) == False:
                DFS(w)
                

print(GRAPH)
# ----------------------------------------------
BFS_QUEUE = []
def BFS(v):
    BFS_QUEUE.append(v)

    while len(BFS_QUEUE) > 0:
        w = BFS_QUEUE[0]
        if (w in GRAPH) == True:
            for z in GRAPH[w]:
                if (z in BFS_QUEUE) == False:
                    BFS_QUEUE.append(z)
                    if len(BFS_QUEUE) == vertex_count:
                        return

DFS(start_vertex)
print("DFS=",DFS_RESULT)

BFS(start_vertex)
print("BFS=", BFS_QUEUE)

