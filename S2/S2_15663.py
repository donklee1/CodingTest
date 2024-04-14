# 15663 S2
from sys import stdin
import itertools

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort()
USE_FLAG = [False] * N
RESULT = []

def dfs(start):
    global N, M
    if (start > N):
        return
    if len(RESULT) == M:
        print(*RESULT) # 리스트를 빠르게 출력하는 방법
        return
    
    prev_data = 0
    for i in range(N):
        if (USE_FLAG[i] == False) and (prev_data != DATA[i]): # 이전데이터와 같지 않아야
            RESULT.append(DATA[i])
            prev_data = DATA[i]
            USE_FLAG[i] = True
            dfs(i+1)
            RESULT.pop()
            USE_FLAG[i] = False

dfs(0)
