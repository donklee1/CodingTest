# S2-11725
from sys import stdin
import sys
sys.setrecursionlimit(100000)

N = int(stdin.readline().rstrip())
GRAPH = [[] for _ in range(N+1)] # 비어있는 2차원
P_NODE = [] # dict 방식은 메모리 낭비
Visited = [False] * (N+1)
for _ in range(N-1):
    n1, n2 = map(int, stdin.readline().split())
    GRAPH[n1].append(n2) #인접리스트 방식
    GRAPH[n2].append(n1) #인접리스트 방식
 
def def_findParent(p_node):
    Visited[p_node] = True
    for node in GRAPH[p_node]:
        if Visited[node] == False:
            Visited[node] = True
            P_NODE.append((node, p_node))
            def_findParent(node)

def_findParent(1)
P_NODE.sort(key = lambda x: x[0])
print(P_NODE)
for child, parent in P_NODE:
    print(parent)