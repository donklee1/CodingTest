# 1205 S4 : 등수구하기
import heapq
score_count, my_score, rank_limit = map(int, input().split())
if score_count > 0:
    score_data = list(map(int, input().split()))
else:
    score_data = []    
ranking_heap = []
max_loop = min(rank_limit,len(score_data))
if max_loop > 0:
    for i in range(max_loop):
        heapq.heappush(ranking_heap, -score_data[i]) # 최대힙(음수로 저장)

# -------------------------------------
degree = 1
if len(ranking_heap) < rank_limit: #빈공간 있는경우
    heapq.heappush(ranking_heap, -my_score) # 점수추가
elif my_score > -ranking_heap[-1]: #마지막등수 이상
    heapq.heappush(ranking_heap, -my_score) # 점수추가
else:
    degree = -1
if degree != -1:
    while ranking_heap[0] != -my_score:
        degree += 1
        heapq.heappop(ranking_heap)
print(degree)