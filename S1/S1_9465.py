# 9465 S1
from sys import stdin

test_case = int(stdin.readline().rstrip())
Up = 0
Dn = 1
for _ in range(test_case):
    n = int(stdin.readline().rstrip())
    STICKER = []
    STICKER.append(list(map(int, stdin.readline().split())))
    STICKER.append(list(map(int, stdin.readline().split())))
    DP = [[0] * n for _ in range(2)]

    DP[Up][0] = STICKER[Up][0]
    DP[Dn][0] = STICKER[Dn][0]
    if n > 1:
        DP[Up][1] = DP[Dn][0] + STICKER[Up][1] #대각선
        DP[Dn][1] = DP[Up][0] + STICKER[Dn][1] #대각선
        if n > 2:
            for k in range(2, n):
                # 이전의 대각선 값과 이전이전의 대각선 값의 최대를 선택함
                DP[Up][k] = max(DP[Dn][k-1], DP[Dn][k-2]) + STICKER[Up][k]
                DP[Dn][k] = max(DP[Up][k-1], DP[Up][k-2]) + STICKER[Dn][k]
    print(max(DP[Up][n-1], DP[Dn][n-1]))
