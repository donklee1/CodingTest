# S3-2606 바이러스
from sys import stdin
import sys
import heapq

# ----------------------------------------------------
def virus(graph, start): # list of list
    global virus_status
    queue = []
    virus_status[start] = True
    heapq.heappush(queue, start)  # 시작 노드부터 탐색 시작
    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        node = heapq.heappop(queue)
        for next_node in graph[node]:
          if virus_status[next_node] == False:
            virus_status[next_node] = True
            heapq.heappush(queue, next_node)

# ----------------------------------------------------
pc_count = int(stdin.readline())
link_count = int(stdin.readline())
graph= [[] for _ in range(pc_count+1)]
virus_status = [False] * (pc_count + 1)

for i in range(link_count):
     pc1, pc2 = map(int, stdin.readline().split())
     graph[pc1].append(pc2)
     graph[pc2].append(pc1) # 양방향 연결주의!

virus(graph, 1)
print(virus_status.count(True)-1)

