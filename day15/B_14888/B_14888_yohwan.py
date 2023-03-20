import itertools

# 입력 값 받기, 순열리스트 만들기
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
operator_list = '+' * add + '-' * sub + '*' * mul + '/' * div
op_list = itertools.permutations(operator_list, N - 1)

# 답 도출해낼 변수들 지정해주기
maxv = -1000000000
minv = 1000000000

# 위에 만든 연산자순열리스트마다 max, min 값에 해당하는지
for op in op_list:
    result = numbers[0]
    for i in range(1, N):
        if op[i - 1] == '+':
            result += numbers[i]
        elif op[i - 1] == '-':
            result -= numbers[i]
        elif op[i - 1] == '*':
            result *= numbers[i]
        elif op[i - 1] == '/':
            if result >= 0:
                result //= numbers[i]
            else:
                result = -1 * (result * (-1) // numbers[i])

    if result > maxv:
        maxv = result
    if result < minv:
        minv = result

print(maxv)
print(minv)
