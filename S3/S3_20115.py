# 20115 S3
from sys import stdin

count = int(stdin.readline().rstrip())
drink_qty = list(map(int, stdin.readline().split()))
drink_qty.sort(reverse=True)

result = drink_qty[0]
for i in range(1, count):
    result += drink_qty[i] / 2

if (result == int(result)):
    print(int(result))
else:
    print(result)
