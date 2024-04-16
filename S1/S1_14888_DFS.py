import sys

def CALC(NUM, OP_STACK):
     VAL = NUM[0]
     for i in range(0, len(OP_STACK)):
          #print("i=", i, "NUM=", NUM)
          if OP_STACK[i] == '+':
               VAL += NUM[i+1]
          elif OP_STACK[i] == '-':  
               VAL -= NUM[i+1]
          elif OP_STACK[i] == '*':  
               VAL *= NUM[i+1]
          elif OP_STACK[i] == '/':  
               if VAL < 0 and (NUM[i+1] > 0):
                    VAL = -((-VAL) // NUM[i+1])
               else: 
                    VAL //= NUM[i+1]
     return VAL

def DFS(OP_STACK, OP_USED):
     global MIN_VAL
     global MAX_VAL
     global NUM
     if len(OP_STACK) == OP_COUNT:
          V = CALC(NUM, OP_STACK)
          if (V < MIN_VAL):
               MIN_VAL = V
          if (V > MAX_VAL):
               MAX_VAL = V
          return
     for idx, op in enumerate(OP2):
          if len(OP_STACK) == 0 or OP_USED[idx] == False:
            OP_USED[idx] = True
            OP_STACK.append(op)
            DFS(OP_STACK, OP_USED)
            OP_STACK.pop()
            OP_USED[idx] = False

MIN_VAL = 1000000000
MAX_VAL = -1000000000
#N = 6
#NUM = list(map(int, "1 2 3 4 5 6".split()))
#OP1 = list(map(int, "2 1 1 1".split()))
N = int(input())
NUM = list(map(int, input().split()))
OP1 = list(map(int, input().split()))
OP2 = []
for index, cnt in enumerate(OP1):
    if index == 0:
        for _ in range(cnt):
            OP2.append("+")
    elif index == 1:
        for _ in range(cnt):
            OP2.append("-")
    elif index == 2:
        for _ in range(cnt):
            OP2.append("*")
    elif index == 3:
        for _ in range(cnt):
            OP2.append("/")
OP_COUNT = len(OP2)
OP_USED = [False] * OP_COUNT
OP_STACK = []
DFS(OP_STACK, OP_USED)
print(MAX_VAL)
print(MIN_VAL)
