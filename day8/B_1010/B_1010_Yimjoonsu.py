T = int(input())

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(M-N) * factorial(N))))