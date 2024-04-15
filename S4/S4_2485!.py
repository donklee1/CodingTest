# S4_2485
import math
from functools import reduce

N = int(input()) # 가로수 개수
GAP = [] # 간격
PREV_P = 0
for i in range(N):
    P = int(input())
    if i > 0:
        GAP.append(P - PREV_P) # 간격
    PREV_P = P

final_gcd = reduce(math.gcd, GAP) # 모든간격의 최대공약수

count = 0
for gap in GAP:
    if gap > final_gcd:
        count += (gap // final_gcd) - 1

print(count)
