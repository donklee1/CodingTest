# 1003 S3

#----------------------------------------------
ZERO = [0] * 41
ONE = [0] * 41

ZERO[0] = 1
ONE[0] = 0
ZERO[1] = 0
ONE[1] = 1
for k in range(2, 41):
    ZERO[k] = ZERO[k-2] + ZERO[k-1]
    ONE[k] = ONE[k-2] + ONE[k-1]

T = int(input())
for _ in range(T):
    N = int(input())
    print(ZERO[N], ONE[N])
