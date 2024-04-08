# 2579 S3
from sys import stdin

count = int(stdin.readline())
STEP = []
for i in range(count):
    val = int(stdin.readline().rstrip())
    STEP.append(val)

DP_MAXVAL = [0] * count
ONE_COUNT = [0] * count

DP_MAXVAL[0] = STEP[0]
ONE_COUNT[0] = 1

for i in range(1, count):
    max_val = 0
    if (ONE_COUNT[i-1] < 2):
        max_val = DP_MAXVAL[i-1] + STEP[i]
        ONE_COUNT[i] = ONE_COUNT[i-1] + 1
    if (i >= 2) and ((DP_MAXVAL[i-2]) + STEP[i] > max_val):
        max_val = DP_MAXVAL[i-2] + STEP[i]
        ONE_COUNT[i] = 0
    DP_MAXVAL[i] = max_val
    print("i=", i, "ONE=", ONE_COUNT, "DP=", DP_MAXVAL)
    
print(DP_MAXVAL[count-1])
