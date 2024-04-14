# 2630 분할정복
from sys import stdin
# 신기법 적용: 샘플 자동입력 --> 실전변환 (매번 입력할 필요없음)
DATA = ["1 1 0 0 0 0 1 1",
        "1 1 0 0 0 0 1 1",
        "0 0 0 0 1 1 0 0",
        "0 0 0 0 1 1 0 0",
        "1 0 0 0 1 1 1 1",
        "0 1 0 0 1 1 1 1",
        "0 0 1 1 1 1 1 1",
        "0 0 1 1 1 1 1 1"
        ]
#N = 8
N = int(input())
MAT = [[0] * N for i in range(N)]
for i in range(N):
    #MAT[i] = list(map(int, DATA[i].split()))
    MAT[i] = list(map(int, stdin.readline().split()))

#print(MAT)

COUNT = [0] * 2 # White, Blue Count
def Work(MAT, START_X, START_Y, LEN):
    #print("START_X=", START_X, "START_Y=", START_Y, "LEN=", LEN)
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
