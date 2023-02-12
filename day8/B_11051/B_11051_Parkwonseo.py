n, k = map(int, input().split())

result = 1
for i in range(max(k, n - k) + 1, n + 1):
    result *= i
print(result)
for i in range(1, min(k, n - k) + 1):
    result //= i

print(result % 10007)