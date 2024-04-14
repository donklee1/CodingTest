# 1932 S1 정수삼각형
from sys import stdin

N = int(stdin.readline().strip())
DP = [0] * N
DP[0] = int(stdin.readline())
PREV_DP = list(DP)
for i in range(1, N):
    NUM = list(map(int, stdin.readline().split()))
    DP[0] = PREV_DP[0] + NUM[0] # 첫번째 수
    for k in range(1, i):
        DP[k] = max(PREV_DP[k-1]+NUM[k], PREV_DP[k]+NUM[k]) # 중간값
    DP[i] = PREV_DP[i-1] + NUM[i] # 마지막 수
    #print("i=", i, "NUM=", NUM, "DP=", DP)
    PREV_DP = list(DP)

print(max(DP))    

