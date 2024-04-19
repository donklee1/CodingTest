# S1-1991 이진트리 탐색
from sys import stdin
tree = dict() # 딕셔너리 사용!!
count = int(input())
for i in range(count):
    root, left, right = input().split()
    tree[root] = left,right # tuple과 동일 (left, right)

def pre_order(data): # 성공
    if data != ".":
        print(data, end="")
        pre_order(tree[data][0]) #튜플 첫항 액세스 방법
        pre_order(tree[data][1]) #튜플 두번째 액세스 방법

def in_order(data):
    if data != ".":
        left, right = tree[data]
        in_order(left)
        print(data, end="")
        in_order(right)

def post_order(data):
    if data != ".":
        post_order(tree[data][0])
        post_order(tree[data][1])
        print(data, end="")

pre_order("A")
print("")
in_order("A")
print("")
post_order("A")
