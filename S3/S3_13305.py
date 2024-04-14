# 13305 S3
from sys import stdin

city_count = int(stdin.readline().rstrip())
DISTANCE = list(map(int, stdin.readline().split()))
PRICE = list(map(int, stdin.readline().split()))

min_price = PRICE[0] # 처음에 무조건 넣어야 함
price = min_price * DISTANCE[0]
for i in range(1, city_count-1): # i 번째까지 기름을 넣는경우
    if PRICE[i] < min_price: # 이전주유소 보다 싼 경우
        min_price = PRICE[i]
    price += DISTANCE[i] * min_price

print(price)
