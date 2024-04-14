# 1463 S3

N = int(input())
DP = [0] * (N+1)
DP[1] = 0 # 1은 목표값이므로, 연산필요없음: 0
for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3]+1) # 3로 나눈것과 -1한것 비교
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2]+1) # 2로 나눈것과 -1한것 비교

print(DP[N])
