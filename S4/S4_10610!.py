# S4_10610 숫자를 섞어 30의 배수가되는 큰수
N = list(input())
N = sorted(N, reverse=True)

if N[-1] != '0' : # 끝자리 0이어야 함
    print(-1)
else:
    sum = 0
    for i in N:
        sum += int(i) #모든 자리수의 합이..
    if sum % 3 == 0 : # 3의 배수가 되는 경우
        print(''.join(N))
    else:
        print(-1)
