# 15663 S2
from sys import stdin
import itertools

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort()
USE_FLAG = [False] * N
RESULT = []
FINAL_RESULT = []

def dfs(start):
    global N, M
    if (start > N):
        return
    if len(RESULT) == M:
        for a in RESULT:
            print(a, end=" ")
        print("")
        return
    
    for i in range(N):
        if USE_FLAG[i] == False:
            RESULT.append(DATA[i])
            USE_FLAG[i] = True
            dfs(i+1)
            RESULT.pop()
            USE_FLAG[i] = False

dfs(0)
