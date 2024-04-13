# 1669 S2 제곱수의 합
from sys import stdin
import math

N = int(input())

DP = [0] * (N+1)
DP[1] = 1
for i in range(2, N + 1):
    DP[i] = i # 최대회수로 시작
    for j in range(1, int(math.sqrt(i) + 1)):  # 1, 4, 9, 16..
        square = j * j
        if (DP[i - square] + 1) < DP[i]: # 이전결과에 1더한것과 최소값 반복
            DP[i] = DP[i - square] + 1

print(DP[N])