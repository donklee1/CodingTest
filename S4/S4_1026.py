# 1026 S4
from sys import stdin
import sys
import itertools

def InnerProduct(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum

N = int(input())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))

A.sort() # 오름차순
B.sort(reverse=True) #내림차순
print(InnerProduct(A,B))