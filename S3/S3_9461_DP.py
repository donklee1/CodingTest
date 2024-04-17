T = int(input())
P = [0] * (101)
P[1] = 1
P[2] = 1
P[3] = 1
for k in range(4, 101):
    P[k] = P[k-2] + P[k-3]

for _ in range(T):
    N = int(input())
    print(P[N])
