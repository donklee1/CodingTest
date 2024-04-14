# 11727

N = int(input())
DP = [0] * 1001

DP[1] = 1
DP[2] = 3
if N > 2:
    for k in range(3, N+1):
        DP[k] = DP[k-2] * 2 + DP[k-1]

print(DP[N] % 10007)
