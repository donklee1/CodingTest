# 1759 G5
from sys import stdin
import itertools

L, C = map(int, input().split())
DATA = list(input().split())
DATA.sort()

COMB = itertools.combinations(DATA, L)

for psw in COMB:
    mo_count = 0
    ja_count = 0
    for al in psw:
        if al in "aeiou":
            mo_count += 1
        else:
            ja_count += 1
    
    if mo_count >= 1 and ja_count >= 2:
        print("".join(psw)) # 붙여서 출력해야함
