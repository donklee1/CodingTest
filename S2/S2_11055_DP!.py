# S2-11055 DP
from sys import stdin

N = int(stdin.readline().rstrip())
DATA = list(map(int, stdin.readline().split()))

DP_SUM = [0] * N
DP_SUM[0] = DATA[0]
for i in range(1, N):
    for k in range(i): # 0..i-1
        if DATA[i] > DATA[k]:
            # 주의 : 이전의 모든 데이터와의 합과 비교해야 함
            DP_SUM[i] = max(DP_SUM[i], DP_SUM[k] + DATA[i])
        else:
            # 현재 데이터가 기존합보다 큰 경우
            DP_SUM[i] = max(DP_SUM[i], DATA[i])

print(max(DP_SUM))