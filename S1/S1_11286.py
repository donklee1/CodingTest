# 11286 S1 절대값 힙
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
            (ABS_VAL, VAL) = heapq.heappop(HEAP)
            print(VAL)
    else:
        heapq.heappush(HEAP, (abs(A), A))
