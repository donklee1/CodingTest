# 14501 S3
N = int(input()) # 상담일 1= < N <= 15

T =  [0] * N # 상담기간날짜
P =  [0] * N # 상담금액
DP = [0] * (N+1)

for i in range(N):
    T[i], P[i] = map(int, input().split())
    DP[i] = P[i]
DP[N] = 0 # 마지막 하나더 추가

for k in range(N-1,-1,-1): # 역방향 진행
    if T[k] + k > N: # 날짜초과
        DP[k] = DP[k+1]
    else:
         # 회의 안하는것(DP[k+1]): 회의하는것(P[k]+DP[k + T[k])의 최대값
        DP[k] = max(DP[k+1], P[k]+DP[k + T[k]])
print(DP[0])