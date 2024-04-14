# 1931 GREEDY
from sys import stdin
def in_range(n, start, end = 0):
    return start <= n <= end if end >= start else end <= n <= start

N = int(input()) # 회의수
MEETING = []
for _ in range(N):
    START, END = map(int, stdin.readline().split())
    MEETING.append((START, END))

MEETING.sort(key=lambda x: (x[1], x[0])) # 종료시간, 시작시간
count = 0
LAST_END = 0
for (START, END) in MEETING:
    if START >= LAST_END: # 시간배정 가능한 경우
        count += 1
        LAST_END = END

print(count)
