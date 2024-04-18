# S2_15663 M과 N(9) 1~N M개, 이전 동일숫자 불가, 사전순
from sys import stdin
import itertools

N, M = map(int, input().split())
DATA = list(map(int, input().split()))
DATA.sort() # 사전순이므르 미리 정렬
USE_FLAG = [False] * N
RESULT = []

def dfs():
    global N, M
    if len(RESULT) == M:
        print(*RESULT) # 리스트를 빠르게 출력하는 방법
        return
    
    prev_data = 0
    for i in range(N):
        if (USE_FLAG[i] == False) and (prev_data != DATA[i]): # 이전데이터와 같지 않아야
            RESULT.append(DATA[i])
            prev_data = DATA[i]
            USE_FLAG[i] = True
            dfs()
            RESULT.pop()
            USE_FLAG[i] = False

dfs(0)
