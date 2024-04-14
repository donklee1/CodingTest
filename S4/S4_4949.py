while True:
    S = input()
    if (S == "."):
        break
    L = list(S)
    STACK1 = []
    error = False
    prev_push = ""
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
    if error == True:
        print("no")
    elif len(STACK1) == 0:
        print("yes")
    else:
        print("no")
        
