from sys import stdin
N, K = map(int, input().split())
LIST = list(map(int, input().split()))

SLIST = [0] * (N-K+1)
for day in range(N-K+1): # 누적합을 배열에 계산
    if day == 0:
        SUM = 0
        for i in range(K):
            SUM += LIST[i]
        SLIST[0] = SUM    
    else:
        # 이전합 - 이전날온도 + 마지막날 온도
        SLIST[day] = SLIST[day-1] - LIST[day-1]+ LIST[day+K-1]

#print(SLIST)
print(max(SLIST))
