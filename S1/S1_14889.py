import itertools

DATA = ["0 1 2 3 4 5",
        "1 0 2 3 4 5",
        "1 2 0 3 4 5",
        "1 2 3 0 4 5",
        "1 2 3 4 0 5",
        "1 2 3 4 5 0"]

N = int(input())
#N = 6
SCORE = [[0] * N for _ in range(N)]
for j in range(N):
    S = list(map(int, input().split()))
    #S = list(map(int, DATA[j].split()))
    SCORE[j] = S

MAN = range(N)
TEAM = list(itertools.combinations(MAN, N // 2))
#print(TEAM)

min_diff = 50000
for T1 in TEAM:
   T2 = list(set(MAN) - set(T1))
   
   sum1 = 0
   for i in T1:
     for j in T1:
          if i != j:
               sum1 += SCORE[i][j]
   sum2 = 0
   for i in T2:
     for j in T2:
          if i != j:
               sum2 += SCORE[i][j]
   diff = abs(sum1-sum2)
   #print(sum1, sum2, "diff=", diff)
   if diff < min_diff:
     min_diff = diff
print(min_diff)
