# 1940 S4
from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())

DATA = list(map(int, stdin.readline().split()))
Used = [0] * N
count = 0
for i in range(N):
    if (Used[i] == 1):
        continue
    for j in range(N):
        if (Used[j] == 1) or (i == j):
            continue
        if (DATA[i] + DATA[j]) == M:
            Used[i] = 1
            Used[j] = 1
            count += 1

print(count)
