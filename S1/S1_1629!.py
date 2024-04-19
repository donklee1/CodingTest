# S1-1629
from sys import stdin

A, B, C = map(int, stdin.readline().split())

def power(A, B):
    global C
    if B == 1:
        return A % C
    else:
        x = power(A, B // 2)
        if B % 2 == 0: # 짝수
            return (x * x) % C
        else:
            return (x * x * A) % C

result = power(A, B)
print(result)
