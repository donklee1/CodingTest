# S2_2805 나무자르기
from sys import stdin

tree_count, wood_required = map(int, stdin.readline().split())
TREE = list(map(int, stdin.readline().split()))

start, end = 1, max(TREE)

while start <= end: # 부등호 <=
    mid = (start + end) // 2

    wood_sum = 0
    for height in TREE: 
        if height > mid:
            wood_sum += height - mid
    if wood_sum < wood_required: # 작음 --> 영역을 큰쪽으로
        end = mid - 1
    else: # 큼 --> 영역을 
        start = mid + 1

print(end)
