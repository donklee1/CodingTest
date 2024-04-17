# 2193 S3
from sys import stdin

N = int(stdin.readline().strip())

DP = [1,1,2]

if (N < 3):
    print(DP[N-1])
    exit(0)
for k in range(3, N):
    DP.append(DP[k-2] + DP[k-1])

print(DP[-1])
