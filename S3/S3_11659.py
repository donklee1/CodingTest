from sys import stdin
N, M = map(int, input().split())
LIST = list(map(int, input().split()))

# SUM = 0 --> 시간초과 방법
# for a in range(i, j+1):
#     SUM += LIST[a-1]
# print(SUM)
    
SLIST = [0] * N
for k in range(N+1): # 누적합을 배열에 계산
    if k == 1:
        SLIST[0] =LIST[0]
    else:
        SLIST[k-1] = SLIST[k-2] + LIST[k-1]

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    i2 = i - 1
    j2 = j - 1
    if i2 == 0:
        SUM = SLIST[j2]
    else:
        SUM = SLIST[j2] - SLIST[i2-1]
    print(SUM)        
