# 3085 S2 사탕게임
from sys import stdin

N = int(stdin.readline())
BOARD = []
for _ in range(N):
    line = list(stdin.readline().rstrip())
    BOARD.append(line)

def GetMaxCount(N, row, col):
    max_count = 1
    count = 1
    data = BOARD[row][0]
    for c in range(1, N): # 열증가
        if BOARD[row][c] == data:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
            data = BOARD[row][c]
    data = BOARD[0][col]
    count = 1
    for r in range(1, N):
        if BOARD[r][col] == data:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
            data = BOARD[r][col]
    #print("r,c", row, col, "result", max_count)
    return max_count

max_result = 0
for r in range(N): # 행
    result = GetMaxCount(N, r, 0)
    max_result = max(max_result, result)
for c in range(N): # 열
    result = GetMaxCount(N, 0, c)
    max_result = max(max_result, result)

for r in range(N): # 행
    for c in range(1, N):
        if BOARD[r][c-1] != BOARD[r][c]:
            #print(r, c-1, "<-->", r, c, " : ",BOARD[r][c-1], "<-->", BOARD[r][c])
            A , B = BOARD[r][c-1], BOARD[r][c] # 백업
            BOARD[r][c-1], BOARD[r][c] = BOARD[r][c], BOARD[r][c-1] # 교환
            result = GetMaxCount(N, r, c)
            max_result = max(max_result, result)
            result = GetMaxCount(N, r, c-1)
            max_result = max(max_result, result)
            BOARD[r][c-1], BOARD[r][c] = A , B

for c in range(N): # 열
    for r in range(1, N):
        if BOARD[r-1][c] != BOARD[r][c]:
            #print(r-1, c, "<-->", r, c, " : ", BOARD[r-1][c], "<-->", BOARD[r][c])
            A , B = BOARD[r-1][c], BOARD[r][c]
            BOARD[r-1][c], BOARD[r][c] = BOARD[r][c], BOARD[r-1][c] # 교환
            result = GetMaxCount(N, r-1, c)
            max_result = max(max_result, result)
            result = GetMaxCount(N, r, c)
            max_result = max(max_result, result)
            BOARD[r-1][c], BOARD[r][c] = A , B

print(max_result)