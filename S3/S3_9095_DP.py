# 9095 S3

DP = [0] * 11
DP[1] = 1 # (1)
DP[2] = 2 # (1+1, 2)
DP[3] = 4 # (1+1+1, 1+2, 2+1, 3)

for k in range(4, 11):
    DP[k] = DP[k-1] + DP[k-2] + DP[k-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(DP[N])
