# 2529 S1
from sys import stdin

count = int(stdin.readline().rstrip()) # 부등호 개수
OP_LIST = list(stdin.readline().split())
RESULT = []

def CheckPossible(RESULT, index, num):
    OK = False
    if (OP_LIST[index-1] == "<") and (RESULT[index-1] < num):
        OK = True
    if (OP_LIST[index-1] == ">") and (RESULT[index-1] > num):
        OK = True
    return OK

min_val = 1e20
max_val = -1
def DFS():
    global min_val
    global max_val
    if len(RESULT) == (len(OP_LIST) + 1):
        value = int(''.join(str(x) for x in RESULT)) #리스트 숫자를 합쳐 값으로
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value
        return

    for num in range(10):
        Condition = False
        if len(RESULT) == 0:
            Condition = True
        elif (num in RESULT) == False and CheckPossible(RESULT, len(RESULT), num) == True:
            Condition = True
        if Condition == True:
            RESULT.append(num)
            DFS()
            RESULT.pop()

DFS()
print(str(max_val).zfill(count+1))
print(str(min_val).zfill(count+1))
