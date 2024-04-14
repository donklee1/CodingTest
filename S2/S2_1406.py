# 1406 S2 에디터
from sys import stdin

class DNode:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLink:
    def __init__(self):
        self.head = DNode("")
        self.tail = DNode("")
        self.size = 0
    
    def append(self, data):
        node = DNode(data)
        if self.size == 0:
            self.head.next = node
            self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
            self.size = 1
        else:
            last_node = self.tail.prev
            self.tail.prev = node
            node.prev = last_node
            node.next = self.tail
            last_node.next = node
            self.size += 1

    def insert(self, node2, data):
        if node2 == self.tail:
            self.append(data)
        else: # node1 <-> new_node <-> node2
            new_node = DNode(data)
            node1 = node2.prev
            node1.next = new_node
            new_node.prev = node1
            node2.prev = new_node
            new_node.next = node2

    def delete(self, node):
        if node != self.head:
            node1 = node.prev
            node2 = node.next
            node1.next = node2
            node2.prev = node1

    def get_data(self, node):
        return node.data

    def printList(self, delimeter = ' '):
        if self.size == 0:
            return
        p = self.head.next
        while p != self.tail:
            print(p.data, end = delimeter)
            p = p.next
        print("")

S = list(stdin.readline().rstrip())
LL = DLink()
for c in S:
    LL.append(c)

N = int(stdin.readline().rstrip())
cursor = LL.tail
for _ in range(N):
    CMD = list(stdin.readline().split())
    if CMD[0] == "L":
        if cursor.prev != LL.head:
            cursor = cursor.prev
    elif CMD[0] == "D":
        if cursor != LL.tail:
            cursor = cursor.next
    elif CMD[0] == "B":
        LL.delete(cursor.prev)
    elif CMD[0] == "P":
        LL.insert(cursor, CMD[1])

LL.printList('')