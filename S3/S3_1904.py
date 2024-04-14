# DP 문제 (1. 배열사용(순차적 계산가능한 경우), 2. dict: 불연속 특정함수 값)
N = int(input())
ARR = [0] * 1000001
ARR[1] = 1
ARR[2] = 2
for i in range(3, N+1):
    ARR[i] = (ARR[i-1] + ARR[i-2]) % 15746
print(ARR[N])  
