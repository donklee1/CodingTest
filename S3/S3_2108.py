# 통계학 2108
from sys import stdin
N = int(input())
L = []
for _ in range(N):
    L.append(int(stdin.readline()))

L.sort()
COUNT = [0] * (4001*2) # -4000.. 0 .. 4000
SUM = 0
for v in L:
    SUM += v
    COUNT[v+4000] += 2

MAX_FREQ = max(COUNT)
MAX_FREQ_LIST = []
for i, v in enumerate(COUNT):
    if MAX_FREQ == v:
        MAX_FREQ_LIST.append(i-4000)

print(round(SUM / N)) # 평균값
index = (int)((N+1)/2)-1
print(L[index]) # 중앙값
if len(MAX_FREQ_LIST) < 2:
    print(MAX_FREQ_LIST[0]) # 최빈값
else:
    print(MAX_FREQ_LIST[1])
#print("FREQ=", MAX_FREQ_LIST)
print(L[-1]-L[0]) # 범위

