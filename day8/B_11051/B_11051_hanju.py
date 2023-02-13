def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

n, k = map(int,input().split())
numerator = factorial(n)
dinominator = factorial(k)*factorial(n-k)
print((numerator//dinominator)%10007)