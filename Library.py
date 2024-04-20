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
class SNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

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
            self.size += 1

    def delete(self, node):
        if node != self.head:
            node1 = node.prev
            node2 = node.next
            node1.next = node2
            node2.prev = node1
            self.size -= 1

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

# ----- 다익스트라 : 최소경로 -----
graph = {  # dict() of dict()
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
import heapq
def dijkstra1(graph, start): # dict() of dict() 사용버젼
  dist_list = [int(1e9)] * len(graph)  # 처음 초기값은 무한대
  dist_list[start] = 0  # 시작 값은 0이어야 함
  queue = []
  heapq.heappush(queue, [dist_list[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    dist, node = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if dist_list[node] < dist:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
      continue
    
    for next_node, next_dist in graph[node].items():
      distance = dist + next_dist  # 해당 노드를 거쳐 갈 때 거리
      if distance < dist_list[next_node]:  # 알고 있는 거리 보다 작으면 갱신
        dist_list[next_node] = distance
        heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
  return dist_list

  return distance_state
  # {'A': 0, 'B': 6, 'C': 1, 'D': 2, 'E': 5, 'F': 6}
  # call --> dijkstra(graph, 'A')

graph2 = [  # list of list
    [('B', 8), ('C', 1), ('D', 2)],
    [],
    [ ('B', 5), ('D', 2)],
    [ ('E', 3), ('F', 5)],
    [ ('F', 1)],
    [ ('A', 5)]
]

def dijkstra2(graph, start): # list of list (노드가 숫자인 경우만 가능)
    dist_list = [int(1e9)] * len(graph)  # 처음 초기값은 무한대
    dist_list[start] = 0  # 시작 노드까지의 거리는 0
    queue = []
    heapq.heappush(queue, [dist_list[start], start])  # 시작 노드부터 탐색 시작

    while queue:  # queue에 남아있는 노드가 없을 때까지 탐색
        dist, node = heapq.heappop(queue)  # 탐색할 노드, 거리
        if dist_list[node] < dist: # 기존 최단거리보다 멀다면 무시
            continue
        for next_node, next_dist in graph[node]:
            distance = dist + next_dist  # 인접노드까지의 거리
            if distance < dist_list[next_node]:  # 기존 거리 보다 짧으면 갱신
                dist_list[next_node] = distance
                heapq.heappush(queue, [distance, next_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return dist_list