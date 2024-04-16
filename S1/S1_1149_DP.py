# 1149 S1 RGB
from sys import stdin

N = int(input())
PRICE = [[0,0,0] for _ in range(N)]
for i in range(N):
    PRICE[i] = list(map(int, stdin.readline().split()))

for k in range(1, N):
    PRICE[k][0] = min(PRICE[k-1][1], PRICE[k-1][2]) + PRICE[k][0]
    PRICE[k][1] = min(PRICE[k-1][0], PRICE[k-1][2]) + PRICE[k][1]
    PRICE[k][2] = min(PRICE[k-1][0], PRICE[k-1][1]) + PRICE[k][2]

print(min(PRICE[N-1]))