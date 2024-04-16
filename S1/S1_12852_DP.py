# 12852 S1 : 1로 만들기 2
N = int(input().rstrip())
min_op_count = [0] * (N+1)
val_list = [0] * (N+1)
for i in range(2, N+1): # 상향식 DP
    operator = 3
    min_op_count[i] = min_op_count[i-1] + 1 # -1연산적용
    val_list[i] = i -1

    if (i % 3) == 0:
        prev = min_op_count[i // 3] + 1
        if prev < min_op_count[i]:
            operator = 1
            val_list[i] = i // 3
        min_op_count[i] = min(min_op_count[i], prev)
    if (i % 2) == 0:
        prev = min_op_count[i // 2] + 1
        if prev < min_op_count[i]:
            operator = 2
            val_list[i] = i // 2
        min_op_count[i] = min(min_op_count[i], prev)

print(min_op_count[N])
index = N
while index >= 1:
    print(index, end=' ')
    index = val_list[index]
