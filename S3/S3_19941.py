# 19941 S3
from sys import stdin

N, K = map(int, stdin.readline().split())
TABLE = list(stdin.readline())

count = 0
RESEVED = [False] * N
for i in range(N):
    if TABLE[i] == "P":
        for j in range(max(0, i-K), min(N, i+K+1), 1): # 
            if TABLE[j] == "H" and RESEVED[j] == False:
                RESEVED[j] = True
                count += 1
                break

print(count)