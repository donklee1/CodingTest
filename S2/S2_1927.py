# 1927 S2 최소 힙
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
            MIN_VAL = heapq.heappop(HEAP)
            print(MIN_VAL)
    else:
        heapq.heappush(HEAP, A)
