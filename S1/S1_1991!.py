# S1-1991 이진트리 탐색
from sys import stdin
tree = dict() # 딕셔너리 사용!!

N = int(input())
for _ in range(N):
    root, left, right = input().split()
    tree[root] = (left, right)

def pre_order(v):
    if v != ".":
        print(v, end="")
        pre_order(tree[v][0])
        pre_order(tree[v][1])

def in_order(v):
    if v != ".":
        in_order(tree[v][0])
        print(v, end="")
        in_order(tree[v][1])

def post_order(v):
    if v != ".":
        post_order(tree[v][0])
        post_order(tree[v][1])
        print(v, end="")

pre_order("A")
print("")
in_order("A")
print("")
post_order("A")
print("")

