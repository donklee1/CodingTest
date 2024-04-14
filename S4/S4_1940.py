# 1940 S4
from sys import stdin

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())

DATA = list(map(int, stdin.readline().split()))
Used = [0] * N
count = 0

def BrutrForce():
    global count
    for i in range(N):
        if (Used[i] == 1):
            continue
        for j in range(N):
            if (Used[j] == 1) or (i == j):
                continue
            if (DATA[i] + DATA[j]) == M:
                Used[i] = 1
                Used[j] = 1
                count += 1

def TwoPointer(start, end, M):
    global count
    while start < end:
        if (DATA[start] + DATA[end]) == M:
            count += 1
            start += 1
            end -= 1
        elif (DATA[start] + DATA[end]) < M:
            start += 1
        elif (DATA[start] + DATA[end]) > M:
            end -= 1

# BrutrForce() # 968 ms
DATA.sort()
TwoPointer(0, N-1, M) # 52ms
print(count)
