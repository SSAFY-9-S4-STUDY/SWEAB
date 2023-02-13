def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer


T = int(input())

for _ in range(T):
    start, arrive = map(int,input().split())
    numerator = factorial(arrive)
    dinominator = factorial(start)*factorial(arrive-start)
    print(int(numerator/dinominator))