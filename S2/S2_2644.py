# S2_2644 촌수계산
from sys import stdin
from collections import deque

people_count = int(stdin.readline().rstrip())
p1, p2 = map(int, stdin.readline().split())
relation_count = int(stdin.readline().rstrip())
GRAPH = [[] for _ in range(people_count+1)]
Visited = [False] * (people_count+1)
for i in range(relation_count):
    parent, child = map(int, stdin.readline().split())
    GRAPH[parent].append(child)
    GRAPH[child].append(parent)

q = deque()
q.append((p1, 0))
result = 0
Visited[p1] = True
Found = False
while (q):
    (people, rel) = q.popleft()
    if people == p2:
        result = rel
        Found = True
        break
    for child in GRAPH[people]:
        if Visited[child] == False:
            Visited[child] = True
            q.append((child, rel+1))
    result += 1

if Found == False:
    print(-1)
else:
    print(result)
