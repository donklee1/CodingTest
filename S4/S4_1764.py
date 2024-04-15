# S4_1764 듣보잡 : 교집합
from sys import stdin
NoHear = set()
NoSee = set()

N, M = map(int, input().split())
for i in range(N):
    NAME = stdin.readline().rstrip()
    NoHear.add(NAME)
for i in range(M):
    NAME = stdin.readline().rstrip()
    NoSee.add(NAME)

NoHearSee = NoHear & NoSee # 교집합
RESULT = list(NoHearSee)    
RESULT.sort()

count = len(RESULT)
print(count)
for i in range(count):
    print(RESULT[i])
