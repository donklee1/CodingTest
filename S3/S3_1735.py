import math
A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

A3 = (A1 * B2) + (B1 * A2)
B3 = B1 * B2

GCD = math.gcd(A3, B3)
A3 = A3 // GCD
B3 = B3 // GCD

print(A3, B3)
