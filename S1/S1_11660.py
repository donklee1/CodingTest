# S1-11660 구간합5
from sys import stdin

N, M = map(int, input().split())
TABLE = []
# (0,0) 좌표를 사용하지 않는것이 계산에 편리함
DP_SUM = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N):
    L = list(map(int, stdin.readline().split()))
    TABLE.append(L)

for y in range(1, N+1):
    for x in range(1, N+1):
        # DP_SUM 좌표는 (0,0) 미사용 / TABLE 좌표는 0,0사용
        DP_SUM[y][x] = DP_SUM[y-1][x] + DP_SUM[y][x-1] - DP_SUM[y-1][x-1] + TABLE[y-1][x-1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, stdin.readline().split())
    part_sum = DP_SUM[y2][x2] - DP_SUM[y2][x1-1] - DP_SUM[y1-1][x2] + DP_SUM[y1-1][x1-1]
    print(part_sum)
