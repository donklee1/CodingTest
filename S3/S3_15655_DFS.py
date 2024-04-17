# 15655 S2
from sys import stdin
import itertools

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort()
RESULT = []

def dfs(start):
    global N, M
    if (start > N):
        return
    if len(RESULT) == M:
        print(*RESULT) # 리스트를 빠르게 출력하는 방법
        return
    
    for i in range(start, N):
            if len(RESULT) == 0 or (DATA[i] > RESULT[-1]):
                RESULT.append(DATA[i])
                dfs(i+1)
                RESULT.pop()

dfs(0)
