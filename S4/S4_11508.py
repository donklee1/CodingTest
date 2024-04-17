# S4-11508
from sys import stdin

N = int(stdin.readline().rstrip())
MILK = []
for _ in range(N):
    MILK.append(int(stdin.readline().rstrip()))

MILK.sort(reverse=True)
price = 0
for i in range(N):
    if (i % 3) != 2:
        price += MILK[i]

print(price)        
