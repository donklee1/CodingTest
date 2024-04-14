# 15686 G5
from sys import stdin
import itertools

N, MAX_STORE = map(int, stdin.readline().split())
CITY = [[0] * N for _ in range(N)]
STORE = []
HOUSE = []
for i in range(N):
    CITY[i] = list(map(int, stdin.readline().split()))
    for j in range(N):
        if CITY[i][j] == 1:
            HOUSE.append((i,j))
        if CITY[i][j] == 2:
            STORE.append((i,j))

STORE_CASE = itertools.combinations(STORE, MAX_STORE)
CASE_DIST = []
for store in STORE_CASE: # 치킨집 조합
    total_dist = 0
    for (hx, hy) in HOUSE:
        mindist = 50000
        for (sx, sy) in store: # 치킨집
            mindist = min(mindist, abs(sx - hx) + abs(sy - hy))
        total_dist += mindist
    CASE_DIST.append(total_dist)
print(min(CASE_DIST))
