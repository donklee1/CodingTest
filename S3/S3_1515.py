# 1515 S3
from sys import stdin

S = stdin.readline().rstrip()

N = 1
while len(S) > 0:
    str_n = str(N)
    if S.startswith(str_n):
        S = S.replace(str_n, "", 1) # 한문자만 지움
    else: #부분일치 하는지 확인
        if len(str_n) > 1:
            for part in str_n:
                if S.startswith(part):
                    S = S.replace(part, "", 1) # 한문자만 지움
    if len(S) == 0:
        break
    N += 1

print(N)