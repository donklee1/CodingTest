# S4_2217 로프의 최대중량
import sys
N = int(input())
MAX_WEIGHT = [] # 버틸 수 있는 최대중량
for i in range(N):
    MAX_WEIGHT.append(int(input()))

MAX_WEIGHT.sort(reverse=True) #내림차순 (강도가 강한 루프우선)

max_val = 0
for i in range(N):
    weight = MAX_WEIGHT[i]
    # 하나의 루프를 사용하는 경우 - 가장강도가 센 중량
    # 복수개의 루프를 사용하는 경우 - 가장약한 강도를 기준으로 
    max_val = max(max_val, weight * (i+1))

print(max_val)

