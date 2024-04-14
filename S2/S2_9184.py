# def w(a,b,c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     elif a < b and b < c:
#         return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
#     else:
#         return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

memo = {}

def dp_w(a, b, c):
    if (a, b, c) in memo:
        return memo[(a, b, c)] # 이미 저장된 것
    
    if a <= 0 or b <= 0 or c <= 0:
        memo[(a, b, c)] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = dp_w(20, 20, 20)
        return memo[(a, b, c)]
    elif a < b and b < c:
        memo[(a, b, c)] = dp_w(a, b, c-1) + dp_w(a, b-1, c-1) - dp_w(a, b-1, c)
        return memo[(a, b, c)]
    else:
        memo[(a, b, c)] = dp_w(a-1, b, c) + dp_w(a-1, b-1, c) + dp_w(a-1, b, c-1) - dp_w(a-1, b-1, c-1)
        return memo[(a, b, c)]    

while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = dp_w(a,b,c)
    print("w(",a,", ",b,", ",c,") = ", result, sep='')
