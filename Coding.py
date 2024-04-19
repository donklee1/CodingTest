# S1-1629 곱셈
from sys import stdin

A, B, C = map(int, input().split())

def power(A, B):
    global C
    if B == 1:
        return A % C
    
    x = power(A, B // 2)
    if (B % 2) == 0:
        return (x * x) % C
    else:
        return (x * x) * A % C

result = power(A, B)
print(result)