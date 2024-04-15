# 2839 S4 설탕봉지
from sys import stdin

def BruteForce(N):
    min_count = 5000
    Found = False
    for x in range(0, (N // 3)+1): # 3K 봉지
        for y in range(0, (N // 5)+1): # 5K 봉지
            Weight = x * 3 + y * 5
            if Weight == N:
                Found = True
                if (x + y) < min_count:
                    min_count = x + y
    if Found == False:
        return -1
    else:
        return min_count

def Solution(N):
    count = 0
    while N > 0:
        if N % 5 == 0:  # 5으로 나눠떨어질 때
            count += N // 5
            break
        N -= 3
        count += 1
        if N == 0:
            break
        elif N == 1 or N == 2:
            count = -1
            break
    return count

N = int(input())
# print(BruteForce(N)) #336ms
print(Solution(N)) #44ms
