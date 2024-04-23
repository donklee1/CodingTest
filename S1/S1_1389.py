# S1_1389 케빈베이컨
from sys import stdin
import sys
from collections import deque

user_count, relation_count = map(int, stdin.readline().split())
GRAPH = [[] for _ in range(user_count+1)]
RELATION = [[0] * (user_count+1) for _ in range(user_count+1)]
for i in range(relation_count):
    man1, man2 = map(int, stdin.readline().split())
    GRAPH[man1].append(man2)
    GRAPH[man2].append(man1)

def BFS(root):
    q = deque()
    q.append(root)
    Visited[root] = 1
    while q:
        node = q.popleft()
        for a in GRAPH[node]:
            if Visited[a] == 0:
                # 단계가 증가될때마다 관계지수 증가
                Visited[a] = Visited[node] + 1
                q.append(a)


result = []
for i in range(1, user_count+1):
    Visited = [0] * (user_count+1)
    BFS(i)
    result.append(sum(Visited))

min_index = result.index(min(result))
print(min_index+1)
