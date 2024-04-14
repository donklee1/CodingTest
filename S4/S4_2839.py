# 2839 S4
from sys import stdin

N = int(input())
min_count = 5000
Found = False
for x in range(0, (N // 3)+1): # 3K 봉지
    for y in range(0, (N // 5)+1): # 5K 봉지
        Weight = x * 3 + y * 5
        if Weight == N:
            Found = True
            if (x + y) < min_count:
                min_count = x + y

if Found == False:
    print(-1)
else:
    print(min_count)
