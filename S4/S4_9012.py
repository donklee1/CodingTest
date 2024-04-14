N = int(input())
for _ in range(N):
    S = input()
    LIST = list(S)
    STACK = []
    RESULT = True
    for c in LIST:
        if c == "(":
            STACK.append("(")
        elif c == ")":
            if len(STACK) > 0:
                STACK.pop()
            else:
                RESULT = False
                break
    if RESULT == False:
        print("NO")
    elif len(STACK) == 0:
        print("YES")
    else:
        print("NO")    
