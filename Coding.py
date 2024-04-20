# G5-1916 최소비용 (dijkstra)
from sys import stdin
import sys
import heapq

# ----------------------------------------------------
def dijkstra1(graph, start): # dict() of dict() 사용버젼
  dist_list = [int(1e9)] * len(graph)  # 처음 초기값은 무한대
  dist_list[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [dist_list[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    dist, node = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if dist_list[node] < dist:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for next_node, next_dist in graph[node].items():
      distance = dist + next_dist  # 해당 노드를 거쳐 갈 때 거리
      if distance < dist_list[next_node]:  # 알고 있는 거리 보다 작으면 갱신
        dist_list[next_node] = distance
        heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
  return dist_list

# ----------------------------------------------------
def dijkstra2(graph, start): # list of list
    dist_list = [int(1e9)] * len(graph)  # 처음 초기값은 무한대
    dist_list[start] = 0  # 시작 노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [dist_list[start], start])  # 시작 노드부터 탐색 시작

    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        (dist, node) = heapq.heappop(queue)  # 탐색할 노드, 거리
        if dist_list[node] < dist: # 기존 최단거리보다 멀다면 무시
            continue

        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < dist_list[next_node]:  # 기존 거리 보다 짧으면 갱신
                dist_list[next_node] = distance
                heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return dist_list

# ----------------------------------------------------
city_count = int(stdin.readline())
bus_count = int(stdin.readline())
graph1 = dict()
for i in range(city_count+1):
   graph1[i] = dict() # 비어있는 dict로 초기화
graph2 = [[] for _ in range(city_count+1)]

for i in range(bus_count):
     start, end, price = map(int, stdin.readline().split())
     if start in graph1:
         sub_graph = graph1[start]
         sub_graph[end] = price
     graph2[start].append((end, price))

target_start, target_end = map(int, stdin.readline().split())
dist1 = dijkstra1(graph1, target_start)
dist2 = dijkstra2(graph2, target_start)
print("graph=", graph1)
print("dist1=", dist1)
print("graph2=", graph2)
print("dist2=", dist2)
print(dist1[target_end])
print(dist2[target_end])
