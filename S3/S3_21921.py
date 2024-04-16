# 21921 S3 누적합, DP
from sys import stdin

N, X = map(int, stdin.readline().split()) # X일간 가장많이 들어온 방문자, 기간개수
PEOPLES = list(map(int, stdin.readline().split())) #방문자수

SUBSUM = [0] * N
SUBSUM[0] = PEOPLES[0]
for i in range(1, X):
    SUBSUM[i] = SUBSUM[i-1] + PEOPLES[i] #누적합
same_count = 1
max_sum = SUBSUM[X-1]
for i in range(X, N):
    SUBSUM[i] = SUBSUM[i-1] + PEOPLES[i] #누적합
    part_sum = SUBSUM[i]-SUBSUM[i-X] # 최근 X일간 방문자수합계
    if part_sum > max_sum:
        max_sum = part_sum
        same_count = 1
    elif part_sum == max_sum:
        same_count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(same_count)
