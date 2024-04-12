# 21921 S3
from sys import stdin

N, X = map(int, stdin.readline().split())
PEOPLES = list(map(int, stdin.readline().split()))

SUBSUM = [0] * N
SUBSUM[0] = PEOPLES[0]
for i in range(1, X):
    SUBSUM[i] = SUBSUM[i-1] + PEOPLES[i]
same_count = 1
max_sum = SUBSUM[i]
for i in range(X, N):
    SUBSUM[i] = SUBSUM[i-1] + PEOPLES[i]
    part_sum = SUBSUM[i]-SUBSUM[i-X]
    if part_sum > max_sum:
        max_sum = part_sum
        same_count = 1
    elif part_sum == max_sum:
        same_count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(same_count)
