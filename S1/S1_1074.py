# S1_1074 DFS
from sys import stdin
import sys
sys.setrecursionlimit(500000)

N, r,c  = map(int, stdin.readline().split())
def DFS(N, r, c):
    global count
    qurter_size = (2 ** N) * (2 ** N) // 4
    mid_pos = (2 ** N) // 2
    if c < mid_pos and r < mid_pos: # 좌상
        pass
    elif c >= mid_pos and r < mid_pos: # 우상
        count += qurter_size
    elif c < mid_pos and r >= mid_pos: # 좌하
        count += qurter_size * 2
    elif c >= mid_pos and r >= mid_pos: # 우하
        count += qurter_size * 3
    if N > 1:
        DFS(N-1, r % mid_pos, c % mid_pos)

count = 0
DFS(N, r,c)
print(count)
