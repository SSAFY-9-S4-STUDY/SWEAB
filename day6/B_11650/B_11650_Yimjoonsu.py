N = int(input())
arr = []

for test_case in range(1, N+1):
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort()

for i, j in arr:
    print(i, j)