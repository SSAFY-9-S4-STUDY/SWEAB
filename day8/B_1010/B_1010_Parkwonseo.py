def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
        
    
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = factorial(m) // (factorial(m - n) * factorial(n))
    print(result)