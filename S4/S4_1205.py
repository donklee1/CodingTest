# 1205 S4 : 등수구하기
import heapq
score_count, my_score, limit = map(int, input().split())
if score_count > 0:
    data = list(map(int, input().split()))
else:
    data = []    
heap = []
max_loop = min(limit,len(data))
if max_loop > 0:
    for i in range(max_loop):
        heapq.heappush(heap, -data[i]) # 최대힙

# -------------------------------------
degree = 1
if len(heap) < limit:
    heapq.heappush(heap, -my_score) # 점수추가
elif my_score > -heap[-1]:
    heapq.heappush(heap, -my_score) # 점수추가
else:
    degree = -1
if degree != -1:
    while heap[0] != -my_score:
        degree += 1
        heapq.heappop(heap)
print(degree)        
