# 11047 GREEDY 최소동전개수
from sys import stdin

N, K = map(int, stdin.readline().split())
COIN = []
for _ in range(N):
    M = int(stdin.readline())
    COIN.append(M) # 동전종류 저장

count = 0
while K > 0:
    for M in range(N-1, -1, -1): # 고액권 우선
        EA = K // COIN[M]
        if EA > 0:
            K -= COIN[M]*EA
            count += EA

print(count)
