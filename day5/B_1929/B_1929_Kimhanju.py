M, N = map(int, input().split())

# N 까지의 숫자를 리스트로 저장
numbers = [i for i in range(N+1)]

# N 이하의 수는 소수이거나 N 제곱근 이하의 수들의 곱으로 이루어져있음
for i in range(2, int(N**0.5)+1):
    if numbers[i]:  # i가 소수이면
        for j in range(2, N//i+1):  # N 이하의 i 곱들은 모두 소수 X
            numbers[i*j] = 0

for i in numbers[M:]:  # M 이상의 소수 출력
    if i > 1:  # 1은 소수 X
        print(i)