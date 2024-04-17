# 2579 S3
from sys import stdin

count = int(stdin.readline())
STEP = [0] # 시작위치
for i in range(count):
    val = int(stdin.readline().rstrip())
    STEP.append(val)

DP_MAXVAL = [0] * (count + 1)

DP_MAXVAL[0] = 0 # 계산을 위해 미사용
if (count == 1): # 예외처리
    print(STEP[1])
    exit(0)
if (count == 2): # 예외처리
    print(STEP[1]+STEP[2])
    exit(0)

DP_MAXVAL[1] = STEP[1]
DP_MAXVAL[2] = STEP[1] + STEP[2]
for i in range(3, count+1):
    # 전계단을 밟은 경우 : DP_MAXVAL[i-3]+STEP[i-1]+STEP[i] 
    # -- 주의 연속해서 3회 불가능하므로 DP_MAXVAL[i-3] 더해야 함 (역방향으로 생각해야 함)
    # 전전계단을 밟은 경우 : DP_MAXVAL[i-2]+STEP[i]
    DP_MAXVAL[i] = max(DP_MAXVAL[i-3]+STEP[i-1]+STEP[i], DP_MAXVAL[i-2]+STEP[i])
    
print(DP_MAXVAL[count])
