# S4_4949 () [] 괄호짝짓기
while True:
    S = input()
    if (S == "."):
        break
    L = list(S)
    STACK1 = []
    for c in L:
        if c == '(' or c == '[': 
            STACK1.append(c)
        elif c == ')':
            if len(STACK1) > 0 and STACK1[-1] == "(":
                STACK1.pop()
            else:
                STACK1.append(c)
        elif c == ']':
            if len(STACK1) > 0 and STACK1[-1] == "[":
                STACK1.pop()
            else:
                STACK1.append(c)
    if len(STACK1) == 0:
        print("yes")
    else:
        print("no")
        
