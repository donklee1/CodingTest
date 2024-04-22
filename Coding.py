# S2_2805 나무자르기
from sys import stdin

tree_count, required_height = map(int, stdin.readline().split())
TREE = list(map(int, stdin.readline().split()))

wood_min  = 1
wood_max = max(TREE)
while wood_min <= wood_max: # 이진검색
    wood_mid = (wood_min + wood_max) // 2
    wood_sum = 0
    for h in TREE:
        if h > wood_mid:
            wood_sum += (h - wood_mid)
    if wood_sum < required_height:
        wood_max = wood_mid - 1
    else:
        wood_min = wood_mid + 1
print(wood_max)