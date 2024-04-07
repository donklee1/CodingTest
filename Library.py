# Library.py
#        생성   삽입      삭제
# list = []     .append(x) .remove(x) .pop()/.pop(0)
# tuple= ()
# dict = {}     d[k]=v     del d[k]
# set  = set()  .add(x)    .remove(x)
# queue
# deque         .append(x) .popleft()  -- 양방항 꺼냄
# heapq = []    heapq.heappush(heap,x) heapq.heappop(heap)
#         최소값 heap[0], 최대값 heap[-1]
# ---------- Linked List -------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---------- Trie -------------------------------
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}       

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        if current_node.data:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words         

# ----- 소수판정 -----
def IsPrime(N):
    if N < 2:
        return False
    elif N == 2:
        return True
    if N % 2 == 0:
        return False
    LastVal = (int)(N ** (1/2)) + 1
    for denom in range(3,LastVal, 2):
        if N % denom == 0:
            return False
    return True

# ----- 행렬곱 -----
def MatMul(A, B):
    rows = len(A)
    cols = len(B[0])
    inner = len(A[0])
    C = [[0] * cols for _ in range(rows)]
    for a in range(rows):
        for b in range(cols):
            sum = 0
            for k in range(inner):
                sum += A[a][k] * B[k][b]
            C[a][b] = sum
    return C                
