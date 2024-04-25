# S1_5525 IOIOI
from sys import stdin

N = int(stdin.readline().strip())
M = int(stdin.readline().strip())
S = stdin.readline().strip()
result = 0
pos = 0
OI_count = 0
while pos < (M - 1):
    if S[pos:pos + 3] == 'IOI': #3칸
        pos += 2 # 다음의 I위치로
        OI_count += 1
        if OI_count == N:
            result += 1
            OI_count -= 1 # 직전상태로 !!
    else:
        pos += 1
        OI_count = 0

print(result)
