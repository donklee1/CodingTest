# 11051 S2
from sys import stdin

def Factorial(N):
    result = 1
    if (N < 2):
        return result
    for i in range(2, N+1):
        result *= i
    return result

N, K = map(int, stdin.readline().split())
nCr = Factorial(N) // (Factorial(K) * Factorial(N-K))# 주의 / 나누면 틀림!!
print(int(nCr) % 10007)
