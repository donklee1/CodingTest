# S4_9012 올바른 괄호문자열
N = int(input())
for _ in range(N):
    S = input() # (,) 로만 이루어짐
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
    if len(STACK) == 0 and RESULT == True:
        print("YES")
    else:
        print("NO")    
