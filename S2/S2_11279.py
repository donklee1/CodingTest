# 11279 S2 최대 힙
from sys import stdin
import heapq

N = int(input())
HEAP = []
for _ in range(N):
    A = int(stdin.readline())
    if A == 0:
        if len(HEAP) == 0:
            print(0)
        else:
            MAX_VAL = -heapq.heappop(HEAP)
            print(MAX_VAL)
    else:
        heapq.heappush(HEAP, -A)
