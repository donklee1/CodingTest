# S2_18770 좌표압축
from sys import stdin
import sys
sys.setrecursionlimit(10000)

N = int(stdin.readline())
LIST = list(map(int, stdin.readline().split()))

LIST2 = []
for i in range(N):
    LIST2.append((LIST[i], i, 0)) # 원본, 순서값, 압축좌표저장

LIST2.sort(key=lambda x: x[0])

# --- DP 방식으로 계산 ---
for i in range(1, N):
    if LIST2[i][0] > LIST2[i-1][0]:
        LIST2[i] = (LIST2[i][0], LIST2[i][1], LIST2[i-1][2]+1)
    else:
        LIST2[i] = (LIST2[i][0], LIST2[i][1], LIST2[i-1][2])

LIST2.sort(key=lambda x: x[1])
for i in range(N):
    print(LIST2[i][2], end=" ")
print("")