# S2_1138 한줄로 서기
from sys import stdin

N = int(stdin.readline())
DATA = list(map(int, stdin.readline().split()))
RESULT = [0] * N

for i in range(N):
    skip_count = DATA[i]
    num = i + 1 # 대상의 숫자
    count = 0
    for j in range(N):
        # 숫자보다 큰경우, 또는 빈경우 카운트 증가하여 조건판단 
        if RESULT[j] == 0 and count == skip_count:
            RESULT[j] = num # 조건만족
            break
        elif RESULT[j] == 0:
            count += 1

print(*RESULT)
