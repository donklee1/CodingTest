# 1912 S2
from sys import stdin
#N = 10 #샘플
#L = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1] #샘플
N = int(input())
L = list(map(int, stdin.readline().split()))
DP = [0] * N

DP[0] = L[0]
for i in range(1, N):
    DP[i] = max(L[i], DP[i-1]+L[i])

print(max(DP))
