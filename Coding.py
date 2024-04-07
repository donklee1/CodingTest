# 11723 s5
from sys import stdin

DATA = set()
M = int(stdin.readline().rstrip())
for _ in range(M):
    cmd = list(stdin.readline().split())
    if cmd[0] == "add":
        param = int(cmd[1])
        DATA.add(param)
    elif cmd[0] == "remove":
        param = int(cmd[1])
        if (param in DATA) == True:
            DATA.remove(param)
    elif cmd[0] == "check":
        param = int(cmd[1])
        if (param in DATA) == True:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        param = int(cmd[1])
        if (param in DATA) == True:
            DATA.remove(param)
        else:
            DATA.add(param)
    elif cmd[0] == "all":
        DATA.clear()
        for i in range(1, 21, 1):
             DATA.add(i)
    elif cmd[0] == "empty":
        DATA.clear()
