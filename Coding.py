# 12852 S1 : 1로 만들기 2
N = int(input())
min_op_count = [0] * (N+1)
op_list = [0,0]
for i in range(2, N+1): # 상향식 DP
    operator = 3
    min_op_count[i] = min_op_count[i-1] + 1 # -1연산적용

    if (i % 3) == 0:
        prev = min_op_count[i // 3] + 1
        if prev < min_op_count[i]:
            operator = 1
        min_op_count[i] = min(min_op_count[i], prev)
    if (i % 2) == 0:
        prev = min_op_count[i // 2] + 1
        if prev < min_op_count[i]:
            operator = 2
        min_op_count[i] = min(min_op_count[i], prev)
    op_list.append(operator)

print(min_op_count[N])
index = 2
print(N, end=" ")
while True: # 연산자를 역추적하여 최소화 과정출력
    if op_list[index] == 3:
        N = N - 1
        index += 1
    elif op_list[index] == 2:
        N = N // 2
        index *= 2
    elif op_list[index] == 1:
        N = N // 3
        index *= 3
    print(N, end=" ")
    if (N == 1):
        break
