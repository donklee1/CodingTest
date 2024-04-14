# 11047 GREEDY
from sys import stdin

N, K = map(int, stdin.readline().split())
COIN = []
for _ in range(N):
    M = int(stdin.readline())
    COIN.append(M)

count = 0
while K > 0:
    for M in range(N-1, -1, -1):
        EA = K // COIN[M]
        if EA > 0:
            K -= COIN[M]*EA
            count += EA

print(count)

