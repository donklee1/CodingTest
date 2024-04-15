# 11399 ATM : 최소대기 GREDY
from sys import stdin
N = input().rstrip()
T = list(map(int, input().split())) # 대기시간
T.sort() # 대기 짧은 사람우선

TOTAL_TIME = 0
WAIT_TIME  = 0
for t in T:
    WAIT_TIME += t
    TOTAL_TIME += WAIT_TIME
print(TOTAL_TIME)
