# 12852 S1 : 1로 만들기 2
N = int(input())
min_op_count = [0] * (N+1)
op_list = [0,0]
for i in range(2, N+1): # 상향식 DP
    operator = 3
    min_op_count[i] = min_op_count[i-1] + 1 # -1연산적용

    if (i % 3) == 0:
        min_op_count[i] = min(min_op_count[i], min_op_count[i // 3] + 1)
        operator = 1
    if (i % 2) == 0:
        min_op_count[i] = min(min_op_count[i], min_op_count[i // 2] + 1)
        operator = 2
    op_list.append(operator)

print(min_op_count)
print(min_op_count[N])
print(op_list)
