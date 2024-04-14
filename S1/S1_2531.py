# 2531 s1
from sys import stdin

dish_count, max_susi, discount_dishs, cuppon = map(int, stdin.readline().split())
SUSI = []
for i in range(dish_count):
    SUSI.append(int(stdin.readline().rstrip()))

max_case = 0
for i in range(dish_count):
    MY_DISH = set()
    for k in range(discount_dishs):
        dish_no = (i + k) % dish_count # 넘치는 경우 고려
        MY_DISH.add(SUSI[dish_no])
    MY_DISH.add(cuppon) # 공짜 쿠폰
    max_case = max(max_case, len(MY_DISH))
    if (max_case > discount_dishs): # 더이상 진행 필요없음
        break

print(max_case)