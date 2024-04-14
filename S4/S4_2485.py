import math
from functools import reduce

N = int(input()) # 가로수 개수
GAP = []
PREV_P = 0
for i in range(N):
    P = int(input())
    if i > 0:
        GAP.append(P-PREV_P) # 간격
    PREV_P = P

#GCD_VAL = math.gcd(GAP) # 리스트의 gcd --> Error
GCD_VAL = reduce(math.gcd, GAP)

count = 0
for G in GAP:
    if G > GCD_VAL:
        count += (G // GCD_VAL) - 1

print(count)        
