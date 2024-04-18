# S3-9375
from sys import stdin

N = int(stdin.readline())
for _ in range(N):
    cloth_count = int(stdin.readline())
    data_set = dict()
    for _ in range(cloth_count):
        name, type = stdin.readline().split()
        if type in data_set:
            data_set[type] += 1
        else:
            data_set[type] = 1

    count = 1
    for key in data_set:
        count *= (data_set[key]+1) # +1: 안 입는 경우 포함
    print(count-1) #알몸인 경우 제외
 
