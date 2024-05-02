# S1_20529
from sys import stdin

def make_tuple(s):
    return (s, 1000)

T = int(input())
N = int(input())
MBTI = list(map(make_tuple, stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        M1 = MBTI[i][0]
        man_dist = MBTI[i][1]
        M2 = MBTI[j][0]
        for k in range(4):
            if M1[k] != M2[k]:
                man_dist += 1
        MBTI[i] = (MBTI[i][0], man_dist)

MBTI.sort(key = lambda x:x[1])
print(MBTI)