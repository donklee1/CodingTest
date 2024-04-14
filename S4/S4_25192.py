# S4_25192 곰곰이
from sys import stdin
N = int(input())

SET = set()
count = 0
for _ in range(N):
    NAME = stdin.readline().rstrip()
    if NAME == "ENTER":
        SET = set() # CLEAR
        continue
    if (NAME in SET) == False: # 한번만
        SET.add(NAME)
        count += 1

print(count)