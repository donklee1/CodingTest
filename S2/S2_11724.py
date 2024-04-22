# S2_11724 연결요소의 개수
from sys import stdin
import sys
sys.setrecursionlimit(10000)

vertex_count, edge_count = map(int, stdin.readline().split())
TREE = [[] for _ in range(vertex_count+1)]
for i in range(edge_count):
    start, end = map(int, stdin.readline().split())
    TREE[start].append(end)
    TREE[end].append(start)

Visited = [False] * (vertex_count+1)

def DFS(node):
    if Visited[node] == True:
        return
    Visited[node] = True
    for a in TREE[node]:
        if Visited[a] == False:
            DFS(a)

item_count = 0
for i in range(1, vertex_count+1):
    if Visited[i] == False:
        DFS(i)
        item_count += 1

print(item_count)
