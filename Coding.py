# 1406 S2 에디터
from sys import stdin

class ListNode:
    def __init__(self, val=0, prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

def PrintNode(node):
    while node:
        print(node.val, end="")
        node = node.next
    print("")

S = list(stdin.readline())
command_count = int(stdin.readline().rstrip())

head_node = ListNode(S[0])
curr_node = head_node
for i in range(1, len(S)):
    new_node = ListNode(S[i])
    curr_node.next = new_node
    new_node.prev = curr_node
    curr_node = curr_node.next

PrintNode(head_node)

for _ in range(command_count):
    CMD_LIST = stdin.readline().split()
    if CMD_LIST[0] == "L": # 커서 <-- 이동
        if curr_node.prev != None:
            curr_node = curr_node.prev
    elif CMD_LIST[0] == "D": # 커서 --> 이동
        if curr_node.next != None:
            curr_node = curr_node.next
    elif CMD_LIST[0] == "B": # 커서왼쪽 삭제
        if curr_node.prev != None:
            prev_node = curr_node.prev
            next_node = curr_node.next
            
            #curr_node.prev = curr_node.prev.prev
    elif CMD_LIST[0] == "P": # 삽입
        new_node = ListNode(CMD_LIST[1], curr_node.prev, curr_node)
        prev = new_node.prev
        if prev != None:
            prev.next = new_node
        curr_node.prev = new_node

print(head_node)
PrintNode(head_node)

