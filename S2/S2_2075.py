# 2075 S2 N번째 큰수
from sys import stdin
import heapq

N = int(stdin.readline())
DATA = [0] * N
heap = []

for i in range(N):
    DATA = list(map(int, stdin.readline().split()))
    for x in DATA:
        if len(heap) < N: # 힙의 크기를 N개 이하로 유지
            heapq.heappush(heap, x)
        else:
            if (heap[0] < x): # 큰값이 들어올때만
                heapq.heappop(heap)
                heapq.heappush(heap, x)

print(heap[0]) # N번째