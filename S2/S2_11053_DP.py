# S2_11053 가장긴 증가하는 부분수열

N = int(input())
DATA = list(map(int, input().split()))
count_dp = [1] * N

for i in range(1, N):
    for k in range(i-1, -1, -1):
        if DATA[i] > DATA[k]:
            # 이전의 조건만족하는 경우와 비교한 최대값
            count_dp[i] = max(count_dp[i], count_dp[k] + 1)

print(max(count_dp))