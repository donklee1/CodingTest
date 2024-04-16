# 2630 분할정복
from sys import stdin
N = int(input())
MAT = [[0] * N for i in range(N)]
for i in range(N):
    MAT[i] = list(map(int, stdin.readline().split()))

COUNT = [0] * 2 # White, Blue Count
def Work(MAT, START_X, START_Y, LEN):
    global COUNT
    # 영역이 모두 같은색인가 ?
    same = True
    first_data = int(MAT[START_X][START_Y])
    if LEN == 1:
        same = True
    else:
        for x in range(START_X, START_X+LEN):
            for y in range(START_Y, START_Y+LEN):
                if first_data != MAT[x][y]:
                    same = False # 다름
                    break
            if same == False:
                break
    if same == True:
        COUNT[first_data] += 1
    else:
        LEN = LEN // 2 # 8 --> 4 --> 2
        Work(MAT, START_X, START_Y, LEN)
        Work(MAT, START_X, START_Y+LEN, LEN)
        Work(MAT, START_X+LEN, START_Y, LEN)
        Work(MAT, START_X+LEN, START_Y+LEN, LEN)

Work(MAT, 0, 0, N)
print(COUNT[0])
print(COUNT[1])
