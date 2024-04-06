# 3474 S3
from sys import stdin

T = int(input())
for _ in range(T):
    N = int(input())

    count = 0
    i = 5
    while i <= N: # 5, 10, 15, 20 ...
        count += N // i # 5의 개수누적
        i *= 5

    print(count)